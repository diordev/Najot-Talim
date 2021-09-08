# Problem 1:
# Foydalanuvchidan olgan raqamingiz mukammalligini aniqlashga harakat qiling.(PERFECT NUMBER)
# Agar sonning bo'linmasining yig'indisi o'ziga teng bo'lsa bu raqam "mukammal son" deyiladi. 
# Misol sifatida 6 - bu mukammal son. (1 + 2 + 3 = 6)

son = int(input("Mukammal sonni bilmoqchi bolsez iltimos hohlagan sonizi kiritng: (1,2,3,4,5,6)"))

result = 0
for i in range (1, son):
    if son % i == 0:
        result = result + i

if result == son:
    print(f"{son} -  bu mukammal son")
else:
    print(f"{son} - bu mukammal son emas")


# Problem 2 
# Siz foydalanuvchidan olgan raqam "Armstrong" raqam ekanligini aniqlashga harakat qiling.
# Masalan, agar raqam 4 ta raqamga ega bo'lsa va uni tashkil etuvchi raqamlarning har birining 
# 4-darajaning yig'indisi (3 xonali sonlar uchun 3-darajali) bu raqamga teng bo'lsa, 
# bu raqam "Armstrong" raqami deb nomlanadi.
# Masalan: 1634 = 1 ^ 4 + 6 ^ 4 + 3 ^ 4 + 4 ^ 4

n1 = input("Iltimos sonni kiriting: ")
n2 = [int(x) for x in n1]
result = 0

for i in n2:
    i = i ** len(n1)
    result = result + i
n1 = int(n1)

if n1 == result:
    print(f"{n1} - armstrong son")
else: 
    print(f"{n1} - armstrong son emas!")



# Problem 3
# Ekranda 1 dan 10 gacha bo'lgan raqamlar bilan ko'paytirish jadvalini chop etishga harakat qiling.
# Eslatma: Ichma Ich Loopdan Foydalaning. Shuningdek, range() funktsiyasidan foydalanib raqamlarni oling.
for a in range(1, 11):
    print(f"--------{a}--------")
    for b in range(1, 11):
        print(f"{a} * {b} = {a * b}")


# Problem 4
# Har bir while loopida foydalanuvchidan raqam oling va foydalanuvchi kiritgan raqamlarni "sum" nomli o'zgaruvchiga qo'shing. 
# Foydalanuvchi "q" tugmachasini bosganda loopni tugatib "yig'indisini" ekranda chop eting.
sum = 0
while True:
    n1 = int(input("Enter your number: "))
    if(n1 == 'q'):
        print(f"Siz kiritgan sonlar - {sum}")
        break
    sum = sum + n1
    print(sum)



# Problem: 5
# Faqat 1 dan 100 gacha bo'lgan raqamlar orasida ekranga 3 ga bo'linadiganlarini chop eting.
for i in range(1, 101):
    if(i % 3 == 0):
        print(f"{i} 3ga bolinadi!")



# Problem 6
Problem: 6
# Muammoning yechimini biz darslarimizda o'rganganmiz(LIST COMPREHENSION). 
# Bu yerda mulohaza yuritish va listni tushunishdan foydalanib, 7
# 1 dan 100 gacha bo'lgan juft sonlarni listga otkaizshga harakat qiling.
# l1 = [x for x in range(1,101) if(x % 2 == 0)]

a = 123
if isinstance(a, int):
    print("Hello world")




