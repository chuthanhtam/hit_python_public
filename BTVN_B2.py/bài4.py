xu = int(input("Nhập số xu bạn có: "))

chai = xu // 28
vo = chai

while vo >= 3:
  doi_them = vo // 3
  chai += doi_them
  vo_con_lai = vo % 3
  vo = vo_con_lai + doi_them

print(f"Số chai bia có thể mua được là: {chai} chai")