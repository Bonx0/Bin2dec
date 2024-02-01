def mostFrequent(zoz: list):
    pocet = 0
    index = 0
    for i in range(len(zoz)):
        if zoz.count(zoz[i]) > pocet:
            pocet = zoz.count(zoz[i])
            index = i
    
    return (zoz[index], pocet)


print(mostFrequent(["a","b","c","a","b","b"]))

