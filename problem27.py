def is_prime(n):
    for i in range(2,(int)((n)**0.5) + 1):
        if n % i == 0: 
            return False
    return True

def get_next_prime(n):
    n += 1
    while not is_prime(n): 
        n += 1
    return n

counter = 0
high = 0
for prime in range(2,1):
    if is_prime(prime):
        for a in range(-999,999):
            counter = -1
            n = 0
            try:
                while is_prime(n**2 + a*n + prime):
                    n += 1
                    counter += 1
                if counter > high: 
                    high = counter
                    print(a,prime,counter,a*prime)
            except: pass