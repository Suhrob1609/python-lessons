# def salom_ber():
#     """ Salom beruvchi funksiya """
#     print("Assalomu alaykum! ")
# salom_ber()

# def salom_ber(ism):
#     """ Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya """
#     print(f"Assalomu alaykum, hurmatli {ism.title()}! ")
# salom_ber("Suhrob")
# salom_ber("Shohruh")
# print(salom_ber.__doc__)

# def toliq_ism(ism, familiya):
#     """Foydalanuvchining to'liq ism familiyasini chiqaruvchi funksiya """
#     print(f"Foydalanuvchi ismi: {ism.title()}")
#     print(f"Foydalanuvchi familiyasi: {familiya.title()}")
# toliq_ism("Suhrob","Oqmirzayev")

def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblovchi funksiya"""
    print(f"Foydalanuvchining ismi: {ism.title()}")
    print(f"{ism.title()} {2025 - tugilgan_yil} yoshda")
yosh_hisobla("Suhrob", 2000)