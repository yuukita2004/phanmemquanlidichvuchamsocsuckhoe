Hệ Thống Quản Lý Dịch Vụ Chăm Sóc Sức Khỏe

Thành viên
Nguyễn Trung Kiên

Mô tả
Ứng dụng quản lý dịch vụ chăm sóc sức khỏe dành cho người dùng và cơ sở y tế, hỗ trợ các chức năng như đăng nhập, đặt lịch khám/dịch vụ, xem danh sách dịch vụ, hủy lịch, và quản lý thông tin cá nhân.

Công nghệ sử dụng

Frontend: PyQt5 + Qt Designer
Backend: Flask (REST API)
Database: MySQL

Cấu trúc thư mục :

├── chay_chuong_trinh.py      # File chạy chính của chương trình

├── co_so_du_lieu.py          # Xử lý kết nối và thao tác database

├── dang_nhap.py              # Giao diện + logic đăng nhập

├── giao_dien_chinh.py        # Giao diện chính của hệ thống

├── quan_tri.py               # Chức năng quản trị

├── tab_quan_tri.py           # Tab quản trị trong giao diện

├── database.db               # Database (có thể dùng SQLite)

├── healthcare.db             # Database hệ thống chăm sóc sức khỏe

