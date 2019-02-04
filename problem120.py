#finished
def func(a,n):
    return ((a-1)**n + (a+1)**n)%a**2

maxtotal = 0
for k in range (3,1001):
    maxn = 0
    for i in range(1,1500):
        temp = func(k,i)
        if temp > maxn:
            maxn = temp
    print('for {} max number is {}'.format(k,maxn))
    maxtotal = maxtotal + maxn
print('SUM: {}'.format(maxtotal))
#333082500