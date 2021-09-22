import math 

print("""Calculator

Amalni tanlang:
1. Qoshish
2. Ayrish
3. Kopaytirish
4. Bolish

Chiqish: q
""")
amal = int(input("Iltimos amalni kritiing: "))
while True:
    while amal < 0 or amal > 4:
        amal = int(input("Iltimos amalni kritiing: "))
    amal = str(amal)
    if(amal == "q"):
        print("Yana kutib qolamiz!")
    amal = int(amal)

    son = input("Iltimos qoshmoqchi bolgan hohlagan soni kirting(11 22 33 44 55): ")
    son = son.split()
    res = 0

    if(amal == 1):
        for x in son:
            res += float(x) 
        print(f"Result: ", res)
    elif(amal == 2):
        for x in son:
            res -= float(x)  
        print(f"Result: {res}")
        break
    elif(amal == 3):
        for x in son:
            res *= float(x)  
        print(f"Result: {res}")
        break
    elif(amal == 4):
        for x in son:
            res //= float(x) 
        print(f"Result: {res}")
        break
    