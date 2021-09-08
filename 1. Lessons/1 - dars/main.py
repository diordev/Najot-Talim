#import plugins or library
from datetime import date

"""Data types in Python"""
# Primitive types: Int, Float, String, Boolean
print("\n-------Variables and Concatenation-------  ")
myName = "Diyorbek"
currentYear = date.today().year
myAge = currentYear - 2005
myHeight = 188.2
isMale = True

print(f"My name is: {myName}, \nMy age: {myAge}, \nMy height: {myHeight}, \nisMale: {isMale}")

# Primitive types see
print("\n-------Types variable-------  ")
print(f"Type is variable age: {type(myAge)}")
print(f"Type is variable myHeight: {type(myHeight)}")
print(f"Type is variable myName: {type(myName)}")
print(f"Type is variable isMale: {type(isMale)}")

# Comments types in Python
"""
Multi-line
"""

# One-line

# qisqacha malumot


#3.Arithmetic examples

#plus
print("\n-------Arithmetic examples-------  ")
n1 = 10
f1 = 10.0
res1 = n1 + f1
print(f"{n1} add to {f1} result: ", res1 , f"\nType result: {type(res1)}", )

#Minus
n2 = 10
f2 = 10.0
res2 = n2 - f2
print(f"\n{n2} minus to {f2} result: ", res2 , f"\nType result: {type(res2)}", )

#Multiplication1
n3 = 10
f3 = 10.0
res3 = n3 * f3
print(f"\n{n3} multiplication to {f3} result: ", res3 , f"\nType result: {type(res3)}", )

#Divided
n4 = 10
f4 = 10.0
res4 = n4 - f4
print(f"\n{n4} Divided to {f4} result: ", res4 , f"\nType result: {type(res4)}", )

# Float qiymatini tashavorish onlik sanoq systemasida olmasdan butun sonni ozini chiqarib berish
n5 = 100
f5 = 3
res5 = n5 // f5
print(f"Float ni int ga ogirish: {f5}")

# Kvadrat
n6 = 10
f6 = 3
res6 = n6 ** f5
print(f"{n6}ni {f6}chi darajasi: {res6}")

# Ildiz
i1 = 10
i2 = 0.5
res1 = i1 ** i2
print(f"{i1}ni ildizi: {res1}")
# ozgaruvchiga qoshimcha qoshish
son1 = 10
son1 += 10
print("son1 += 10:", son1)

# ozgaruvchiga qoshimcha ayrish
son1 = 10
son1 -= 10
print("son1 -= 10:", son1)

# ozgaruvchiga qoshimcha kopaytirish
son1 = 10
son1 *= 10
print("son1 *= 10:", son1)

# ozgaruvchiga qoshimcha bolish
son1 = 10
son1 /= 10
print("son1 /= 10:", son1)

# ozgaruvchiga qoshimcha floatni yoq qilish bolish
son1 = 10
son1 //= 10
print("son1 //= 10:", son1)






#Others
print("\n-------Oters-------  ")

#len()
str1 = "Dioyrbek"
print(f"str1 ni matn uzunligi: {len(str1)}ga teng")

# [start:finish:jumping]
# [boshla:tugat:sakra]
# [inclusiv:exlusiv:stop]
userFullName = "Rustamjonov Diyorbek"
print(f"1) {userFullName} - ni birinchi harfi: {userFullName[0]}")
print(f"2) {userFullName} - ni oxirgi harfi: {userFullName[-1]}") #-0 -> bollmidi hato boladi
print(f"3) {userFullName} - ni harf chiqarishni 0dan boshlab 10gacha 2ta iktada oshir: {userFullName[0:10:2]}")

# Str ni ichidagi malutmoni ozgartirish
# fc = "Tuventus"
# fc[0] = "Y" #Str ni ichidagani malutmoni ozgartirib bolmaydi
# print(fc)

#Str ni *3 ga kopaytirish
str1 = "Python"
str1 *= 3
print(f"str *= 3: {str1}")


#int ni type ni ozgartirib str qilib str ga qoshib koramiz
num1 = 3
str2  = "Python "
str2 += str(num1)
print(f"str2 += str(num1): {str2}")



# strdagi sonni ni float qilib int son qoshib koramiz
str1 = "455.101"
str1 = float(str1) + 33;
print(str1)



# Flowgorithm in Python)))


# Faktorial ni topish formulasi
"""
print("\n-------Faktorial formulasi-------  ")

son = input("Faktorial ni bilmoqchi bolgan soningizni kiriting: ")
son = int(son) #input ga kiritgan son baribir string bolib tushadi oshanga buni biz int() qilib olishimiz kerak shuning uchun str ni int ga conver qilib olyabman
factorial = 1 #bu yerda faktorial ni boshlangiz son beryabmiz yani 1ga tenglayabmiz boshlab hisoblashini

if son <= 0: #Tekshiruv qoyabmiz kiritilingan sonimiz 0 dan kichkina bolsa error chiqar devomiz
   print("Iltimos 0 dan katta sonni kiriting!")
else:
   for i in range(1, son + 1): # range(); 1chi parametriga boshlanish oqi, 2chi parametriga tugatish oqi
       factorial = factorial * i

   print(f"{son}ni faktoriali: ", factorial)
"""







#Tog va Juft song ga ajratish
"""
print("\n-------Tog Juft son ga ajratish-------  ")
startSon = input("Birinchi sonni kiriting(0dan katta bolish kerak): ")
stopSon = input("Ikkinchi sonni kiriting(birinchi kiritgan sonizdan katta bolishi kerak) : ")

startSon = int(startSon)
stopSon = int(stopSon)

if 0 >= startSon:
    print("Iltimos 0 dan katta son ni kiritin")
elif startSon >= stopSon:
    print("Iltimos 1chi kiritingan sonizdan kattasini kiriting")
else:
    for i in range(startSon, stopSon, 1):
        if i % 2 == 1:
            print(f"{i} - tog son;")
        else:
            print(f"{i} - juft son;")
"""








# Uchburchakni yuzasini aniqlaydigan formula
# S = (a / 2)  * h
"""
print("\n-------Uchburchakni yuzasini aniqlaydigan formula-------  ")
def hajmHisobla(balandlik, asos): #def bu function ekan, def dan kegin function ni nomi kiritiladi kegin uni parametrlari kiritiladi
    result = (balandlik / asos) * 2
    result = int(result)
    return print(f"Hajmi: {result}")
hajmHisobla(10,10)
"""


# Yakuniy uchun 60% va oraliq uchun 40% da hisoblang
"""
print("\n-------Yakuniy uchun 60% va oraliq uchun 40% da hisoblang-------  ")
yakuniy = input("Yakuniyni kiriting: ")
oraliq = input("Oraliqni kiriting: ")
def bahoHisoblaFunksiya(yakuniy, oraliq):
    natija = (int(yakuniy) * 0.6) + (int(oraliq) * 0.4)
    if(natija >= 90):
        b = 5
    elif(natija >= 80):
        b = 4
    elif(natija >= 70):
        b = 3
    elif(natija >= 60):
        b = 2
    else:
        b = -1

    return b;
baho = bahoHisoblaFunksiya(yakuniy, oraliq)

print(f"Sizning bahoyingiz: {baho}")
"""
