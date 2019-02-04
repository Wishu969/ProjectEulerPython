def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)    

def factsum(n):
    t = 0
    for i in str(n):
        t += factorial(ord(i) - 48)
    return t

def sfactsum(n):
    temp = factsum(n)
    t = 0
    for i in str(temp):
        t += ord(i) - 48
    return t

def smallint(n):
    i = 1
    while True:
        if n == sfactsum(i):
            return i
        else:
            i=i+1

def sumsmallint(n):
    s = smallint(n)
    temp = 0
    for i in str(s):
        temp += ord(i) - 48
    return temp
#inskjdfsdf
#temp = 0
#for i in range(1,151):
#    print(i)
#    temp += sumsmallint(i)
#print(temp)
for i in range (1,100):
    print('{}   {}    {}'.format(i,smallint(i),sumsmallint(i)))