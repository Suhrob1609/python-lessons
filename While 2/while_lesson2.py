# print("Yaqin do'stlaringiz ro'yxatini kiriting: ")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n} - do'stingizni ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash != "ha":
#         break
# print("Do'stlaringiz ro'yxati: ")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshini saqlaymiz. ")
# dostlar = {}
# ishora =True
# while ishora:
#     ism = input("Do'stingizning ismini kiriting: ")
#     yosh = input(f"{ism.title()} ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)

#     javob = input("Yana ma'lumot kiritasizmi? (ha/yo'q? )")
#     if javob == "yo'q":
#         ishora = False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ["nexia", "matiz", "tico", "gentra", "matiz", "mers"]
# while "matiz" in cars:
#     cars.remove("matiz")
# print(cars)

# talabalar = ["Suhrob", "Shohruh", "Farruh", "Zuhra", "Fotima"]
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba} ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)
