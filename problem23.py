#proper divisor
#limit 28123
#sum of TWO numbers
with open(r'D:\Python\Courses\ProjectEulergithub\Database\databaseProblem23') as file:
    lines = file.read().splitlines()
lines = list(map(int, lines))

def isabundant(n = 1):
    while n < 30000:
        temp = 0
        for i in range(1,(int)(n/2) + 1):
            temp = temp + i if n % i == 0 else temp + 0
        if temp > n: 
            print(n, temp)
            yield n
        n += 1

full = []
def insert_in_file(a):   
    for i in isabundant():
        a.write(str(i) + "\n")
        full.append(i)

def search(n, l):
    y = len(l) - 1
    x = 0
    while l[x] + l[y] != n:
        #print('{} {} = {}'.format(x,y,l[x] + l[y]))
        if l[x] == l[y]: return True
        if x > y: return True
        if l[x] + l[y] > n: y -= 1
        if l[x] + l[y] < n: x += 1
    return False

test = 0
for i in range(1,1):
    if search(i,full):
        print(i)
        test += 1

print(lines)
#print(search(28124,full))
#print(full)