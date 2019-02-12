from multiprocessing import Pool

def reverse(n):
    return int(str(n)[::-1])

def isUneven(n):
    for i in str(n):
        if (int(i) % 2 == 0):
            return False     
    return True

def test(n):
    r = 0
    for i in range(n-10000,n):
        r += i
    return r

a = 0
def thread(limit):
    x = 0
    for i in range((int)(limit/10),limit):
        if i % 10 != 0:
            a = i + reverse(i)
            if isUneven(a):
                x += 1
    print(x)
    return x

#improve algorithm 
a = 0
if __name__ == '__main__':
    p = Pool(5)
    for i in p.map(thread,[10**1,10**2,10**3,10**4,10**5,10**6,10**7,10**8,10**9]):
        a += i
    print(a)