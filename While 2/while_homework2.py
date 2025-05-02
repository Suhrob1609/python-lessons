# Task1
# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# print("Buyurtma qabul qiluvchi dastur yozing! ")
# buyurtmalar = []
# ishora = True
# while ishora:
#     buyurtma = input("Mahsulot nomini kiriting ")
#     buyurtmalar.append(buyurtma)
#     javob = input("Yana mahsulot kiritasizmi? (ha/yo'q)? ")
#     if javob == "yo'q":
#         ishora = False
# print(buyurtmalar)

# Task2
# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# mahsulotlar = {}
# ishora = True
# while ishora:
#     mahsulot = input("Mahsulot nomini kiriting: ")
#     narx = input(f"{mahsulot} ning narxi: ")
#     javob = input("Yana mahsulot kiritasizmi? (ha/yo'q? )")
#     mahsulotlar[mahsulot] = int(narx)
#     if javob == "yo'q":
#         ishora = False

# print(mahsulotlar)

# Task3
# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin).
# Agar mahsuot e-bozorda mavjud bo'lsa mahsulot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
# buyurtma = ["un", "non", "shakar", "olma", "anor", "nok", "sut", "kefir"]
# mahsulotlar = {"olma": 5000,
#                "un": 10000,
#                "anjir": 14000,
#                "yog'": 50000,
#                "go'sht": 100000}
# for mahsulot in buyurtma:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot} ning narxi {mahsulotlar[mahsulot]}")
#     else:
#         print(f"Bizda {mahsulot} yo'q")
