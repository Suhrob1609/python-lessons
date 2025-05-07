# Task1
# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def tug_yil(ism, yoshi):
#     """Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblovchi funksiya """
#     print(f"Foydalanuvchi ismi: {ism.title()}")
#     print(f"Foydalanuvchi yoshi: {yoshi}")
#     print(f"{ism.title()} {2025-yoshi} - yilda tug'ilgan. ")
# tug_yil("Suhrob", 25)

# Task2
# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def daraja(son):
#     """Kiritilgan sonning kvadratini va kubini hisoblovchi funksiya"""
#     print(f"Kiritilgan son: {son}")
#     print(f"{son} ning kvadrati: {son ** 2} ga teng")
#     print(f"{son} ning kubi: {son ** 3} ga teng")

# daraja(3)

# Task3
# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def juft_toq(son):
#     """Sonning juft yoki toqligini chiqaruvchi funksiya"""
#     print(f"Kiritilgan son: {son}")
#     if son % 2 == 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")
# juft_toq(3)

# Task4
# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def kattasi(son1,son2):
#     """Kiritilgan 2 ta sonning kattasini konsolga chiqaruvchi funksiya """
#     if son1 > son2:
#         print(f"{son1} > {son2}")
#     elif son1 < son2:
#         print(f"{son2} > {son1}")
#     else:
#         print(f"{son2} = {son1}")
# kattasi(2,2)

# Task5
# Foydalanuvchidan x va y sonlarini olib, x ni y darajasini konsolga chiqaruvchi funksiya yozing.
# def darajalar(x,y):
#     """x ning y-darajasini chiqaruvchi funksiya"""
#     print(f"{x} ning {y}- darajasi: {x**y}")
# darajalar(2,5)

# Task6
# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def darajalar(x, y=2):
#     """x ning y-darajasini chiqaruvchi funksiya"""
#     print(f"{x} ning {y}- darajasi: {x**y}")
# darajalar(10)

# Task7
# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing.
# Natijalarni konsolga chiqaring.
# def bolinish_alomatlari(son):
#     """Kiritilgan sonning 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bolinishini tekshiruvchi funksiya"""
#     for n in range(2, 11):
#         if son % n == 0:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi ")

# bolinish_alomatlari(20)
