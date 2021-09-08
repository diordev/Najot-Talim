# Problem 1: Foydalanuvchidan olgan boy va vazn qiymatlariga kora tana indeksini aniqlang 
# va shu qoidalarga kora ekranga shu yozuvlarni yozdiring
"""
vazn = float(input("Iltimos vazningizni kiriting: "))
height = float(input("Iltimos boyingizni razmerini kiriting (1.8): "))

tanaIndex = vazn  / (height ** 2)
print(f"Sizning tana Indexingiz: {tanaIndex}")
"""






# Problem 2: Foydalanuvchidan 3 dona son oling va eng kattasini ekranga chiqaring
"""
s1 = float(input("Iltimos birinchi sonni kiriting: "))
s2 = float(input("Iltimos ikkinchi sonni kiriting: "))
s3 = float(input("Iltimos uchinchi sonni kiriting: "))

if s1 > s2 and s1 > s3:
    print(s1)
elif s2 > s1 and s2 > s3:
    print(s2)
elif s3 > s1 and s3 > s2:
    print(s3)
"""



# Problem 3: Foydalanuvchi kiritgan 1-,2- va final imtixon ballariga qara 5 lik sistemada bahosini belgilang:
"""
1 - Imtixon balli : 30%
2 - Imtixon balli : 30%
Final - Imtixon balli : 40%
Yuqorida Imtixon Ballari 100% da qanchadan ulush olishi keltirilgan. Pastagi baholash tizimi:

Toplam Ball >= 85 --------> 5
Toplam Ball >= 80 --------> 4.5
Toplam Ball >= 75 --------> 4
Toplam Ball >= 70 --------> 3.5
Toplam Ball >= 65 --------> 3
Toplam Ball >= 60 --------> 2.5
Toplam Ball >= 55 --------> 2
Toplam Ball < 55 --------> Yiqildingiz !!!
"""
"""
birinchiImtixonBall = float(input("1 - Imtixon ballini kiriting: (max: 30): "))
ikkinxhiImtixonBall = float(input("2 - Imtixon ballini kiriting:(max: 30) "))
finalImtixonBall = float(input("Iltimos final ball ni kiriting: (max: 40)"))

UmumiyBall = birinchiImtixonBall + ikkinxhiImtixonBall + finalImtixonBall

if UmumiyBall >= 85:
    print(f"Sizni imtixon balingiz  {UmumiyBall} bolganligi uchun,\nSizning bahoyingiz: 5")
elif UmumiyBall >= 80 and 85 < UmumiyBall:
    print(f"Sizni imtixon balingiz  {UmumiyBall} bolganligi uchun,\nSizning bahoyingiz: 4.5")
elif UmumiyBall >= 75 and 80 < UmumiyBall:
    print(f"Sizni imtixon balingiz  {UmumiyBall} bolganligi uchun,\nSizning bahoyingiz: 4")
elif UmumiyBall >= 70 and 75 < UmumiyBall:
    print(f"Sizni imtixon balingiz  {UmumiyBall} bolganligi uchun,\nSizning bahoyingiz: 3.5")
elif UmumiyBall >= 65 and 70 < UmumiyBall:
    print(f"Sizni imtixon balingiz  {UmumiyBall} bolganligi uchun,\nSizning bahoyingiz: 3")
elif UmumiyBall >= 60 and 65 < UmumiyBall:
    print(f"Sizni imtixon balingiz  {UmumiyBall} bolganligi uchun,\nSizning bahoyingiz: 2.5")
elif UmumiyBall >= 55 and 60 < UmumiyBall:
    print(f"Sizni imtixon balingiz  {UmumiyBall} bolganligi uchun,\nSizning bahoyingiz: 2")
else:
    print(f"Sizni imtixon balingiz  {UmumiyBall} bolganligi uchun,\nSiz Yiqildingiz !!!")
"""


# Problem 4: Endi geometrik shakl hisoblab chiqamiz. 
# Birinchidan foydalanuvchidan uchburchak yoki to'rtburchak turini topishni xohlayotganingizni so'rang.
print("""Quidagi shakillardan birini tanleng:
1) T`ort burchak
2) Uchburchak """)
burchak = int(input("Shakillarni birini tanleng: ")) 
if(burchak == 1):
        a = int(input("Iltimos birinchi burchakni uzunligini kriitng: "))
        b = int(input("Iltimos ikkinchi burchakni uzunligini kriitng: "))
        c = int(input("Iltimos uchinchi burchakni uzunligini kriitng: "))
        d = int(input("Iltimos tortinchi burchakni uzunligini kriitng: "))
        if(a == b == c == d):
            print("Kvadrat")
        elif(a == b != c == d):
            print("Toʻgʻri 4 burchak")
        else:
            print("Oddiy t`ort burchak")
elif(burchak == 2):
        a = int(input("Iltimos birinchi burchakni uzunligini kriitng: "))
        b = int(input("Iltimos ikkinchi burchakni uzunligini kriitng: "))
        c = int(input("Iltimos uchinchi burchakni uzunligini kriitng: "))
        if(a == b == c):
            print("Uchburchak")
        elif(a == b != c):
            print("Toʻgʻri 3 burchak")
        else:
            print("Oddiy Uchburchak")
else:
    print("Uzur bunday amal mavjud emas!")