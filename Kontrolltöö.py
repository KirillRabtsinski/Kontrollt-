from random import *
#4var
#5Ülesanne Sponge Bob praeb lihapalle. Kokku on tal K kotlette, ühele pannile mahub M kotlette.
#Arvuta, mitu "täis" panni on vaja praadida ja kui palju kotlette jääb viimasele veel praadida.
print("Ülesanne 5")
K = int(input("Sisestage kõigi kotlettide arv: "))
M = int(input("Sisestage ühel pannil praaditavate kotlettide arv: "))

full_pans = K // M
remaining_cutlets = K % M

print("Full pans needed:", full_pans)
print("Remaining cutlets:", remaining_cutlets)

#4Ülesanne Üherakuline amööb jaguneb iga 3 tunni järel 2 rakuks. Määrake, kui palju rakke on 3, 6, 9, ..., 24 tunni pärast, kui algselt oli üks amööb.
print("Ülesanne 4")
amööb = 1

for i in range(3, 25, 3):
    amööb *= 2
    print(f"Pärast {i} Tundi: {amööb} on kamber")   
   
#3Ülesanne Iga klassi õpilase füüsika hinded on teada. Määrake minimaalne ja maksimaalne punktisumma. (Hinded ja õpilaste arv saadakse juhuslikult)
print("Ülesanne3")
import random

class_size = int(input("Kirjutage õpilaste arv: "))
hinne = [random.randint(0, 100) for _ in range(class_size)]

min_hinne = min(hinne)
max_hinne = max(hinne)

print("Minimum hinne:", min_hinne)
print("Maximum hinne:", max_hinne)
#2Ülesanne Trüki naturaalarvude astmed, mis ei ületa antud arvu n. Kasutaja määrab eksponendi ja arvu n.
print("Ülesanne2")
exponent = int(input("Seadke eksponent n: "))
n = int(input("Seadke arv n: "))

for i in range(1, n+1):
    print(i**exponent)


#1Ülesanne Koostage programm, mis, kui anda arvu n vahemikus 1 kuni 9, kuvab ekraanil n looma. Kahe naaberlooma vahel on ka tühi (tühikutest) veerg
print("Ülesanne1")
n = int(input("Kirjutage arv vahemikus 1 kuni 9: "))
peegel = """
  ^---^
 (o o )
   ! =!/)
"""

for i in range(n):
    print(peegel, end="  ")
