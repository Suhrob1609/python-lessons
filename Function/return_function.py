# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism yasovchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# talaba1 = toliq_ism_yasa(familiya="Oqmirzayev", ism="Suhrob")
# talaba2 = toliq_ism_yasa(familiya="Alimov", ism="Shohruh")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def toliq_ism_yasa(ism, familiya, otasining_ismi = ""):
#     """To'liq ism qaytaruvhi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa("Suhrob", "Oqmirzayev", "Shuhratovich ")
# talaba2 = toliq_ism_yasa("Alimov", "Shohruh")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def avto_info(kompaniya, model, rangi, karobka, yili, narhi = None):
#     avto = {"kompaniya": kompaniya,
#             "model": model,
#             "rangi": rangi,
#             "karobka": karobka,
#             "yili": yili,
#             "narh":narhi}
#     return avto
# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2018)
# avto2 = avto_info("GM", "Gentra", "Qora", "Mexanika", 2024, 15000)
# avtolar = [avto1, avto2]
# print("Onlayn bozordagi mavjud avtomobillar: ")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto["narh"]
#     else:
#         narh = "Noma'lum"
#     print(f"{avto["rangi"]} {avto["model"]}. Narhi: {narh}")

# def oraliq(min, max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min+=1
#     return sonlar
# print(oraliq(0,10))
# print(oraliq(10,20))

def oraliq(min, max, qadam=None):
    sonlar = []
    while min < max:
        if qadam:
            sonlar.append(min)
            min = min + qadam
        else:
            sonlar.append(min)
            min += 1
    return sonlar


print(oraliq(0, 10, 2))
print(oraliq(10, 20))
