n = int(input("Nhập n: "))

dem = 0
tong = 0

if n == 0:
  dem += 1
else:
  while n != 0:
    tmp = n % 10
    tong += tmp
    dem += 1
    n //= 10

print(f"Số chữ số: {dem} - Tổng chữ số: {tong}")