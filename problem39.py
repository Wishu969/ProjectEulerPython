#solved
def pythagoras(a,b): 
    return ((a**2 + b**2)**0.5)


lista = []
listb = []
n = 0
highest = 0
hign = 0
for P in range(1,1000):
    for a in range(1,(int)(P/2)):
        for b in range(1,(int)(P/2)):
            if a in listb and b in lista: 
                pass
            else:
                c = pythagoras(a,b)
                if (a+b+c) == P:
                    n += 1
                    lista.append(a)
                    listb.append(b)
                    #print(a,b,c,P)
    if n == 0: pass
    else:
        if n > hign: 
            hign = n
            highest = P
        print(P,n,highest)
        n = 0
print("done")