# Problem 1: Foydalanuvchidan olgan 3 ta sonni bir biriga kopaytiring.
# Va natijani ekranga format dan foydalanib chiqaring.
# Split orqali qilganim
numbers = input("Iltimos 3ta sondi kiriting: ")
numbers = numbers.split()
numbers = [int(x) for x in numbers] #Bu yerda x intejer bolganligi uchun numbers larni integer qilib olyabman
jami = 1
for i in numbers:
    jami *= i
print(f"{numbers} sonlar kopaytmasi: ",jami)


# default
n1 = int(input("1chi sonni kiriting: "))
n2 = int(input("2chi sonni kiriting: "))
n3 = int(input("3chi sonni kiriting: "))
print(f"{n1} * {n2} * {n3}: {n1 * n2 * n3}")

# Problem 2: Foydalanuvchidan olgan B'OY va VAZN qiymatlaridan foydalanib tana hajm indeksini toping.
# Formula: kilo / boy(kvadrat)

kilo = int(input("Ilitmos vazningizni kiriting: "))# 65
boy = float(input("Iltimos boyingizni kiritng metrda: ")) #1.88

hajmi = kilo / (boy ** 2)
print(f"Sizning hajmingiz: {hajmi}")


# Problem 3: Bir mashinaning kilometrda necha litr ishlatgani va necha kilometr yol bosganini foydalanuvchidan oling va haydovchining toplamda qancha to'lashi kerak ekanligini chiqaring.
litrBenzin = int(input("Necha litr benzin quidingiz: "))#10
km = int(input("Necha kilometr bosib otingiz: "))#500
benzinNarxi = 5600
benzinNarxi *= litrBenzin
print(f"{km}km ga {litrBenzin}l benzindi narxi: {benzinNarxi}")



# Problem 4: Foydalanuvchilardan ism,familya va tugilgan yilini olgan holda ularni tagma tag yozdiring
name = input("Iltimos ismingizni kiriting: ")
surName = input("Iltimos familiyangizni kiriting: ")
age = input("Iltimos yoshingiz ni kiriting")
print(f"Name: {name}", f"Surname: {surName}", f"Age: {age}", sep=("\n"))


# Problem 5: Foydalanuvchidan ikki son oling va bu sonlarning ornini ozgartiring
son1 = int(input("Iltimos birinchi sonni kiriting: ")) #20
son2 = int(input("Iltimos ikkinchi sonni kiriting: ")) #15

son1 = son1 + son2 #20 = 20 + 15 => bu yerda son1 = 35
son2 = son1 - son2 #15 = 35 - 15 => son2 = 20       old 15
son1 = son1 - son2 #35 = 35 - 15 => son1 = 15       old 20

print(f"birnchi son {son2} ikkinchi {son1}")

# Problem 6: Foydalanuvchidan tik uchburchakning tik bolgan ikki burchagini(a,b) oling va hipotenus
# uzunligini topishga harakat qiling.
# Formula: a^2 + b^2 = c^2
a = int(input("Iltimos birinchi burchakni qiymatini kiriting: "))
b = int(input("Iltimos ikkinchi burchakni qiymatini kiriting: "))
c = (a ** 2) + (b ** 2)
c = c ** 0.5
print(c)
