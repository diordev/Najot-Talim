import random
from time import sleep
import random
from rich.progress import track

#richni kompyuterga ornatish
#pip install rich

print("""------------Random Game------------
Qoydalar:
1. 3ta imkonyatta aniq sonni topishingiz kerak
2. Agar 1tada aniq sonni topsangiz PRIZ bor

1 va 10 orasidagi sonlarni taxmin qiling!
""")


def do_step(step):
    sleep(random.uniform(0.01,0.1))
def progress(time,des):
    for step in track(range(time), description=f"{des}"):
        do_step(step)

randSon = random.randint(1,10)
imkon = 3
while True:
    kiritilinganRandSon = input("Tahminingiz: ")
    if(kiritilinganRandSon == "q"):
        print("Yana kutib qolamiz!")
        break

    kiritilinganRandSon = int(kiritilinganRandSon)

    while(kiritilinganRandSon < 0 or kiritilinganRandSon > 10):
        kiritilinganRandSon = input("Tahminingiz: ")
    if(kiritilinganRandSon > randSon):
        progress(50,"Sabr...")
        print("Kelishtiring bratan!")
        imkon -= 1
        print(f"Sizning imkonyatingiz: {imkon}")
    elif(kiritilinganRandSon < randSon):
        progress(50,"Sabr...")
        print("Qoshing bratan!")
        imkon -= 1
        print(f"Sizning imkonyatingiz: {imkon}")
    else:
        if(imkon == 3):
            print("Siz bitta da topganingiz uchun sizga MASHINA beringlar!!!")
            print(f"Javob: {randSon}")
        else:
            print("Togri topdingiz!")
            print(f"Javob: {randSon}")
    if(imkon == 0):
        print("Game over!")
        break