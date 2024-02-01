import math


a = int(input("Zadaj cislo:"))

b=0

while a>0:
    b += a % 10
    a = a // 10
    
    
print(b)
    