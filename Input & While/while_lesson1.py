# input()
# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr? ")
# height = float(height)

# while()
# son = 1
# while son <= 5:
#     print(son, end=" ")
#     son += 1
# print("Dastur tugadi")

# while() and input()
# print("Kiritilgan sonnning kvadratini qaytaruvchi dastur ")
# savol = "Istalgan sonni kiriting "
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = " "
# while qiymat != "exit":
#     qiymat = input(savol)
#     if qiymat != "exit":
#         print(float(qiymat)**2)
# print("Dastur tugadi! ")

# ishora
# print("Kiritilgan sonning kvadrtini hisoblovchi dastur. ")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# a = True

# while a:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         a = False
#     else:
#         print(float(qiymat) ** 2)
# print("Dastur to'xtatildi! ")

# break while
# print("Kiritilgan sonning kvadratini hisoblovchi dastur: ")
# savol = "Istalgan sonni kiriting. "
# savol += "(dasturni to'xttish uchun 'exit' deb yozing): "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print("Dastur to'xtatildi! ")

# break for
# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         continue
#     else:
#         print(f"{son} ning kvadrati: {son ** 2}")
# print("Dastur to'xtatildi! ")

# continue while
# son = 0
# while son < 11:
#     son+=1
#     if son % 2 == 0:
#         continue
#     else:
#         print(son)

# infinite loop
# son = 1
# while son > 0:
#     son+=1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)
