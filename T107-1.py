n = int(input("Nhập số tự nhiên n: "))

print("Các ước số của", n, "là:", end=" ")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")