a = []
b = []

def insert(a,b,c):
    test = []
    test.extend(str(a))
    test.extend(str(b))
    test.extend(str(c))
    return test

def is_pan(l):
    example = [1,2,3,4,5,6,7,8,9]
    if len(l) != 9: return False
    l.sort()
    for n in range(9):
        if l[n] != str(example[n]):
            return False
    return True

# 39 × 186 = 7254
print(is_pan(insert(39,186,7254)))
q = 0
for x in range(1,999):
    for y in range(1,999):
        if x in b and y in a: pass
        else:
            test = []
            if x*y == y*x:
                z = x * y
                test = insert(x,y,z)
                if is_pan(test):
                    print('product found', x,y,z)
                    q += z
                    a.append(x)
                    b.append(y)

print(q)