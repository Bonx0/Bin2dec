cislo = int(input("Zadaj cislo:"))

cifra = 0
sumaCifier = 0
while cislo != 0:
    cifra = cislo % 10
    sumaCifier += cifra
    cislo //= 10
print(f"Suma cifier {sumaCifier}")