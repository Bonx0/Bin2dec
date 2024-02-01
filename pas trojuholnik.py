
x = int(input("vyska:"))


def faktorial(cislo:int):
    spolu = 1
    while cislo > 1:
        spolu *= cislo
        cislo -= 1
    return spolu

def kombi(hore:int,dole:int):
    return faktorial(hore)//(faktorial(hore-dole)*faktorial(dole))

def trojuholnik(v:int):
    for b in range(v):
        for a in range(b+1):
            print(kombi(b,a), end=" ")
        print("\n")

trojuholnik(x)
