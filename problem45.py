def triangle(n=2): 
    while True:
        yield (int)((n * (n + 1) ) / 2)
        n += 1

def pentagonal(n=2): 
    while True:
        yield (int)(n * (3*n - 1) / 2)
        n += 1

def hexagonal(n=2): 
    while True:
        yield (int)(n * (2*n - 1))
        n += 1

def equal(x,y,z):
    a,b,c = next(x),next(y),next(z)
    while True:
        if a > b: b = next(y)
        if a < b: a = next(x)
        if a == b:
            if a > c: c = next(z)
            if a < c: a = next(x)
            if a - b - c == -a:
                return a
                  
print(equal(triangle(286),pentagonal(165),hexagonal(143)))