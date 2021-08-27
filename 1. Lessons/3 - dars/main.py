#Korosh kerak: Sprit method for input

jamoa1 = print("Birinchi jamoani kriitng")
jamoa2 = print("Ikkimchi jamoani kriitng")
jamoa3 = print("Uchinchi jamoani kriitng")

jamoalar = [jamoa1, jamoa2, jamoa3]

print("Birinchi jamo: ", jamoalar[0])
print("Ikkinchi jamo: ", jamoalar[1])
print("Uchinchi jamo: ", jamoalar[2])


print('1 < 2 and "Murod" == "Murod": => ',1 < 2 and "Murod" == "Murod")
print('1 > 2 and "Murot" == "Murod": => ', 1 > 2 and "Murot" == "Murod")

print('1 != 2 and True and False: => ', 1 != 2 and True and False)
print('True or False and False: => ', True or False and False)

print('1 < 2 or "Murod" == "Murod": => ', 1 < 2 or "Murod" == "Murod")
print('1 > 2 or "Murod" == "Murod": => ', 1 > 2 or "Murod" == "Murod")

print("1 != 2 or True or False: => ", 1 != 2 or True or False)
print("True and False or False: => ", True and False or False)

print("not 2 == 2: => ",not 2 == 2)
print('not "True" == 2: => ', not "True" == 2)

print('not (1 > 2 or "Murot" == "Murod"): => ', not (1 > 2 or "Murot" == "Murod"))



print(10 > 2)
print("Salom" == "Hello")
print("Salom" != "Hello")
print("Salom" > "Salom")
print("a" < "ab")
print("aa" > "ab")
print("a" > "z")
print("a" < "z")
print("a" > "A")
print("a" > "A")

print(11 == "11")

#ord()
print(ord("a"))
print(ord("A"))
print(chr(97))
print(chr(65))


# If else
if (10 == 10):
    print("10 10ga teng!")
    print("Hello world")
if(True):
    if(False):
        print("Hello Second IF")
    print("Hello First IF")

yosh = int(input("Yoshingizni kiriting: "))
if(yosh <= 17):
    print("Qabul qilinmadingiz!")
else:
    print("Qabul qilindingiz!")

son = int(input("Sonni kiriting: "))
if(son <= 0):
    print("Manfiy!")
else:
    print("Musbat!")

son = int(input("SOn kiriting: "))
if(son == 1):
    print("Bir")
elif(son == 2):
    print("Ikki")
elif(son == 3):
    print("Uch")
else:
    print("Qidirilayotgan son toplamdi!")

#%%
son = input("Son kiriting: ")
if(son == "1"):
    print("Bir")
elif(son == "2"):
    print("Ikki")
elif(son == "3"):
    print("Uch")
else:
    print("Qidirilayotgan son toplamdi!")

#%%
ball = int(input("Ballni kiriting: "))
if(ball > 100):
    print("GRANT")
elif(ball >= 80 and ball <= 100):
    print(5)
elif(ball >= 60 and ball < 80):
    print(4)
elif(ball >= 40 and ball < 60):
    print(3)
else:
    print("O`ta olmadingiz!")
#%%
ball = 100
if(ball >= 100):
    print("Matematika uchun otdingiz !")
if(ball > 80):
    print("Informatika uchun otdingiz !")

#%%
print("""-----Calculator-----
Quyidagi Amallardan birini tanlang:
+, Qo`shish
-, Ayrish
*, Ko`paytirish
/, Bo`lish
""")
son1 = float(input("Son1 ni kiriting: "))
amal = input("Amalni tanlang: ")
if(amal == "+" or amal == "-" or amal == "*" or amal == "/"):
    son2 = float(input("Son2 ni kiriting: "))
    if(amal == "+"):
        print(f"{son1}ni {son2}ga qoshganda = {son1 + son2}")
    elif(amal == "-"):
        print(f"{son1}ni {son2}ga ayirganda = {son1 - son2}")
    elif(amal == "*"):
        print(f"{son1}ni {son2}ga kopaytirganda = {son1 * son2}")
    elif(amal == "/")
        print(f"{son1}ni {son2}ga bolganda = {son1 / son2}")
else:
    print("Tanlangan Amal Notogri!!!")

#%% foydalanuvchi sign up qilish

db_user = "admin"
db_pass = "1122"

username = input("Ussername: ")
password = input("Password: ")

if(db_user == username and db_pass != password):
    print("Password notogri !!")
elif(db_user != username and db_pass == password):
    print("Username notogri kiritilingan")
elif(db_user == username and db_pass == password):
    print("Username va Password notogri !!!")
else:
    print("Hush kelibsiz tizimga !!!")


#%%
a = (1)
print(type(a))

b = 11,22,33,44,55,66
print(type(b))


print("e" in "Hello")
print("ell" in "Hello")
print("l" in "Hello")
print(11 in [11,22,33,44])
print(223 in [11,22,33,44,55])
print(22 in ([11,22,33,44,55,66,77]))

lst1 = [11,22,33,44,55]
for son in lst1:
    print(son)

str1 = "Najottalim"
for i in str1:
    print(i)

lst2 = [11,22,33,44,55,66,77]
for son in lst2:
    if(son % 2 == 0):
        print(son)

lst3 = [11,22,33,44,55,66,77]
for son in lst2[:4:]:
    if(lst3 % 2 == 0):
        print(son)

lst4 = [11,22,33,44,55,66,77]
jamo = 0
for s in lst3:
    jami += 3
    print(jami)

p = "Python"
for i in p:
    print(i * 3)

n1 = [(11,22),(33,44),(55,66)]
for i,j in n1:
    print(i,j)

n2 = [(11,22),(33,44,66),(55,77)]
for i in n2:
    for j in i:
        print(j)

d1 = {"bir":"one","ikki":"two","uch":"three"}
for i in d1:
    print(i)

for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i,j in d1.items():
    print(i,j,sep=" - ")




