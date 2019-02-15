def triangle(n): return (int)((n * (n + 1) ) / 2)
def pentagonal(n): return (int)(n * (3*n - 1) / 2)
def hexagonal(n): return (int)(n * (2*n - 1))

for t in range(1,300):
    for p in range(1,300):
        for h in range(1,300):
            x = triangle(t)
            y = pentagonal(p)
            z = hexagonal(h)
            if x == y and x == z:
                print(x+y+z)
