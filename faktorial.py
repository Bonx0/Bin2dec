
cislo = int(input("Zadaj cislo:"))
spolu = 1

while cislo > 1:
    spolu *= cislo
    cislo -= 1
print(spolu)