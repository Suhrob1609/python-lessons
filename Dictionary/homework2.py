# Task1
# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
# dictionary = {"Boolen":"Mantiqiy qiymat",
#               "Integer":"butun son",
#               "Float":"o'nlik son",
#               "For":"Biror amalni qayta-qayta bajarish sikli ",
#               "If":"shartlarni tekshirish operatori",
#               "Integer":"Butun son",
#               "Print":"Chop etish funksiyasi",
#               "Tuple":"O'zgarmas ro'yxat",
#               "Else":"Aks holda",
#               "Key":"Kalit so'z"}
# for key, value in sorted(dictionary.items()):
#     print(f"{key.title()} - {value}")

# Task2
# Davlatlar va ularning poytaxtlari lug'atini tuzing.
# Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
# davlatlar = {"Uzbekistan": "Toshkent",
#              "Amerika": "Washington",
#              "Rossiya": "Moskva",
#              "Tojikiston": "Dushanbe",
#              "Italiya": "Rim",
#              "Singapur": "Singapur",
#              "Qirg'iziston": "Bishkek"}
# print("Davlatlar ro'yxati: ")
# for key in sorted(davlatlar.keys()):
#     print(key)
# print("Kiritilgan davlatlar poytaxti: ")
# for value in sorted(davlatlar.values()):
#     print(value)

# Task3
# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
# davlatlar = {"Uzbekistan": "Toshkent",
#              "Amerika": "Washington",
#              "Rossiya": "Moskva",
#              "Tojikiston": "Dushanbe",
#              "Italiya": "Rim",
#              "Singapur": "Singapur",
#              "Qirg'iziston": "Bishkek"}
# davlat = input("Istalgan davlatning nomini kiriting: ")
# if davlat in davlatlar.keys():
#     print(f"{davlat} davlatning poytaxti: {davlatlar[davlat]}")

# else:
#     print("Bizda bunday ma'lumot yo'q ")

# Task4
# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang.
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating,
# aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

# restoran = {"manti": 20000,
#             "lag'mon": 25000,
#             "shashlik": 12000,
#             "somsa": 11000,
#             "chuchvara": 30000,
#             "shurva": 35000,
#             "sushi": 50000,
#             "tushonka": 40000,
#             "mastava": 35000,
#             "osh": 55000
#             }
# print("3 ta taom buyurtma bering: ")
# buyurtmalar = []
# for ovqat in range(3):
#     buyurtmalar.append(input(f"{ovqat+1} - ovqatni kiriting:"))
# for buyurtma in buyurtmalar:
#     if buyurtma in restoran:
#         print(f"{buyurtma} ning narxi: {restoran[buyurtma]}")
#     else:
#         print(f"Bizda {buyurtma}  yo'q ")
