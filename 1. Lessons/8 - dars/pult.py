#PULT UCHUN CLASS
from time import sleep, time
from types import prepare_class
class Pult():
    def __init__(self, tv_holat="Off", tv_ovoz=0,kanal_list=["BBC","MY5"], kanal="BBC"):
        print("Pult kiritilmoqda......")
        self.tv_holat = tv_holat
        self.tv_ovoz = tv_ovoz
        self.kanal_list = kanal_list
        self.kanal = kanal
    
    #Ovoz bilan ishlash 
    def __str__(self):
        if (self.tv_holat == "On"):
            return f"""Tv Holati: {self.tv_holat}
    Ovoz: {self.tv_ovoz}
    Kanal listi: {self.kanal_list}
    Hozirgi Kanal: {self.kanal}
            """
        else:
            return "Televizor ocihrilgan..."
    def ovoz_ozgartirish(self):
        while True:
            soniya = 5
            belgi = input("+ | -: ")
            if(belgi == "+"):
                if(self.tv_ovoz < 5):
                    self.tv_ovoz += 1
                    print(f"Ovoz +: {self.tv_ovoz}")
                    soniya = 5
                    continue
            elif(belgi == "-"):
                if(self.tv_ovoz > 0):
                    self.tv_ovoz -= 1
                    print(f"Ovoz -: {self.tv_ovoz}")
                    soniya = 5
                    continue
            else:
                print("Ovoz yangilandi...")
                print(f"Ovoz -: {self.tv_ovoz}")
                break
            for i in range(4, -1, -1):
                sleep(1)
                print("Maksimal ovoz 5")
                soniya -= 1
            if soniya <= 0:
                print("................")
                break
    
    def tv_power(self):
        if(self.tv_holat == "On"):
            print("Tv ochirilmoqda...")
            self.tv_holat = "Off"
        else:
            print("Tv yoqilmoqda")
            self.tv_holat = "On"
        
# for x in range(1,4):
#     sleep(1)
#     if x == 3:
#         print("Hello world")