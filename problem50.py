#unfinished
def isPrime(n = 2):
    for num in range(2,(int)(n**0.5) + 1):
        if n % num == 0:
            return 0
    return n

def generator(n = 2):
    while(True):
        if isPrime(n) != 0: 
            #temp += n
            yield n
        n += 1

primelist = []
temp = 0
for i in generator():
    temp += i
    if temp > 10: break
    primelist.append(i)
print(primelist)

def bit_mask(l):
    x = len(l)
    bit = 7
    temp = 0
    while bit != 0:
        temp = 0
        bit = bin(bit)
        q = str(bit)[2:]
        for s,i in zip(q,range(0,3)):
            if s == "1":
                temp += l[i]
        print(temp)
        bit = int(q,2)
        bit -= 1

if __name__ == '__main__':
    bit_mask(primelist)