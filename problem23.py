#proper divisor
#limit 28123
#sum of TWO numbers
def isabundant(n = 1):
    while n < 200:
        temp = 0
        for i in range(1,(int)(n/2) + 1):
            temp = temp + i if n % i == 0 else temp + 0
        if temp > n: 
            yield n
        n += 1

full = []
for i in isabundant():
    full.append(i)
print(full)

def search(n, l):
    y = len(l) - 1
    x = 0
    while l[x] + l[y] != n:
        print('{} {} = {}'.format(x,y,l[x] + l[y]))
        if l[x] == l[y]: return False
        if l[x] + l[y] > n: y -= 1
        if l[x] + l[y] < n: x += 1
    return True

for i in range(1,28123):
    if search(i,full):
        