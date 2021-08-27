#Print method
print(4.4)
print(4,2)
print("Hello world")
print(1,2,4,True,"Salom")
print("Salom\nHello\nPrivet")
print("Salom\nHello\nPrivet")

#Print sep()
#sep() => seperator() method 
#sep() => seperator print ni ichidagi , dan kegin method beriladida 
print(11,22,33,44,55,66, sep=('--'))
print("Asror","Asadbek","Ali", sep=("\n"))

#Method * in print
print("Python", sep=(" "))

# "Python" -> string to list items => ["P","y","t","h","o","n"]
print("Method *: ",*"Python", sep=("-"))

#Error code *
#1. can't use starred expression here
#a = *"Hello world" #1. bu erda yulduzcha ifodasini ishlatib bo'lmaydi
#print(a)

#BMW ni ["B","M","W"] qilib orasiga => B.M.W qilib beradi
print(*"BMW", sep=("."))

#String ni ichidagi bosh joy ham bitta belgi
print(*" BMW ", sep=".")

#Format
a = 10
b = 20 
c = 30

print("1-son: {}, 2-son: {}, 3-son: {}".format(a,b,c)) 

#format ni oziga index berish
print("1-son: {1}, 2-son: {0}, 3-son: {2}".format(a,b,c))

#format ni f korinishadi berish
print(f"1-son: {a}, 2-son: {c}, 3-son: {b}")

print("Python","C","JS", sep="-")

#end() faqat print ni ichida ishledi
#end() default => end("\n")

print("Python", "C", "JS", end=" - ")
print("Ruby", "Go", "Dart", end=" - ")
print("Rust","Cpp","C#")


#List lar
lst1 = list()
lst2 = []

print(lst1)
print(lst2)



l = [11, 22, 33, 44, True, "Hello world"]
print(l)

# Yulduzcha qoyib chiqarganimizda shunday holadi boladi
print(*l)
# result => 11, 22, 33, 44, True, "Hello world"

l1 = [11,22,33,44,55,66,77]
print("l1[0]: ", l1[0])
# ekranga l1 ni oxirgi indeksini olyabmiz
print("l1[-1]: ", l1[-1])

#list ni uzunligini olyabmiz
print("len(l1): ", len(l1))

#[start:finish:jumping]
print("l1[:3] & 3gacha boradi: ",l1[:3])
print("l1[:3:2] & 0dam 3gacha sanedi va 2tadan sakratadi: ", l1[:3:2])
print("l1[::2] & Hammasini ikktadan sakratadi: ", l1[::2])


# 2ta listni birbirga qoshish
l1 = [11,22,33]
l2 = [44,55,66]
print(l1 + l2)

l3 = [77, 88, 99]

#bu yerda hato beradi chunki str ni list ga qosholmiman devotti
#print(l3 + "Hello")

#str ni l3 ga qoshish uchun biz
print("l3 + [\"Hello world\"]: ", l3 + ["Hello world"]) # bu yerda qoshilgandaham oxiriga qoshlyabdi

#list ni ichidagi index ni value sini ozgartirish 
l4 = [111,222,333,444]
l4[0] = 555
print("l4[0] = 555: ", l4)

#list ichidagi malumotni birdaniga ozgartirish 
l5 = [555,666,777,888,999,1111]
l5[0:1] = 222,222
#item assigment
print("l5[0:1] = 222,222: ", l5)

# list ni 3ga kopaytirganda ekranga 3marta chiqarib beradi osha list ni
l6 = [4, 3, 2, 1]
print("l6 * 3: ", l6 * 3)

 
# appent() faqat list ga ishledi bu method list ni oxiriga qoshib beradi
l7 = [33, 22, 11]
l7.append(00)
print("l7.append(00): ", l7)


# pop() faqat list ga ishledi bu method list default oxiridan ochirvoradi indeksni
l8 = [111,222,333,444]
l8.pop() # bu ichiga list ni indekisi berilsa osha indeksni ochirvoradi
print("l8.pop(): ", l8)


# pop()ni ichiga list ni indekisi berilsa osha indeksni ochirvoradi
l9 = [111,222,333,444]
l9.pop(0) # bu ichiga list ni indekisi berilsa osha indeksni ochirvoradi
print("l9.pop(0): ", l9)


#insert() function ni oziga 2ta parametrni oladi 1chi parametri list ni index, 2chisi esan unga beriladigan qiymati object
l15 = [11,22,33,44]
l15.insert(2, "Hello world")#bu yerda l15 ni 2chi index ni Hello world ga tengla deyabamiz
print("l15.insert(2, \"Hello world\") => ", l5)


#sort for int
l10 = [32,12,31,23,1,312,3,123,12,312]
l10.sort()
print("[32,12,31,23,1,312,3,123,12,312] => ", l10)


#sort reverse for int
l11 = [11,2131,231,32,1,1,23,32,3,123,1,34]
l11.sort(reverse=True)
print("reverse [11,2131,231,32,1,1,23,32,3,123,1,34] => ", l11)


#sort for str
l12 = ["Samsung", "Oneplus", "Huawei", "Apple"]
l12.sort()
print('["Samsung", "Oneplus", "Huawei", "Apple"] => ', l12)

#sort for str
l13 = ["Samsung", "Oneplus", "Huawei", "Apple"]
l13.sort(reverse=True)
print("['Apple', 'Huawei', 'Oneplus', 'Samsung'] => ", l13)

# sort str lar harfga qarab emas odatta ichidagi hamma elamentiga qarab sort ledi
l14 = ["a" , "ab", "aab", "abb"]
l14.sort()
print('["a" , "ab", "aab", "abb"] => ',l14)

#matritsa tuzish
mrs1 = [11,22,33]
mrs2 = [44,55,66]
mrs3 = [77,88,99]
# mrs1 mrs2 mrs3 ni hammasini bitta list ga tuzish
mrs4 = [mrs1, mrs2, mrs3]
print("[mrs1, mrs2, mrs3] => ", mrs4)
print("mrs4[0][-1] => ", mrs4[0][-1])
print("mrs4[-1][-1] => ", mrs4[-1][-1])




#TUPL -> Ozgarmas degani
#TUPL ni List lardan farqi bu ozgartira olmimizham hamda qosha olmimiz
tpl1 = tuple()
tpl2 = ()

print(type(tpl1))
print(type(tpl2))


tpl3 = (11,22,33,44,55)
print("Tuple: ", tpl3)

#Tuple Error codes
#tpl3.append(11)
#tpl3.pop()
#tpl3.insert()


tpl4 = (11,22,33,5,"Hello",True,[11,22,33],(44,55,77))
print(tpl4[-2][-1])# tpl4 ni ichidagi list da gi 33ni chiqarmoqchi bolsa




#DICTIONARY => Lugat - object key && values
#Dictionart da faqat key lari orqali ushab olamiz
dict1 = {}
dict2 = dict()

print(type(dict1))
print(type(dict2))

dct1 = {
            "bir": "One",
            "Ikki": "Two",
            "Uch": "three",
            "Tort": "four"
        }

print(dct1["bir"])

dct2 = {"a": [11,22,{"b": [33,44,55]}]}
print(dct2["a"][-1]["b"][-1])#55 ni ekranga chiqarish 


#Error codes dictionary
#print(dct1[12312312312])#print ga dictionary yoq key ni beradiga bolsek
# KeyError qaytaradi chunki bu key dictionary da mavjud emas


dct3 = {1: "a", 2: "ikki", 3: "uch"}
print(dct3)

dct4 = {"a": 11, "b":22, "c": 33}
dct4["a"] = 111
#dictionary da yoq key ni kiritib unga value beradiga bolsek dictionary ni oxiridan qoshadi
dct4["h"] = "Hello"
print(dct4)

#dictionary ni faqat key larini olish uchun
print("dct4.keys() => ", dct4.keys())
#dictionary ni faqat velue larini olish uchun
print("dct4.values() => ", dct4.values())
#dictionary ni polniy olish uchun items()
print("dct4.items() => ", dct4.items())



#Input

# input()
#a = input()
#print(a)

b = int(input("Son kiriting: ")) # !input dan xardoyim str type da malumot kealdi bi buni int qilib olishimiz kerak chun str ni int ga qoshib bolmidi shuning uchun
print(b + 1000)


a = int(input("1chi sonni kiriting: "))
b = int(input("2chi sonni kiriting: "))
c = int(input("3chi sonni kiriting: "))
print("a + b + c: ",a + b + c)