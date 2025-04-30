# car_0 = {"model": "gentra",
#          "rangi": "oq",
#          "yil": 2018,
#          "narx": 13000,
#          "km": 50000,
#          "karobka": "mexanika"}
# car_1 = {"model": "lacette",
#          "rangi": "qora",
#          "yil": 2024,
#          "narx": 17000,
#          "km": 5000,
#          "karobka": "avtomat"}
# car_2 = {"model": "matiz",
#          "rangi": "oq",
#          "yil": 2015,
#          "narx": 6000,
#          "km": 150000,
#          "karobka": "mexanika"}
# car = car_0
# print(f"{car["model"].title()},"
#       f"{car["rangi"]} rang, "
#       f"{car["yil"]} - yil,"
#       f"{car["narx"]}$")
# car = car_1
# print(f"{car["model"].title()},"
#       f"{car["rangi"]} rang, "
#       f"{car["yil"]} - yil,"
#       f"{car["narx"]}$")
# car = car_2
# print(f"{car["model"].title()},"
#       f"{car["rangi"]} rang, "
#       f"{car["yil"]} - yil,"
#       f"{car["narx"]}$")
# cars = [car_0, car_1, car_2]
# for car in cars:
#     print(f"{car["model"].title()},"
#       f"{car["rangi"]} rang, "
#       f"{car["yil"]} - yil,"
#       f"{car["narx"]}$")

# malibus = []
# for n in range(10):
#     new_car = {
#         "model":"malibu",
#         "rang":"None",
#         "yil":2020,
#         "narx":"None",
#         "km":0,
#         "karobka":"avtomat"
#     }
# malibus.append(new_car)
# for malibu in malibus:
#     if malibu["karobka"] == "avtomat":
#         malibu["narx"] = 40000
#     else:
#         malibu["narx"] = 35000
# for malibu in malibus:
#     print(malibu)

# Lug'at ichida ro'yxat
# Ali quyidagi tillarni biladi.
# php
# sql
# dasturchilar = {"Suhrob":["C++", "Java", "Python"],
#                 "Shohruh":["C++", "Java"],
#                 "Farruh":["Jango", "C#"],
#                 "Ali":["php", "sql"]}
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi. ")
#     for til in tillar:
#         print(til.upper())

# Lug'atlar ichida lug'atlar
hamkasblar = {"ali": {"familiya": "Valiyev",
                      "tyil": 2000,
                      "ma'lumot": "oliy",
                      "tillar": ["python", "php"]},
              "vali": {"familiya": "Ganiyev",
                       "tyil": 1990,
                       "ma'lumot": "oliy",
                       "tillar": ["python", "sql"]},
              "jack": {"familiya": "Bezis",
                       "tyil": 1994,
                       "ma'lumot": "oliy",
                       "tillar": ["java", "php"]},
              }
for ism, info in hamkasblar.items():
    print(
        f"\n{ism.title()} {info["familiya"].title()}, {info["tyil"]} - yilda tug'ilgan. \n")
