#solved
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
        if l[x] == l[y]: return False
        if x > y: return False
        if l[x] + l[y] > n: y -= 1
        if l[x] + l[y] < n: x += 1
    return True

test = 0
for i in range(1,28124):
    if not search(i,lines):
        print(i)
        test += i    
print(test,test)