while True:
    s_input = input("Nhập số giây: ")
    try:
        s = int(s_input)
        if s < 0:
            print("Số giây thì âm kiểu j :/")
            continue
        break
    except ValueError:
        print("Nhập số :/")

sg = s
d = s // 86400
s = s % 86400

h = s // 3600
s = s % 3600

m = s // 60
sc = s % 60

print(f"{sg} giây = {d} ngày {h} giờ {m} phút {sc} giây")