
h = int(input("hodiny:"))
m = int(input("minuty:"))

def map(a:int,b:int,c:int,d:int,x:int,):

    y = ((d-c)/(b-a)*(x-a))+c

    return y



hangle = map(0,12,0,360,h)
mangle = map(0,60,0,360,m)
hangle += map(0,60,0,30,m)


print(abs(hangle-mangle))