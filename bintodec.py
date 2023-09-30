import math

a = int(input("Zadaj cislo:"))

c=0
b=0
while a>0:
    
    b += (a%10)*(2**c)
    a = a//10
    c += 1
print(b)
    