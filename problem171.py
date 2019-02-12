import time
import itertools
l = [0,1,4,9,16,25,36,49,64,81]
def getSum(n):
    temp = 0
    for char in (str)(n):
        temp += ((int)(char))**2
    return temp



total = 0
for n in range(1,100):
    total += getSum(n)
    print('{} {}'.format(total,n))



print('{}EXIT'.format(total))


start = time.time()
temp = 0
for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t in itertools.product(l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l,l):
    temp += (a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t)
    if temp % 1000000000 == 0: print(temp)
end = time.time()
print(end - start)
print(temp)