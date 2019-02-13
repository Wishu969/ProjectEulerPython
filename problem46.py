def generator(n = 1):
    while (True):
        if n % 2 != 0:
            if not isprime(n):
                yield n
        n += 1

def gen(n = 1):
    while (True):
        yield (2 * (n**2))
        n += 1

def isprime(n):
    for i in range(2,(int)(n**0.5)+1):
        if n % i == 0: return False
    return True

for odd in generator():
    if odd > 1000000: break
    for i in gen():
        a = odd - i
        if a < 0: 
            print('HMM {}'.format(odd))
            break
        if isprime(a): break