# For loop
# for ozgaruvchi in iterable:
#    harakat

# WHILE lOOP
# ozgaruvchi
# while(shart):
#    harakat
#   ortirma
from typing import List, Type


i = 0
while(i < 10):
    print(f"i: {i}")
    i += 1


print("\n--------List ni ichidegi elementlarni ekranga bostirish---------")
lst1 = [11,22,33,44,55,66]
# print(*lst1) # bu usul faqat print() da ishledi
i = 0
while i < len(lst1):
    print(f"I: {i}.Value {lst1[i]}")
    i += 1


print("\n-------- Foydalanuvchi kiritgan sonlarni qoshib beradigan dastur---------")
# break Toxtatish
# continue Otkazib yuborish
jami = 0
while True:
    s = input("Ultimos son kiriting Chiqish(`q`): ")
    if(s == 'q'):
        print(f"Jami: {jami}!")
        break
    s = int(s)
    if(s >= 0 and 100 <= s):
        print("Ilitmos 0dan 100gacha sonnni kiriting: ")
        jami += s
    else:
        jami += s


print("\n\n--------range()---------")
print("range(0,10): ", *range(0,10))
a = range(20)
print("type(range(20)): ", type(a))


print("\n--------range() in list---------")
a = list(range(20))
print("list(range(20)): ",a)


print("\n--------range() in tuple---------")
a = tuple(range(20))
print("tuple(range(20)): ",a)

print("\n--------range() in for()---------")
# range(0, 20, 1) => 1chi parametri boshlanish, 2chi parametri tugatish, 3chi parametri shart nechta nechta oshirish
for i in range(0,20,1):
    print(i)
for i in range(10):
    print(f'"*" * {i}: ', "*" * i )
for i in range(10,0,-1):
    print(f'"*" * {i}: ', "*" * i)

print("\n\n--------BREAK and CONTINUE---------")
# BREAK = bu dasturni toxtatish degani
# Continue = otkazib yuborish

for i in range(10):
    if i == 5:
        continue
    print(i)
for i in range(10):
    print(f"-----------{i}-----------")
    for j in range(1,10):
        # Ozi bu yerda tsikl 9gacha chiqarish kerak no leki|| tsikl 5ga teng boladigan bolsa dasturni toxtayabmiz ub degani BREAK
        if(j == 5):
            break
        elif(j == 4):
        #Bu yerda tsikl 4 bolib keladigan bolsa 4ni otkazvor deb shart qoyabmi
            continue
        print(j)
print("\n\n--------Foydalanuvchini ismini chiqarish---------")
while True:
    name = input("Iltimos ismingizni kiriting(Chiqis: `q`): ")
    if(name == "q"):
        print(f"Yana kutib qolamiz {name} !")
        break
    else:
        print(f"Salom: {name}")


print("\n\n--------While da Contnue + Break ni ishlatish---------")
a = 0
print("-------While to Contnue ---------")
while a < 10:
    if(a == 4):
        print(f"Continue: {a}")
        a += 1
        continue
    print(f"Work: {a}")
    a += 1


print("-------While to Break ---------")
b = 0 
while b < 10:
    if(b == 6):
        print(f"Break: {b}")
        b += 1
        break
    print(f"Work: {b}")
    b += 1

print("-------While in List ---------")
lst3 = [11,22,33,44,55]
jami = 0
index = 0
while index < len(lst1):
    jami += lst1[index] 
    index += 1
print(f"[11,22,33,44,55] => {jami}")

print("\n\n-------LIST COMPREHENSION ---------")

# Bu endi default qiladigan yolimiz
lst1 = [11,22,33,44,55,66,77,88,99]
lst2 = []

for i in lst1:
    if(i % 2 == 0):
        lst2.append(i)

print(f"List1 dagi elementlar: {lst1}")
print(f"List1 dagi elementlarni juft sonlarini list2 ga yozdi: {lst2}")

#LIST COMPREHENSION dan qiladigan bolsek
lst1 = [11,22,33,44,55,66,77,88,99,111,222]
lst2 = [x for x in lst1 if x % 2 == 0] # bir qotor code bilan 2chi listga kochiryabmiz
print(lst2)

lst3 = [11,22,"33","44",55,"66",77,88]
lst4 = [int(i) for i in lst3]
print(f"lsti ni ichda str keladigan bolsa uni int qilib olishimiz kerak: {lst4}")


# List ni ichidegi list larni ikkinchi lstga otkazish

lst7 = [[11,22,33],[44,55,66],[77,88,99]]
lst8 = [j for x in lst7 for j in x ]
print("[[11,22,33],[44,55,66],[77,88,99]]: => ", lst8)




#LOGIN APP
print("\n\n-----------LOGIN APP-----------")
import time
db_user = "admin"
db_pass = '1234'
imkon = 3
while(True):
    if(imkon > 0):
        username = input("Iltimos username ni kiriting(Chiqish: `q`): ")
        password = input("Iltimos password ni kiriting(Chiqish: `q`): ")
        if(username == "q" or password == "q"):
            print("Yana kutib qolamiz!")
            break
        if(db_user == username and db_pass != password):
            print("Password notogri kiritilingan !")
            imkon -= 1 
            print(f"Imkoniyat: {imkon}")
        elif(db_user != username and db_pass == password):
            print("Username notogri kiritilngan !")
            imkon -= 1
            print(f"Imkoniyat: {imkon}")
        elif(db_user != username and db_pass != password):
            print("Username va Passwor notogri kiritilingan!")
            imkon -= 1
            print(f"Imkoniyat: {imkon}")
        else:
            print("Xush kelibsiz !")
    else:
        print("3 - soniyadan kegin qayta urining")
        for i in range(3,0,-1):
            time.sleep(1)
            print(f"{i} - soniya")
        imkon = 3
    
print("\n\n-----------ATM-----------")
print("""
1.Balansi ko`rish
2.Mablag` Qoshish
3.Mablag` yechish

Chiqish uchun: `q`""")

balans = 1000
while True:
    amal = int(input("Amalni kiriting: "))
    if(amal == -1):
        print("Yana kutib qolamiz!")
        break
    elif(amal == 1):
        print(f"Sizning balansingiz: {balans}$")
    elif(amal == 2):
        qoshish = float(input("Summa kiriting: "))
        balans += qoshish
        print(f"Yangi balans: {balans}$")
    elif(amal == 3):
        yechish = float(input("Mablag yechish: "))
        if yechish <= balans:
            balans -= yechish
            print(f"Yangi balans: {balans}$")
        else:
            print("Iltimos balansingizni toldiring!")
            print(f"Sizga -{yechish - balans}$ yetmayabdi")
            continue