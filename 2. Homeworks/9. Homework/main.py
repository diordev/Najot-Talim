print("""\nProblem 8: Integerdan tashkil topgan listni ichidagi hamma elementlar yigindisini hisoblang""")
"""
lst1 = [11,22,33,44,55,66,77]
jami = 0
for x in lst1:
    jami += x
print(f"{lst1}: {jami};")
"""

print("""\nProblem 9: Listdagi 3 ta ballni taqqoslaydigan dastur""")
"""
a = [6, 6, 7]
b = [5, 6, 2]

a1 = 0
b1 = 0
for i in range(len(b)):
    if(a[i] > b[i]):
        a1 +=  1
    elif(a[i] < b[i]):
        b1 += 1
r1 = [a1,b1]
print(r1)
"""
print("""\nProblem 10: 3 ga 3 matrits dioganallarini absolyut farqlarini toping""")
"""
matritsa = [
    [11,22,33],
    [44,55,66],
    [77,88,99],
]
print("Matritsa: ")
to_down = matritsa[0][0] + matritsa[1][1] + matritsa[-1][-1]
to_up = matritsa[-1][1] + matritsa[1][-1] + matritsa[0][-1]
absolute = abs(to_down - to_up)
print(f"Absolute: |{to_down} - {to_up}| = {absolute}")
"""
print("""\nProblem 11: 3 ta bir xil uzunlikdagi list elementlari yigindisini hisoblash""")
"""
lst1 = [11,22,33]
lst2 = [44,55,66]
lst3 = [77,88,99]
res1,res2,res3 = 0,0,0
for q,w,e in lst1,lst2,lst3:
    res1 += q
    res2 += w
    res3 += e
result = int(res1 + res2 + res3)
print("Result: ",(result))
"""

print("""\nProblem 12: Berilgan listni o'sib borish tartibida sortlash 3 xil usulda ishlang""")
"""
lst1 = [11,22,33,44,55,66,77,88]
lst1.sort(reverse=Trues) 
print("First: ",lst1)
"""
"""
lst2 = [11,22,33,44,55,66,77,88]
lst2.sort()
print("Second: ",lst2)
"""



print("""\nProblem 13: Raqam kiritlsa o'ssh raqamni so'zga aylantirib beradigan dastur yozing""")
"""
def funRead(number):
    if(number == 10):
        print("O`ng")
    elif(number == 20):
        print("yigirma")
    elif(number == 30):
        print("o'ttiz")
    elif(number == 40):
        print("qirq")
    elif(number == 50):
        print("ellik")
    elif(number == 60):
        print("oltmish")
    elif(number == 70):
        print("yetmish")
    elif(number == 80):
        print("sakson")
    elif(number == 90):
        print("toqson")
    else:
        dict1 = {1:"o'n",2:"yigirma",3:"o'ttiz",4:"qirq",5:"ellik",6:"oltmish",7:"yetmish",8:"sakson",9:"toqson",}
        dict2 = {1:"bir",2:"ikki",3:"uch",4:"tort",5:"besh",6:"olti",7:"yetti",8:"sakkiz",9:"to'qqiz"}
        n1 = number // 10
        n2 = number % 10
        print(dict1[n1],end=(' '))
        print(dict2[n2])
funRead(int(input("Sonni kiriting -> Harfga o'giramiz! : ")))
"""

print("""\nProblem 14: a listni ichida 3 ta listdan tashkil topgan elementlari bor 
a listni hamma elementlarini int holatda boshqa bir listga kochiring.""")
"""
aa = [[11,22,33],[11,22,33],[11,22,33]]
bb = [int(x) for i in aa for x in i]
print(bb)
"""
