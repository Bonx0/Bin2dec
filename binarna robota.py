import math

a = int(input("Zadaj cislo:"))

c=0
b=0
while a>0:
    
    b += (a%2)*(10**c)
    a = a//2
    c += 1
print(b)
    