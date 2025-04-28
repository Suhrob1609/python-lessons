# Homework
# Task1
# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida
# 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo).
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :
# Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
# otam = {"ism":"Alimov Shuhrat",
#         "t_yil":1971,
#         "t_joyi":"Qashqadaryo viloyati"}
# print(f"{otam['ism']}, {otam['t_yil']} -yilda, {otam['t_joyi']}da tug'ilganlar")

# Task2
# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
# Kamida uch kishining sevimli taomini konsolga chiqaring:
# Alining sevimli taomi osh
# favourite_meal = {"Shuhrat":"manti",
#                   "Rohila":"chuchvara",
#                   "Shohruh":"shashlik",
#                   "Farruh":"osh",
#                   "Zuhra":"Galpyuse"}
# meal = favourite_meal["Farruh"]
# print(f"Farruhning sevimli taomi {meal}")

# Task3
# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
# dictionary = {"integer":"butun son",
#               "float":"o'nlik son",
#               "string":"matn",
#               "if":"agar shart operatori",
#               "else":"aks holda",
#               "print":"chop etish",
#               "del":"o'chirish",
#               "append":"ro'xatning oxiriga element qo'shish",
#               "clear":"tozalash",
#               "title":"barcha elementlarning 1-harfini katta qilish"}
# print( dictionary)

# Task4
# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
# dictionary = {"integer": "butun son",
#               "float": "o'nlik son",
#               "string": "matn",
#               "if": "agar shart operatori",
#               "else": "aks holda",
#               "print": "chop etish",
#               "del": "o'chirish",
#               "append": "ro'xatning oxiriga element qo'shish",
#               "clear": "tozalash",
#               "title": "barcha elementlarning 1-harfini katta qilish"}
# word = input("Birorta so'z kiriting: ")
# if word in dictionary:
#     print(dictionary[word])
# else:
#     print("Bunday so'z mavjud emas")
# 2nd version
# print(dictionary.get(word, "Bunday so'z mavjud emas"))
