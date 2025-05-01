# Task1
# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# savol = "Yoqtirgan kitoblaringizni kiriting: "
# savol+="(Barcha kitoblaringizni kiritib bo'lganingizdan so'ng 'stop' deb yozing): "
# while True:
#     kitob = input(savol)
#     if kitob == 'stop':
#         break
# print("Rahmat")

# Task2
# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul.
# Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
# savol = "Yoshingiz nechida? "
# savol += "(dasturni tugallash uchun 'exit' yoki 'quit' deb yozing! )"
# while True:
#     yosh = (input(savol))
#     if yosh == "exit" or yosh == "quit":
#         break
#     yosh = int(yosh)
#     if yosh < 7:
#         print(f"Chipta {yosh} yoshli fuqarolarga 2000 so'm ")

#     if 7 < yosh <= 18:
#         print(f"Chipta {yosh} yoshli fuqarolarga 3000 so'm ")

#     if 18 < yosh <= 65:
#         print(f"Chipta {yosh} yoshli fuqarolarga 10000 so'm ")

#     if yosh > 65:
#         print(f"Chipta {yosh} yoshli fuqarolarga 0 so'm ")

# Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xususiy holatlarda tsikl abadiy qaytarilib qolmoqda.
#  Xatolarni to'g'rilay olasizmi?
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='Exit':
#         break
#     elif float(qiymat)<0:
#         continue

#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
