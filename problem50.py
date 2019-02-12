#unfinished
def isPrime(n = 2):
    for num in range(2,(int)(n**0.5) +1):
        if n % num == 0:
            return 0
    return n
def generator(n = 2):
    temp = 0
    while(True):
        if isPrime(n) != 0: 
            #temp += n
            yield n
        n += 1

primelist = []
temp = 0
for i in generator():
    temp += i
    if temp > 100: break
    primelist.append(i)

primelist.reverse()
e = 0
total = 0
for prime in primelist:
    total += prime
    if isPrime(total) != 0: e = total


print(e)