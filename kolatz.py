

cislo = int(input("Zadaj cislo:"))
kolatz = [cislo]
while cislo != 1:
    if  cislo % 2 == 0:
        cislo /= 2
        kolatz.append(cislo)
    else:
        cislo = 3*cislo+1
        kolatz.append(cislo)
print(kolatz)