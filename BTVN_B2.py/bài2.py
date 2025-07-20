luong = int(input("Nhập lương của nhân viên:"))
thue = 0
thuNhap = 0
if luong == 15000000:
  thue = luong * 0.3
  thuNhap = luong - thue
elif luong >= 7000000 and luong < 15000000:
  thue = luong * 0.2
  thuNhap = luong - thue
elif luong < 7000000:
  thue = luong * 0.1
  thuNhap = luong - thue
else:
  print("Lương nhân viên không cao qua mức đó!!!")

print("Thuế: " , thue)
print("Thu Nhập: ", thuNhap