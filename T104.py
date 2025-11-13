so_dien = int(input("Nhập số điện tiêu thụ trong tháng (kWh): "))

if so_dien <= 50:
    tien_dien = so_dien * 1678
elif so_dien <= 100:
    tien_dien = 50 * 1678 + (so_dien - 50) * 1734
else:
    tien_dien = 50 * 1678 + 50 * 1734 + (so_dien - 100) * 2014

print("Số tiền điện phải trả là:", tien_dien, "đồng")