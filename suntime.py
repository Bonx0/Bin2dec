
h = int(input("Zadaj hodiny:"))
m = int(input("Zadaj minuty:"))

angle = (180/12*(h-6))+(180/720*m)

print(angle)