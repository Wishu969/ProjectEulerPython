def getSum(n):
    temp = 0
    for char in (str)(n):
        temp += ((int)(char))**2
    return temp

total = 0
for n in range(1,10**20):
    total += getSum(n)
    if n % 1000000 == 0:
        print('{} {}'.format(total,n))

print('{}EXIT'.format(total))