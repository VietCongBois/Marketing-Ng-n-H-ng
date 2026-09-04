<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Customer Manager | Quản lý Khách hàng</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.sheetjs.com/xlsx-0.20.3/package/dist/xlsx.full.min.js"></script>
  <style>
    :root {
      --primary: #4f46e5;
      --primary-hover: #4338ca;
      --primary-light: #eef2ff;
      --success: #059669;
      --success-hover: #047857;
      --danger: #dc2626;
      --danger-hover: #b91c1c;
      --slate-50: #f8fafc;
      --slate-100: #f1f5f9;
      --slate-200: #e2e8f0;
      --slate-300: #cbd5e1;
      --slate-400: #94a3b8;
      --slate-500: #64748b;
      --slate-600: #475569;
      --slate-700: #334155;
      --slate-800: #1e293b;
      --slate-900: #0f172a;
    SyntaxError: invalid decimal literal
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.05);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.08), 0 4px 6px -4px rgb(0 0 0 / 0.05);
      --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.08);
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background: linear-gradient(160deg, #f1f5f9 0%, #e0e7ff 50%, #f8fafc 100%);
      min-height: 100vh;
      color: var(--slate-800);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }

    /* ===== CONTAINER ===== */
    .app {
      max-width: 960px;
      margin: 0 auto;
      padding: 28px 20px 40px;
    }

    /* ===== HEADER ===== */
    .header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 28px;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .brand-logo {
      width: 44px;
      height: 44px;
      background: linear-gradient(135deg, #4f46e5, #7c3aed);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 700;
      font-size: 18px;
      box-shadow: 0 4px 12px rgba(79, 70, 229, 0.35);
    }

    .brand-text h1 {
      font-size: 20px;
      font-weight: 700;
      color: var(--slate-900);
      letter-spacing: -0.3px;
    }

    .brand-text p {
      font-size: 13px;
      color: var(--slate-500);
      margin-top: 1px;
    }

    /* ===== NAV ===== */
    .nav {
      display: flex;
      background: white;
      border-radius: var(--radius);
      padding: 6px;
      box-shadow: var(--shadow);
      border: 1px solid var(--slate-200);
      margin-bottom: 24px;
    }

    .nav-btn {
      flex: 1;
      padding: 12px 16px;
      border: none;
      background: transparent;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 600;
      color: var(--slate-500);
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }

    .nav-btn:hover {
      color: var(--slate-700);
      background: var(--slate-50);
    }

    .nav-btn.active {
      background: var(--primary);
      color: white;
      box-shadow: 0 2px 8px rgba(79, 70, 229, 0.3);
    }

    /* ===== CARD ===== */
    .card {
      background: white;
      border-radius: var(--radius);
      box-shadow: var(--shadow-lg);
      border: 1px solid var(--slate-200);
      overflow: hidden;
    }

    .card-body {
      padding: 32px;
    }

    .card-header {
      padding: 20px 32px;
      border-bottom: 1px solid var(--slate-100);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }

    .card-title {
      font-size: 18px;
      font-weight: 700;
      color: var(--slate-900);
      letter-spacing: -0.2px;
    }

    /* ===== FORM ===== */
    .form-grid {
      display: grid;
      gap: 20px;
    }

    .form-group label {
      display: block;
      font-size: 13px;
      font-weight: 600;
      color: var(--slate-600);
      margin-bottom: 7px;
      letter-spacing: 0.2px;
    }

    .form-group label .required {
      color: var(--danger);
    }

    .form-control {
      width: 100%;
      padding: 11px 14px;
      border: 1.5px solid var(--slate-200);
      border-radius: 9px;
      font-size: 14.5px;
      color: var(--slate-800);
      background: var(--slate-50);
      transition: all 0.2s ease;
      font-family: inherit;
    }

    .form-control:hover {
      border-color: var(--slate-300);
    }

    .form-control:focus {
      outline: none;
      border-color: var(--primary);
      background: white;
      box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.12);
    }

    textarea.form-control {
      min-height: 100px;
      resize: vertical;
    }

    /* ===== BUTTONS ===== */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 11px 20px;
      border: none;
      border-radius: 9px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: inherit;
    }

    .btn:active {
      transform: scale(0.98);
    }

    .btn-primary {
      background: var(--primary);
      color: white;
      box-shadow: 0 2px 8px rgba(79, 70, 229, 0.3);
    }

    .btn-primary:hover {
      background: var(--primary-hover);
      box-shadow: 0 4px 12px rgba(79, 70, 229, 0.35);
    }

    .btn-success {
      background: var(--success);
      color: white;
      box-shadow: 0 2px 8px rgba(5, 150, 105, 0.25);
    }

    .btn-success:hover {
      background: var(--success-hover);
    }

    .btn-ghost {
      background: var(--slate-100);
      color: var(--slate-700);
    }

    .btn-ghost:hover {
      background: var(--slate-200);
    }

    .btn-danger {
      background: #fef2f2;
      color: var(--danger);
      border: 1px solid #fecaca;
    }

    .btn-danger:hover {
      background: #fee2e2;
    }

    .btn-sm {
      padding: 6px 12px;
      font-size: 12.5px;
      border-radius: 7px;
    }

    .btn-group {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    /* ===== LOGIN ===== */
    .login-wrapper {
      max-width: 380px;
      margin: 40px auto;
      text-align: center;
    }

    .login-icon {
      width: 64px;
      height: 64px;
      background: var(--primary-light);
      border-radius: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 20px;
      font-size: 28px;
    }

    .login-wrapper h2 {
      font-size: 22px;
      font-weight: 700;
      color: var(--slate-900);
      margin-bottom: 6px;
    }

    .login-wrapper p {
      color: var(--slate-500);
      font-size: 14px;
      margin-bottom: 28px;
    }

    .login-form {
      text-align: left;
    }

    .error-msg {
      color: var(--danger);
      font-size: 13px;
      margin-top: 10px;
      display: none;
      text-align: center;
    }

    /* ===== TABLE ===== */
    .table-container {
      overflow-x: auto;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
    }

    thead th {
      background: var(--slate-50);
      padding: 13px 16px;
      text-align: left;
      font-weight: 600;
      color: var(--slate-600);
      font-size: 12.5px;
      text-transform: uppercase;
      letter-spacing: 0.4px;
      border-bottom: 1px solid var(--slate-200);
      white-space: nowrap;
    }

    tbody td {
      padding: 14px 16px;
      border-bottom: 1px solid var(--slate-100);
      color: var(--slate-700);
      vertical-align: middle;
    }

    tbody tr {
      transition: background 0.15s ease;
    }

    tbody tr:hover {
      background: var(--slate-50);
    }

    tbody tr:last-child td {
      border-bottom: none;
    }

    .customer-name {
      font-weight: 600;
      color: var(--slate-900);
    }

    .badge {
      display: inline-flex;
      align-items: center;
      background: var(--primary-light);
      color: var(--primary);
      padding: 3px 10px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
    }

    /* ===== EMPTY STATE ===== */
    .empty-state {
      text-align: center;
      padding: 56px 20px;
      color: var(--slate-400);
    }

    .empty-state .icon {
      font-size: 42px;
      margin-bottom: 14px;
      opacity: 0.6;
    }

    .empty-state p {
      font-size: 15px;
      color: var(--slate-500);
    }

    /* ===== TOAST ===== */
    .toast {
      position: fixed;
      bottom: 28px;
      right: 28px;
      background: var(--slate-900);
      color: white;
      padding: 14px 20px;
      border-radius: 10px;
      font-size: 14px;
      font-weight: 500;
      box-shadow: var(--shadow-xl);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .toast.show {
      transform: translateY(0);
      opacity: 1;
    }

    .toast.success {
      background: var(--success);
    }

    /* ===== PAGE ===== */
    .page {
      display: none;
    }

    .page.active {
      display: block;
      animation: fadeIn 0.25s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 640px) {
      .app {
        padding: 16px 12px 32px;
      }

      .card-body {
        padding: 22px 18px;
      }

      .card-header {
        padding: 16px 18px;
      }

      .header {
        margin-bottom: 20px;
      }

      .brand-text h1 {
        font-size: 17px;
      }

      .nav-btn {
        font-size: 13px;
        padding: 10px 8px;
      }
    }
  </style>
</head>
<body>
  <div class="app">
    <!-- HEADER -->
    <div class="header">
      <div class="brand">
        <div class="brand-logo">CM</div>
        <div class="brand-text">
          <h1>Customer Manager</h1>
          <p>Quản lý danh sách khách hàng chuyên nghiệp</p>
        </div>
      </div>
    </div>

    <!-- NAVIGATION -->
    <div class="nav">
      <button class="nav-btn active" id="btnPage1" onclick="showPage(1)">
        <span>📝</span> Nhập khách hàng
      </button>
      <button class="nav-btn" id="btnPage2" onclick="showPage(2)">
        <span>🔐</span> Admin
      </button>
    </div>

    <!-- ========== PAGE 1: FORM ========== -->
    <div id="page1" class="page active">
      <div class="card">
        <div class="card-header">
          <div class="card-title">Thông tin khách hàng mới</div>
        </div>
        <div class="card-body">
          <form id="customerForm" onsubmit="saveCustomer(event)">
            <div class="form-grid">
              <div class="form-group">
                <label for="name">Tên khách hàng <span class="required">*</span></label>
                <input type="text" id="name" class="form-control" required placeholder="Nguyễn Văn A">
              </div>

              <div class="form-group">
                <label for="phone">Số điện thoại <span class="required">*</span></label>
                <input type="tel" id="phone" class="form-control" required placeholder="0912 345 678">
              </div>

              <div class="form-group">
                <label for="address">Địa chỉ</label>
                <input type="text" id="address" class="form-control" placeholder="Số nhà, đường, quận/huyện...">
              </div>

              <div class="form-group">
                <label for="note">Ghi chú</label>
                <textarea id="note" class="form-control" placeholder="Ghi chú thêm về khách hàng..."></textarea>
              </div>
            </div>

            <div style="margin-top: 28px;">
              <button type="submit" class="btn btn-primary">
                <span>💾</span> Lưu khách hàng
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- ========== PAGE 2: ADMIN ========== -->
    <div id="page2" class="page">
      <!-- Login -->
      <div id="loginSection" class="card">
        <div class="card-body">
          <div class="login-wrapper">
            <div class="login-icon">🔒</div>
            <h2>Đăng nhập Admin</h2>
            <p>Nhập mật khẩu để truy cập khu vực quản trị</p>

            <div class="login-form">
              <div class="form-group">
                <label for="password">Mật khẩu</label>
                <input type="password" id="password" class="form-control" placeholder="Nhập mật khẩu..." 
                       onkeydown="if(event.key==='Enter') checkPassword()">
              </div>
              <button class="btn btn-primary" style="width:100%; margin-top:8px;" onclick="checkPassword()">
                Đăng nhập
              </button>
              <p class="error-msg" id="errorMsg">Sai mật khẩu. Vui lòng thử lại.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Admin Content -->
      <div id="adminContent" style="display:none;">
        <div class="card">
          <div class="card-header">
            <div style="display:flex; align-items:center; gap:12px;">
              <div class="card-title">Danh sách khách hàng</div>
              <span class="badge" id="countBadge">0</span>
            </div>
            <div class="btn-group">
              <button class="btn btn-success" onclick="exportExcel()">
                <span>📥</span> Xuất Excel
              </button>
              <button class="btn btn-ghost" onclick="logout()">
                <span>🚪</span> Thoát
              </button>
            </div>
          </div>

          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th style="width:50px">#</th>
                  <th>Tên khách hàng</th>
                  <th>Số điện thoại</th>
                  <th>Địa chỉ</th>
                  <th>Ghi chú</th>
                  <th>Thời gian</th>
                  <th style="width:80px">Thao tác</th>
                </tr>
              </thead>
              <tbody id="customerTable">
                <!-- data -->
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast -->
  <div id="toast" class="toast"></div>

  <script>
    const ADMIN_PASSWORD = "Minklaus";
    let isLoggedIn = false;

    document.addEventListener('DOMContentLoaded', () => {
      renderTable();
    });

    function showPage(pageNum) {
      document.getElementById('page1').classList.remove('active');
      document.getElementById('page2').classList.remove('active');
      document.getElementById('btnPage1').classList.remove('active');
      document.getElementById('btnPage2').classList.remove('active');

      document.getElementById('page' + pageNum).classList.add('active');
      document.getElementById('btnPage' + pageNum).classList.add('active');

      if (pageNum === 2) {
        if (isLoggedIn) {
          document.getElementById('loginSection').style.display = 'none';
          document.getElementById('adminContent').style.display = 'block';
          renderTable();
        } else {
          document.getElementById('loginSection').style.display = 'block';
          document.getElementById('adminContent').style.display = 'none';
          document.getElementById('password').value = '';
          document.getElementById('errorMsg').style.display = 'none';
        }
      }
    }

    function checkPassword() {
      const input = document.getElementById('password').value;
      if (input === ADMIN_PASSWORD) {
        isLoggedIn = true;
        document.getElementById('loginSection').style.display = 'none';
        document.getElementById('adminContent').style.display = 'block';
        renderTable();
        showToast('Đăng nhập thành công', 'success');
      } else {
        document.getElementById('errorMsg').style.display = 'block';
        document.getElementById('password').value = '';
        document.getElementById('password').focus();
      }
    }

    function logout() {
      isLoggedIn = false;
      showPage(1);
      showToast('Đã thoát khỏi Admin');
    }

    function saveCustomer(e) {
      e.preventDefault();

      const name = document.getElementById('name').value.trim();
      const phone = document.getElementById('phone').value.trim();
      const address = document.getElementById('address').value.trim();
      const note = document.getElementById('note').value.trim();

      if (!name || !phone) {
        showToast('Vui lòng nhập đầy đủ Tên và Số điện thoại');
        return;
      }

      const customers = getCustomers();
      customers.push({
        id: Date.now(),
        name,
        phone,
        address,
        note,
        createdAt: new Date().toLocaleString('vi-VN')
      });

      localStorage.setItem('customers', JSON.stringify(customers));
      document.getElementById('customerForm').reset();
      showToast('Đã lưu khách hàng thành công', 'success');
    }

    function getCustomers() {
      return JSON.parse(localStorage.getItem('customers') || '[]');
    }

    function renderTable() {
      const customers = getCustomers();
      const tbody = document.getElementById('customerTable');
      const badge = document.getElementById('countBadge');

      badge.textContent = customers.length;

      if (customers.length === 0) {
        tbody.innerHTML = `
          <tr>
            <td colspan="7">
              <div class="empty-state">
                <div class="icon">📋</div>
                <p>Chưa có khách hàng nào.<br>Hãy thêm từ trang <strong>Nhập khách hàng</strong>.</p>
              </div>
            </td>
          </tr>
        `;
        return;
      }

      tbody.innerHTML = customers.map((c, index) => `
        <tr>
          <td style="color:var(--slate-400); font-weight:500;">${index + 1}</td>
          <td class="customer-name">${escapeHtml(c.name)}</td>
          <td>${escapeHtml(c.phone)}</td>
          <td>${escapeHtml(c.address || '—')}</td>
          <td style="max-width:180px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;" title="${escapeHtml(c.note || '')}">
            ${escapeHtml(c.note || '—')}
          </td>
          <td style="font-size:13px; color:var(--slate-500); white-space:nowrap;">${c.createdAt}</td>
          <td>
            <button class="btn btn-danger btn-sm" onclick="deleteCustomer(${c.id})">Xóa</button>
          </td>
        </tr>
      `).join('');
    }

    function deleteCustomer(id) {
      if (!confirm('Bạn có chắc muốn xóa khách hàng này?')) return;

      let customers = getCustomers();
      customers = customers.filter(c => c.id !== id);
      localStorage.setItem('customers', JSON.stringify(customers));
      renderTable();
      showToast('Đã xóa khách hàng');
    }

    function exportExcel() {
      const customers = getCustomers();
      if (customers.length === 0) {
        showToast('Không có dữ liệu để xuất');
        return;
      }

      const data = customers.map((c, i) => ({
        'STT': i + 1,
        'Tên khách hàng': c.name,
        'Số điện thoại': c.phone,
        'Địa chỉ': c.address || '',
        'Ghi chú': c.note || '',
        'Thời gian lưu': c.createdAt
      }));

      const ws = XLSX.utils.json_to_sheet(data);
      const wb = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(wb, ws, 'Danh sách KH');

      ws['!cols'] = [
        { wch: 6 }, { wch: 22 }, { wch: 15 },
        { wch: 28 }, { wch: 28 }, { wch: 18 }
      ];

      const fileName = `Danh_sach_khach_hang_${new Date().toISOString().slice(0,10)}.xlsx`;
      XLSX.writeFile(wb, fileName);
      showToast('Đã xuất file Excel thành công', 'success');
    }

    function showToast(message, type = '') {
      const toast = document.getElementById('toast');
      toast.textContent = message;
      toast.className = 'toast' + (type ? ' ' + type : '');
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2800);
    }

    function escapeHtml(text) {
      if (!text) return '';
      const div = document.createElement('div');
      div.textContent = text;
      return div.innerHTML;
    }
  </script>
</body>
</html>
