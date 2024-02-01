a = int(input("vyska:"))
b = str(input("symbol:"))


def trojuholnik(v:int,s:str):
    for b in range(v):
        for a in range(b+1):
            print(s, end=" ")
        print("\n")
        
def trojuholnik2(height:int,symbol:str):
    for line in range(height):
        print((" ")*((height*2+1)-(line*2+1)),(symbol+" ")*(line*2+1))

trojuholnik2(a,b)