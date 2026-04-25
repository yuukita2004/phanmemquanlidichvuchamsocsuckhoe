import sqlite3

def ket_noi_co_so_du_lieu():
    return sqlite3.connect("database.db")

def tao_cac_bang():
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        # Bảng bệnh nhân
        con_tro.execute("""
            CREATE TABLE IF NOT EXISTS thanh_vien (
                ma_so INTEGER PRIMARY KEY AUTOINCREMENT,
                ma_benh_nhan TEXT UNIQUE,
                ho_ten TEXT,
                ngay_sinh TEXT,
                so_dien_thoai TEXT,
                email TEXT,
                ngay_tham_gia TEXT,
                trang_thai TEXT
            )
        """)
        # Bảng nhân viên
        con_tro.execute("""
            CREATE TABLE IF NOT EXISTS huan_luyen_vien (
                ma_so INTEGER PRIMARY KEY AUTOINCREMENT,
                ho_ten TEXT,
                so_dien_thoai TEXT,
                chuyen_mon TEXT
            )
        """)
        # Bảng Lịch hẹn
        con_tro.execute("""
            CREATE TABLE IF NOT EXISTS lich_tap (
                ma_so INTEGER PRIMARY KEY AUTOINCREMENT,
                ma_hlv TEXT,
                ngay TEXT,  
                gio TEXT,
                dia_diem TEXT,
                mo_ta TEXT
            )
        """)
        # hóa đơn
        con_tro.execute("""
            CREATE TABLE IF NOT EXISTS phi_thanh_vien (
                ma_so INTEGER PRIMARY KEY AUTOINCREMENT,
                ma_thanh_vien TEXT,
                so_tien REAL,
                ngay_thanh_toan TEXT,
                trang_thai TEXT
            )
        """)
        ket_noi.commit()

def them_thanh_vien(ma_thanh_vien, ho_ten, ngay_sinh, so_dien_thoai, email, ngay_tham_gia, trang_thai):
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("""
            INSERT INTO thanh_vien (ma_thanh_vien, ho_ten, ngay_sinh, so_dien_thoai, email, ngay_tham_gia, trang_thai)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (ma_thanh_vien, ho_ten, ngay_sinh, so_dien_thoai, email, ngay_tham_gia, trang_thai))
        ket_noi.commit()

def cap_nhat_thanh_vien(ma_so, ma_thanh_vien, ho_ten, ngay_sinh, so_dien_thoai, email, ngay_tham_gia, trang_thai):
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("""
            UPDATE thanh_vien SET ma_thanh_vien=?, ho_ten=?, ngay_sinh=?, so_dien_thoai=?, email=?, ngay_tham_gia=?, trang_thai=?
            WHERE ma_so=?
        """, (ma_thanh_vien, ho_ten, ngay_sinh, so_dien_thoai, email, ngay_tham_gia, trang_thai, ma_so))
        ket_noi.commit()

def xoa_thanh_vien(ma_so):
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("DELETE FROM thanh_vien WHERE ma_so=?", (ma_so,))
        ket_noi.commit()

def lay_danh_sach_thanh_vien():
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("SELECT * FROM thanh_vien")
        return con_tro.fetchall()

# Hàm cho nhan vien
def them_nhan_vien(ma_hlv, ho_ten, so_dien_thoai, chuyen_mon):
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("""
            INSERT INTO huan_luyen_vien (ho_ten, so_dien_thoai, chuyen_mon)
            VALUES (?, ?, ?)
        """, (ho_ten, so_dien_thoai, chuyen_mon))
        ket_noi.commit()

def cap_nhat_nhan_vien(ma_so, ho_ten, so_dien_thoai, chuyen_mon):
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("""
            UPDATE huan_luyen_vien SET ho_ten=?, so_dien_thoai=?, chuyen_mon=?
            WHERE ma_so=?
        """, (ho_ten, so_dien_thoai, chuyen_mon, ma_so))
        ket_noi.commit()

def xoa_nhan_vien(ma_so):
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("DELETE FROM huan_luyen_vien WHERE ma_so=?", (ma_so,))
        ket_noi.commit()

def lay_danh_sach_nhan_vien():
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("SELECT ma_so, ho_ten, so_dien_thoai, chuyen_mon FROM huan_luyen_vien")
        return con_tro.fetchall()

# Hàm cho Lịch 
def them_lich(ma_lich, ma_hlv, ngay, gio, dia_diem, mo_ta):
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("""
            INSERT INTO lich_tap (ma_hlv, ngay, gio, dia_diem, mo_ta)
            VALUES (?, ?, ?, ?, ?)
        """, (ma_hlv, ngay, gio, dia_diem, mo_ta))
        ket_noi.commit()

def cap_nhat_lich(ma_so, ma_hlv, ngay, gio, dia_diem, mo_ta):
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("""
            UPDATE lich_tap SET ma_hlv=?, ngay=?, gio=?, dia_diem=?, mo_ta=?
            WHERE ma_so=?
        """, (ma_hlv, ngay, gio, dia_diem, mo_ta, ma_so))
        ket_noi.commit()

def xoa_lich(ma_so):
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("DELETE FROM lich_tap WHERE ma_so=?", (ma_so,))
        ket_noi.commit()

def lay_danh_sach_lich():
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("SELECT ma_so, ma_hlv, ngay, gio, dia_diem, mo_ta FROM lich_tap")
        return con_tro.fetchall()

# Hàm cho Phí thành viên
def them_phi_thanh_vien(ma_thanh_vien, so_tien, ngay_thanh_toan, trang_thai):
    with ket_noi_co_so_du_lieu() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO phi_thanh_vien (ma_thanh_vien, so_tien, ngay_thanh_toan, trang_thai)
            VALUES (?, ?, ?, ?)
        """, (ma_thanh_vien, so_tien, ngay_thanh_toan, trang_thai))
        conn.commit()

def cap_nhat_phi_thanh_vien(ma_so, ma_thanh_vien, so_tien, ngay_thanh_toan, trang_thai):
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("""
            UPDATE phi_thanh_vien SET ma_thanh_vien=?, so_tien=?, ngay_thanh_toan=?, trang_thai=?
            WHERE ma_so=?
        """, (ma_thanh_vien, so_tien, ngay_thanh_toan, trang_thai, ma_so))
        ket_noi.commit()

def xoa_phi_thanh_vien(ma_so):
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("DELETE FROM phi_thanh_vien WHERE ma_so=?", (ma_so,))
        ket_noi.commit()

def lay_danh_sach_phi_thanh_vien():
    with ket_noi_co_so_du_lieu() as ket_noi:
        con_tro = ket_noi.cursor()
        con_tro.execute("SELECT ma_so, ma_thanh_vien, so_tien, ngay_thanh_toan, trang_thai FROM phi_thanh_vien")
        return con_tro.fetchall()

# Khởi tạo bảng khi chạy lần đầu
if __name__ == "__main__":
    tao_cac_bang()
