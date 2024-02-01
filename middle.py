
cislo = int(input("Zadaj cislo:"))
listCisel = []
x = 0
length = len(str(cislo))
while cislo>0:
    x = cislo % 10
    listCisel.append(x)
    cislo //= 10
if length % 2 == 0:
    priemer = (listCisel[length//2] + listCisel[(length//2)-1])/2
    print(priemer)
else:    
    v = listCisel[length//2]
    print(v)