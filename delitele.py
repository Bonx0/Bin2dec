#vypise delitele a pocet delitelov a vypise len prvociselne delitele

cislo = int(input("Zadaj cislo:"))

pocetDelitelov = 0
delitel = 1
listDelitelov = []
while delitel<=cislo:
    if cislo%delitel == 0:
        listDelitelov.append(delitel)
        pocetDelitelov += 1
    delitel += 1
print(listDelitelov)