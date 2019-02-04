def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def shift(x):
    temp = list(str(x))
    for i in range(len(str(x))):
        temp[i] = str(x)[i-1]
    return int(''.join(temp))

def circular(x):
    for _ in range(len(str(x))):
        if not isprime(x):
            return False
        x = shift(x)
    print(x)    
    return True

cnt = 0
for i in range (1,1000000):
    if ('1' in str(i) or '3' in str(i) or '9' in str(i)or '7' in str(i)) and not '6' in str(i) and not '8' in str(i)and not '4' in str(i)and not '5' in str(i)and not '2' in str(i)and not '0' in str(i):
        #print('index : {}'.format(i))
        if circular(i):
            cnt += 1  
                     
print('found: {}'.format(cnt))
    