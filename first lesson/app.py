# Foydalanuvchidan biror butun son kiritishni so'rang.Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
number = int(input("Enter the number: "))
for n in range(2, 11):
    if number % n == 0:
        print(f"{number} {n} ga qoldiqsiz bo'linadi ")
