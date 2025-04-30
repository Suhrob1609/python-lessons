# Task1
# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }
# mashhurlar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in mashhurlar:
#     ism = shaxs["ism"]
#     tyil = shaxs["tyil"]
#     vyil = shaxs["vyil"]
#     tjoy = shaxs["tjoy"]
#     print(f"{ism} {tyil}-yilda {tjoy}da tug'ilgan, {vyil-tyil} yil umr ko'rgan")

# Task2
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }
# buxoriy["asar"] = "Al-jome Al-sahih"
# qodiriy["asar"] = "O'tgan kunlar"
# vohidov["asar"] = "Nido dostoni"
# navoiy["asar"] = "Hamsa"
# mashhurlar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in mashhurlar:
#     ism = shaxs["ism"]
#     asar = shaxs["asar"]
#     print(f"{ism} ning mashhur asari: {asar}")

# Task3
# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang.
# Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'atga saqlang.
# Natijani konsolga chiqaring.
# kinolar = {"Shohruh":["Kara Sevda", "Omonat", "Hukmdor"],
#         "Farruh":["Janob hech kim", "Ona", "Vatan"],
#         "Suhrob":["Volida", "USA tarixi", "Amir Temur"]}
# for ism, kino in kinolar.items():
#     print(f"{ism} ning yoqtirgan kinolari: ")
#     for fkino in kino:
#         print(fkino)

# Task4
# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
# Har bir davlat haqida ma'lumotni konsolga chiqaring.
# davlatlar = {"Uzbekistan": {"poytaxti": "Toshkent", "aholisi": "38mln", "prezidenti": "Sh.Mirziyoyev"},
#              "USA": {"poytaxti": "Washington", "aholisi": "347 mln", "prezidenti": "Donald J. Trump"},
#              "Misr": {"poytaxti": "Cairo", "aholisi": "114 mln", "prezidenti": "Abdel Fattah el-Sisi"}}
# for davlat, malumot in davlatlar.items():
#     print(f"{davlat} haqida ma'lumot: ")
#     for ism, good in malumot.items():
#         print(f"{ism}: {good}")

# Task5
# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering.
# Agar davlat sizning lug'atingizda mavjud bo'lmasa,"Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
davlatlar = {"Uzbekistan": {"poytaxti": "Toshkent", "aholisi": "38mln", "prezidenti": "Sh.Mirziyoyev"},
             "USA": {"poytaxti": "Washington", "aholisi": "347 mln", "prezidenti": "Donald J. Trump"},
             "Misr": {"poytaxti": "Cairo", "aholisi": "114 mln", "prezidenti": "Abdel Fattah el-Sisi"}}
davlat = input("Davlatni kiriting : ")
if davlat in davlatlar.keys():
    for x, m in davlatlar[davlat].items():
        print(f"{x} : {m}")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")
