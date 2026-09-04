import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
from io import BytesIO

# ==================== CẤU HÌNH ====================
PASSWORD = "Minklaus"
DATA_FILE = "customers.json"

# ==================== HÀM HỖ TRỢ ====================
def load_customers():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_customers(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def init_session():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "customers" not in st.session_state:
        st.session_state.customers = load_customers()

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Customer Manager",
    page_icon="📋",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ==================== CSS TÙY CHỈNH ====================
st.markdown("""
<style>
    /* Tổng thể */
    .stApp {
        background: linear-gradient(160deg, #f8fafc 0%, #eef2ff 45%, #f1f5f9 100%);
    }

    /* Card form */
    .form-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 28px 32px 32px;
        box-shadow: 0 10px 25px -5px rgba(0,0,0,0.07), 0 4px 6px -4px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }

    /* Header trang 1 */
    .page-header {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 8px;
    }
    .page-icon {
        width: 52px;
        height: 52px;
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        color: white;
        box-shadow: 0 4px 14px rgba(79, 70, 229, 0.35);
    }
    .page-title {
        font-size: 26px;
        font-weight: 700;
        color: #0f172a;
        margin: 0;
        letter-spacing: -0.3px;
    }
    .page-subtitle {
        color: #64748b;
        font-size: 14.5px;
        margin-top: 2px;
    }

    /* Info box */
    .info-box {
        background: #eef2ff;
        border: 1px solid #c7d2fe;
        border-radius: 12px;
        padding: 16px 18px;
        font-size: 13.5px;
        color: #3730a3;
        line-height: 1.55;
    }

    /* Nút */
    .stButton > button {
        border-radius: 10px !important;
        font-weight: 600 !important;
        height: 46px !important;
    }

    /* Form input */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 10px !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #0f172a;
    }
    section[data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    section[data-testid="stSidebar"] .stRadio label {
        color: #e2e8f0 !important;
    }
</style>
""", unsafe_allow_html=True)

init_session()

# ==================== SIDEBAR ====================
st.image("logo.jpg")
with st.sidebar:
    st.markdown("### 📋 Customer Manager")
    st.caption("Hệ thống quản lý khách hàng")
    st.markdown("---")

    page = st.radio(
        "Điều hướng",
        ["📝 Nhập khách hàng", "🔐 Admin"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.caption("Mật khẩu Admin: **Minklaus**")

# ==================== TRANG 1: NHẬP KHÁCH HÀNG ====================
if page == "📝 Nhập khách hàng":

    # Header đẹp
    st.markdown("""
    <div class="page-header">
        <div class="page-icon">📝</div>
        <div>
            <div class="page-title">Nhập khách hàng mới</div>
            <div class="page-subtitle">Điền đầy đủ thông tin bên dưới để lưu vào hệ thống</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")  # khoảng cách

    # Layout 2 cột: Form + Hướng dẫn
    col_form, col_info = st.columns([1.7, 1], gap="large")

    with col_form:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)

        with st.form("customer_form", clear_on_submit=True):
            # Hàng 1: Tên + SĐT
            c1, c2 = st.columns(2)
            with c1:
                name = st.text_input(
                    "Tên khách hàng *",
                    placeholder="Nguyễn Văn A",
                    help="Bắt buộc"
                )
            with c2:
                phone = st.text_input(
                    "Số điện thoại *",
                    placeholder="0912 345 678",
                    help="Bắt buộc"
                )

            # Địa chỉ
            address = st.text_input(
                "Địa chỉ",
                placeholder="Số nhà, tên đường, phường/xã, quận/huyện..."
            )

            # Ghi chú
            note = st.text_area(
                "Ghi chú",
                placeholder="Thông tin bổ sung về khách hàng (nếu có)...",
                height=110
            )

            st.write("")  # khoảng cách nhẹ

            submitted = st.form_submit_button(
                "💾  Lưu khách hàng",
                use_container_width=True,
                type="primary"
            )

            if submitted:
                if not name.strip() or not phone.strip():
                    st.error("Vui lòng nhập đầy đủ **Tên khách hàng** và **Số điện thoại**!")
                else:
                    new_customer = {
                        "id": int(datetime.now().timestamp() * 1000),
                        "name": name.strip(),
                        "phone": phone.strip(),
                        "address": address.strip(),
                        "note": note.strip(),
                        "created_at": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    }
                    st.session_state.customers.append(new_customer)
                    save_customers(st.session_state.customers)
                    st.success(f"✅ Đã lưu khách hàng **{name.strip()}** thành công!")

        st.markdown('</div>', unsafe_allow_html=True)

    with col_info:
        st.markdown("""
        <div class="info-box">
            <strong>📌 Hướng dẫn nhanh</strong><br><br>
            • Các trường có dấu <strong>*</strong> là bắt buộc<br>
            • Số điện thoại nên nhập đủ 10 số<br>
            • Ghi chú giúp bạn nhớ thông tin quan trọng<br>
            • Dữ liệu sẽ được lưu ngay sau khi bấm nút
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.markdown("""
        <div class="info-box" style="background:#f0fdf4; border-color:#bbf7d0; color:#166534;">
            <strong>💡 Mẹo</strong><br><br>
            Sau khi lưu, bạn có thể vào trang <strong>Admin</strong> để xem danh sách và xuất file Excel.
        </div>
        """, unsafe_allow_html=True)

# ==================== TRANG 2: ADMIN ====================
else:
    st.markdown("""
    <div class="page-header">
        <div class="page-icon">🔐</div>
        <div>
            <div class="page-title">Khu vực Admin</div>
            <div class="page-subtitle">Quản lý và xuất dữ liệu khách hàng</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Đăng nhập
    if not st.session_state.logged_in:
        st.info("Vui lòng nhập mật khẩu để tiếp tục")

        with st.form("login_form"):
            password = st.text_input("Mật khẩu", type="password", placeholder="Nhập mật khẩu...")
            login_btn = st.form_submit_button("Đăng nhập", use_container_width=True, type="primary")

            if login_btn:
                if password == PASSWORD:
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("❌ Sai mật khẩu! Vui lòng thử lại.")

    # Nội dung Admin
    else:
        # Thanh công cụ
        c1, c2, c3 = st.columns([2, 1, 1])

        with c1:
            st.markdown(f"**Tổng số khách hàng:** `{len(st.session_state.customers)}`")

        with c2:
            if st.button("🚪 Thoát", use_container_width=True):
                st.session_state.logged_in = False
                st.rerun()

        with c3:
            if st.session_state.customers:
                df = pd.DataFrame(st.session_state.customers)
                df = df.rename(columns={
                    "name": "Tên khách hàng",
                    "phone": "Số điện thoại",
                    "address": "Địa chỉ",
                    "note": "Ghi chú",
                    "created_at": "Thời gian lưu"
                })
                df.insert(0, "STT", range(1, len(df) + 1))
                df = df[["STT", "Tên khách hàng", "Số điện thoại", "Địa chỉ", "Ghi chú", "Thời gian lưu"]]

                output = BytesIO()
                with pd.ExcelWriter(output, engine="openpyxl") as writer:
                    df.to_excel(writer, index=False, sheet_name="Danh sách KH")
                excel_data = output.getvalue()

                st.download_button(
                    label="📥 Xuất Excel",
                    data=excel_data,
                    file_name=f"Danh_sach_khach_hang_{datetime.now().strftime('%Y%m%d')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )

        st.markdown("---")

        # Bảng dữ liệu
        if not st.session_state.customers:
            st.info("📋 Chưa có khách hàng nào. Hãy thêm từ trang **Nhập khách hàng**.")
        else:
            display_data = []
            for i, c in enumerate(st.session_state.customers, 1):
                display_data.append({
                    "STT": i,
                    "Tên khách hàng": c["name"],
                    "Số điện thoại": c["phone"],
                    "Địa chỉ": c.get("address") or "—",
                    "Ghi chú": c.get("note") or "—",
                    "Thời gian": c["created_at"]
                })

            st.dataframe(
                pd.DataFrame(display_data),
                use_container_width=True,
                hide_index=True
            )

            # Xóa khách hàng
            st.markdown("#### 🗑️ Xóa khách hàng")
            options = {f"{c['name']} ({c['phone']})": c["id"] for c in st.session_state.customers}
            selected = st.selectbox("Chọn khách hàng muốn xóa", list(options.keys()))

            if st.button("Xóa khách hàng đã chọn", type="secondary"):
                customer_id = options[selected]
                st.session_state.customers = [c for c in st.session_state.customers if c["id"] != customer_id]
                save_customers(st.session_state.customers)
                st.success("Đã xóa khách hàng!")
                st.rerun()
