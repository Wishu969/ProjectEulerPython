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
    if temp > 10000: break
    primelist.append(i)
print(primelist)

def func():
    length = len(primelist) - 1
    temp = 0
    cnt = 0
    for i in range(length):
        temp += i
        cnt += 1
    if isPrime(temp) != 0:
        print(temp)
        print(cnt)
    

func()