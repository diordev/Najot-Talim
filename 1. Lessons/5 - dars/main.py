#Method lar 
#Classlarning ichida yoziladigan functionlar
#Classning methodi deyiladi

lst1 = []
# append bu method function
# lst1.append(10)

tpl1 = (1,2,3)
# yani buyerdaham index() method vazifasini bajaryabdi
print(tpl1.index(2))

# Function -> Build-In && User-defined
#Built-In => Bu default function lar yani Python tomonidan beriladigan funksiyalar
# Masalan:
# input()
# range()
# int()
# str()
# float()
# type()
# print()



# User-defined
# def bilan function ni chaqirib olamiz 
# def funksiyani_nomi(argumentlari):
    # return argumentlari + 5
def qosh():
    print(10 + 10)
qosh()
print("\n\n-----------sayHello()-----------")
def sayHello(ism):
    print(f"Salom: {ism}")
ism = input("Ismingizni kiriting: ")
sayHello(ism)


print("\n\n-----------Faktorial ni topish function-----------")

def factorial(son):
    f = 1
    if(son == 0 or son == 1):
        print("Son faktoriali: 1")
    else:
        while son >= 1:
            f *= son
            son -= 1
        print(f"Faktoriali: {f}")
faktoria = int(input("Iltimos faktorialni kiriting: "))
factorial(faktoria)

print("\n\n-----------Function return qaytarishi-----------")
def qosh(a,b):
    return a + b
a = qosh(10,20)
print(f"qosh(10,20): {a}")

print("\n\n-----------Function ni ichidagi funtion-----------")
def a(a):
    return a + 5
def b(b):
    return b + 5
print("a(b(5)): ", a(b(5)))#15

def a(a):
    return a + 1
def b(b):
    return b + 2
def c(c):
    return c + 3
print("a(b(c(19))) + a(b(c(15))): ",a(b(c(19))) + a(b(c(15))))

# Function lardagi paramet turalari
# Required, Default, Optional
print("\n\n-----------Function lardagi paramet turalari-----------")
print("-----------Required-----------")
def qosh(a,b):
    return a + b
print("def qosh(a,b): => ", qosh(10,20))



print("\n-----------Default-----------")
# Default function da parametrga qiymat berib qoyamiz yani 
def bol(a = 10, b = 5):
    return a // b
print("Foydalanuvchi function ni parametriga hech narsa bermasi u dafault qiymatni oladi: ", bol())
print("Foydalanubchi function ni parametrini bersa u default ni tashavorib parametrni oladi: ", bol(100,5))



print("\n-----------Optional-----------")
# Optional oziga beskonechniy qiymat ola oladi oziga
def yigindi(*sonlar):
    jami = 0
    for i in sonlar:
        jami += i
    return jami
print("yigindi(10,20,30,40,50): ", yigindi(10,20,30,40,50))

print("\n-----------Default + Required + Optional-----------")
def example(a,*c,b="Ahmad"):
    print(f"a: {a};", f"b: {b};", f"c: {c};")
example(10,11,12,2312,123,123,123,32, b="Diyorbek")

print("\n-----------Juft && Tog-----------")
son = int(input("Son kiriting: "))
juftMi = lambda son : son % 2 == 0
if juftMi(son):
    print("Juft son!")
else:
    print("Tog son!")



print("\n-----------Tub son && Tub son-----------")


def prime_mi(son):
    for i in range(2,son):
        if(son % 2 == 0):
            return False
        return True

while True:
    son = input("Tub sonni aniqlash uchun biror bir sonni kiriting: ")
    if son == "q":
        print("Yana kutib qolamiz!")
        break
    son = int(son)
    if(son == 1):
        print("Tub son emas!")
    elif(son == 2):
        print("Tub son!")
    else:
        if(prime_mi(son)):
            print("Son tub ekan!")
        else:
            print("Son tub emas ekan!")