#napiste program ktory nacita 3 vstupy a premeni ich na cisla zisti ci tieto 3 cisla mozu byt strany 
# trojuholnika ak ano overi ci je pravouhly rovnostranny alebo rovnoramenny



import math

a = int(input("1. cislo:"))
b = int(input("2. cislo:"))
c = int(input("3. cislo:"))

if a+b>c and b+c>a and a+c>b:
    print("Mozu byt strany trojuholnika.")
    if a^2 + b^2 == c^2 or c^2 + b^2 == a^2 or a^2 + c^2 == b^2:
        print("je pravouhly")
    else:
        print("nie je pravouhly")
    if a==b and b==c and a==c:
        print("je rovnostranny")
    elif a==b or b==c or a==c:
        print("je rovnoramenny")
    else:
        print("nie je rovnostranny ani rovnoramenny")
else:
    print("Nemozu byt strany trojuholnika")
    