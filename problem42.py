database = open(r"ProjectEulergithub\Database\databaseWords","r")
wordlist = database.readline().split(',')

def triangle(n=1): 
    while True:
        yield (int)((n * (n + 1) ) / 2)
        n += 1

def init():
    temp = []
    for i in triangle():
        if (i > 5000): break
        temp.append(i)
    return temp

def GetWordSum(a):
    n = str(a)
    temp = 0
    for i in str(n):
        temp += ((ord)(i) - 64)
    return temp + 60

tList = init()
a = 0
for i in range(len(wordlist)):
    if GetWordSum(wordlist[i]) in tList:
        a += 1
print(a)