import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

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

# ==================== GIAO DIỆN ====================
st.set_page_config(
    page_title="Customer Manager",
    page_icon="📋",
    layout="centered",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh
st.markdown("""
<style>
    .main-title {
        font-size: 28px;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 4px;
    }
    .sub-title {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 24px;
    }
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
    }
    div[data-testid="stForm"] {
        background: #f8fafc;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

init_session()

# ==================== SIDEBAR MENU ====================
st.sidebar.markdown("### 📋 Customer Manager")
st.sidebar.caption("Quản lý danh sách khách hàng")

page = st.sidebar.radio(
    "Chọn trang",
    ["📝 Nhập khách hàng", "🔐 Admin"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.caption("Mật khẩu Admin: `Minklaus`")

# ==================== TRANG 1: NHẬP KHÁCH HÀNG ====================
if page == "📝 Nhập khách hàng":
    st.markdown('<div class="main-title">Nhập thông tin khách hàng</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Điền thông tin bên dưới rồi bấm Lưu</div>', unsafe_allow_html=True)

    with st.form("customer_form", clear_on_submit=True):
        name = st.text_input("Tên khách hàng *", placeholder="Nguyễn Văn A")
        phone = st.text_input("Số điện thoại *", placeholder="0912 345 678")
        address = st.text_input("Địa chỉ", placeholder="Số nhà, đường, quận/huyện...")
        note = st.text_area("Ghi chú", placeholder="Ghi chú thêm về khách hàng...", height=100)

        submitted = st.form_submit_button("💾 Lưu khách hàng", use_container_width=True, type="primary")

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
                st.success(f"✅ Đã lưu khách hàng **{name}** thành công!")

# ==================== TRANG 2: ADMIN ====================
else:
    st.markdown('<div class="main-title">🔐 Khu vực Admin</div>', unsafe_allow_html=True)

    # --- Đăng nhập ---
    if not st.session_state.logged_in:
        st.markdown('<div class="sub-title">Nhập mật khẩu để truy cập</div>', unsafe_allow_html=True)

        with st.form("login_form"):
            password = st.text_input("Mật khẩu", type="password", placeholder="Nhập mật khẩu...")
            login_btn = st.form_submit_button("Đăng nhập", use_container_width=True, type="primary")

            if login_btn:
                if password == PASSWORD:
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("❌ Sai mật khẩu! Vui lòng thử lại.")

    # --- Nội dung Admin sau khi đăng nhập ---
    else:
        col1, col2, col3 = st.columns([2, 1, 1])

        with col1:
            st.markdown(f"**Tổng số khách hàng:** `{len(st.session_state.customers)}`")

        with col2:
            if st.button("🚪 Thoát", use_container_width=True):
                st.session_state.logged_in = False
                st.rerun()

        with col3:
            if st.session_state.customers:
                # Tạo file Excel
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

                # Xuất Excel
                from io import BytesIO
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

        # Hiển thị bảng
        if not st.session_state.customers:
            st.info("📋 Chưa có khách hàng nào. Hãy thêm từ trang **Nhập khách hàng**.")
        else:
            # Tạo dataframe để hiển thị
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

            df_display = pd.DataFrame(display_data)
            st.dataframe(df_display, use_container_width=True, hide_index=True)

            # Phần xóa khách hàng
            st.markdown("#### Xóa khách hàng")
            options = {f"{c['name']} ({c['phone']})": c["id"] for c in st.session_state.customers}
            selected = st.selectbox("Chọn khách hàng muốn xóa", list(options.keys()))

            if st.button("🗑️ Xóa khách hàng đã chọn", type="secondary"):
                customer_id = options[selected]
                st.session_state.customers = [c for c in st.session_state.customers if c["id"] != customer_id]
                save_customers(st.session_state.customers)
                st.success("Đã xóa khách hàng!")
                st.rerun()
