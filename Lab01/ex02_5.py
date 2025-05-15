gio_lam = float(input("Nhập tổng số giờ làm trong tuần: "))
luong_gio = float(input("Nhập lương thực nhận mỗi giờ (đồng): "))

gio_tieu_chuan = 44
he_so_tang_ca = 1.5

if gio_lam <= gio_tieu_chuan:
    tong_luong = gio_lam * luong_gio
else:
    gio_tang_ca = gio_lam - gio_tieu_chuan
    tong_luong = gio_tieu_chuan * luong_gio + gio_tang_ca * luong_gio * he_so_tang_ca

print(f"Tổng lương tuần này là: {tong_luong:.2f} đồng")
