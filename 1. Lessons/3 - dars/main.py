
# 3ta jamoa nomini foydalanuvchidan olib list ga saqlash
"""
jamo1 = input("Iltimos jamo 1 ni kiriting: ")
jamo2 = input("Iltimos jamo 2 ni kiriting: ")
jamo3 = input("Iltimos jamo 3 ni kiriting: ")

jamoList = [jamo1,jamo2,jamo3]
jamoList.insert(0, "Hello wolrd")

print(jamoList)
"""
# True  => rost
# False => yolgon
# or  => yoki
# and => va

# Code ni oqish
# Code   => if(10 == 10 and 10 > 15)
# Trans  => agar 10 teng bolsa 10ga va 10 katta bolsa 15 dan bitta shart ni bajar deyilyabdi
print("----------and----------")
print("False and True: ", False and True)
print("True and False: ", True and False)
print("True and True: ",True and True)
print("False and False: ", False and False)
print("\n----------or----------")
print("False or True: ",False or True)
print("True or False: ",True or False)
print("False or False: ", False or False)
print("True or True: ", True or True)


print("\n-----------and || or => operators + boolean-----------")
print("-----------1-----------")
tekshiruv1 = 1 < 2 and "Murod" == "Murod" #False
tekshiruv2 = 1 > 2 and "Murod" == "Murot" #False

print(f'1 < 2 and "Murod" == "Murod": {tekshiruv1}')
print(f'1 > 2 and "Murod" == "Murot": {tekshiruv2}')

# != => bu belgi teng emas degani yani false bolsa true qaytaradi True bolsa false
print("\n-----------2-----------")
tekshiruv3 = 1 != 2 and True and False #False
tekshiruv4 = True or False and False #True

print(f'1 != 2 and True and False: {tekshiruv3}')
print(f'True or False and False: {tekshiruv4}')

print("\n-----------3-----------")
tekshiruv5 = 1 < 2 or "Diyor" == "Diyor" #True
tekshiruv6 = 1 > 2 or "Diyor" == "Dior" #False
print(f'1 < 2 or "Diyor" == "Diyor": {tekshiruv5}')
print(f'1 > 2 or "Diyor" == "Dior": {tekshiruv6}')


print("\n\n-----------Number and Str operator-----------")
print("-----------1-----------")
print(f"10 < 4: ", 10 < 4)
print(f'"Salom" == "Hello": ', "Salom" == "Hello")

print("\n-----------2-----------")
print(f'"Salom" != "Hello": ', "Salom" != "Hello")
print(f'"Salom" > "Salom": ', "Salom" > "Salom")

print("\n-----------3-----------")
# a,b,c,d....
print('"a" > "b": ',"a" > "b") #False
print('"z" > "a": ',"z" > "a") #True

print("\n-----------4-----------")
#Kichkina hariflar katta hariflardan katta boladi va oldinda yuradi 
#P.S: a, b, c, d, ... , z, A, B, C, D, ... , Z
#Harflarni katta kichilkigiga qaraganda
print(f'"a" > "A": ', "a" > "A")#True
print(f'"a" > "B": ', "a" > "B")#True
print(f'"z" > "A": ',"z" > "A")#True
print(f'"Z" > "A": ',"Z" > "A")#True

print("\n-----------5-----------")
# Qande aytilgan bolsa oshande ishloradi ekan 
print('"a" > "bb": ',"a" > "bb")
print('"aa" > "b": ',"aa" > "b")
print('"bb" > "a": ',"bb" > "a")
print('"bb" > "aa": ',"bb" > "aa")

print("\n-----------6-----------")
print('"a" > "bb": ', "a" > "bb")
print('"a" > "bb": ', "a" > "bb")
print('"a" > "bb": ',"a" > "bb")
print('"a" > "bb": ',"a" > "bb")

print("\n\n-----------Ascii table: ord(), chr()-----------")
print("-----------1 ord('a')-----------")
# ascii tablitsasini aniqlash
# ord() orqali qaysi harif yoki sinbolni nechinchi jadvalda turganini korishimiz mumkun
# Yani => ord("a") => 97 tablitsada a turganini etadi
print('ord("a"): ',ord("a")) #97
print('ord("A"): ',ord("A")) #65
print('ord("b"): ',ord("b")) #65
print('ord("B"): ',ord("B")) #65

print("\n-----------2 chr(98)-----------")
# ord() orqali qaysi harif yoki sinbolni jadvaldegi raqamiga qarab izledi po index
# Yani => chr(97) => a Ascii table number ga qarab izledi simbol ni 
print('chr(97): ',chr(97)) #a
print('chr(65): ',chr(65)) #A
print('chr(98): ',chr(98)) #b
print('chr(66): ',chr(66)) #B


print("\n\n-----------Operators, if(), elif(), else------------")
print("\n-----------1 if()-----------")

# if    => agar
# elif  => yokiagar
# else  => yoki

a = 10
b = 10
# if shartiga kirish uchun ikkinchi qatordagi code 4ta probleb tashlanda shu if ga kiradi 
# 4ta 
if(a == b):
	print("if(a == b): ",a == b)

if True:
	#Birinchi if ni ichidegi if ni False qilganim uchun `Hello Second IF`ni chiqarmadi
	if False:
		print("Hello Second IF")
	print("Hello First IF")

print("\n-----------2 else()-----------")
# if()ni shartiga tushmasa else() ishledi
# if() => True
# else => False

yosh = int(input("Yoshingizni kiriting: "))
if(yosh >= 17): # Bu yerda foydalanuvchi 17dan katta son kiritisa qabul qilinadi yani True && 17dan kichik son kiritsa False yani else ni shartini bajaradi
	print("Qabul qilindingiz !!!", yosh >= 17)
else:
	print("Qabul qilinmadingiz !!!", yosh >= 17)


son = int(input("Sonni kiriting: "))
if(son < 0):
	print("Manfiy !", son < 0)
else:
	print("Musbat !", son < 0)


# Ishga kirish dasturi
userName = input("Ismingizni kiriting: ")
age = int(input(f"{userName} yoshingizni kiriting: "))
jobs = input(f"Kasbingizni nma {userName}: ")
if(age >= 18 and 45 <= age or jobs == "Developer" or jobs == "Software" or jobs == "Enginer"):
	print(f"{userName} ishga olindingiz tabrikleman!!")
else:
	print("Uzur biz sizni ishga olomimiz !!!")


print("\n-----------2 elif()-----------")
# elif() => yoki agar
# shart if() ga tushmedigan bolsa elif()qilib yana shart berishimiz mumkun

son = int(input("Son kiriting: "))
if(son == 1):
	print("Bir")
elif(son == 2):
	print("Ikki")
elif(son == 3):
	print("uch")
else:
	print("Qidirilayotgan son topilmadi!!!")


print("\n-----------3 Imtihon javobini tekshirish.-----------")
ball = float(input("Ballni kiriting: "))
if(ball > 100):
	print("GRANT")
elif(ball >= 80 and ball <= 100):
	print(f"Sizning balingiz - {ball}, \nTekshiruv: (ball >= 80 and ball <= 100): \nSizning bahoyingiz: 5")
elif(ball >= 60 and ball < 80):
	print(f"Sizning balingiz - {ball}, \nTekshiruv: (ball >= 60 and ball < 80): \nSizning bahoyingiz: 4")
elif(ball >= 40 and ball < 60):
	print(f"Sizning balingiz - {ball}, \nTekshiruv: (ball >= 40 and ball < 60): \nSizning bahoyingiz: 3")

else:
	print(f"Sizning balingiz - {ball} bolganligi uchun ota olmadiz !!!")

print("\n\n-----------Calculator.-----------")
print("""
Quyidagi Amallardan birini tanlang:
+. Qo`shish
-. Ayrish
*. Ko`paytirish
/. Bo`lish
""")
amal = input("Amalni tanlang: ")
if(amal == "*" or amal =="-" or amal == "+" or amal == "-"):
	son1 = float(input("Son1: "))
	son2 = float(input("Son2: "))
	if amal == "+":
		print(f"{son1} + {son2}: ",son1 + son2)
	elif amal == "-":
		print(f"{son1} - {son2}: ",son1 - son2)
	elif amal == "*":
		print(f"{son1} * {son2}: ",son1 * son2)
	elif amal == "/":
		print(f"{son1} / {son2}: ",son1 / son2)
else:
	print("Notogri amal!")

print("\n\n-----------Log in system.-----------")
db_user = "admin"
db_pass = "1122"
username = input("Username: ")
password = input("Password: ")

if(db_user == username and db_pass != password):
	print("Parol notogri kiritilingan!")
elif(db_user != username and db_pass == password):
	print("Username notogri kiritilindi! ")
elif(db_user != username and db_pass != password):
	print("Username va Password notogri!")
else:
	print("Xush kelibsiz!")
# Tekshiruv operatorini ichiga `pass` kiritilingan bolsa bu otkazib yuborish uchun ishlatiniladi
print("\n\n-----------in, for()-----------")
# in ni birinchi parametiri qidirilayotgan kalit, 2ch parametri qidirilis kerak bolgan sozlar
# yani
print('"a" in "Hello": ', "a" in "Hello")# bu yerda `Hello` ni ichida a bormi deb qidiryabmiz bu `False`
print('"e" in "Hello": ', "e" in "Hello")# bu yerda `Hello` ni ichida e bormi deb qidiryabmiz bu esa `True`
print('"el" in "Hello": ',"el" in "Hello")#True
print('"1" in "1133445566": ',"1" in "1133445566")#True
print('11 in [11,22,33,44,55,66]: ', 11 in [11,22,33,44,55,66])#True
print('22 in [11,22,33,44,55,66]: ', 22 in [11,22,33,44,55,66])#True

# tpl1 = (1)#Tupl ni ichida bitta element boladigan bolsa buni type(int) boladi chunki qavs arifmetik amallar da ishlatilganligi uchun


print("\n-----------for()-----------")
# List da turgan sonlarni ekranga chiqarib berish
lst1 = [11,22,33,44,55,66]
for son in lst1:
	print(son)



# str niham ekranga chiqarib berish
str1 = "Najottalim"
for i in str1:
	print(i, end=" ")


print("\n-----------Tog juft songa ajratish-----------")
#Tog va juft sonni ajratish
lst2 = [1,2,3,4,5,6,7,8]
for i in lst2:
	if(i % 2 == 0):
		print(f"{i} - Juft son!")
	else:
		print(f"{i} - Tog son!")



print("\n-----------List ni yigindisi topish-----------")
#List ni yigindisi topish
lst3 = [11,22,33,44,55,66]
jami = 0 
for i in lst3:
	jami += i
print(f"{lst3}ni yigindisi: {jami}")



# str ni kopaytirish
p = "Python"
for i in p:
	print(i * 3)