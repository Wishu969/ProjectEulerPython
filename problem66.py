#x2 – Dy2 = 1
high = 0
for D in range(98,1000):
    x,y,a = 1,1,0
    while a != 1 and D != (int)(D**0.5)**2:
        a = (x**2) - (D*(y**2))
        if a > 1: y += 1
        if a < 1: x += 1
    if x > high: high = x
    print('{}^2 - {} * {}^2 = {} HIGHEST {}'.format(x,D,y,a,high))

#66249    // 61
#2281249  // 97