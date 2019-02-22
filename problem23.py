#proper divisor
#limit 28123
#sum of TWO numbers
def isabundant(n):
    temp = 0
    for i in range(1,(int)(n/2) + 1):
        if n % i == 0: 
            temp += i
    return temp > n 

templist = []
a = 0
b = 28124
x = 0
while b < 28123:
    if isabundant(x):
        templist.append(x)
        a,b = b,b+a
    x += 1
print(isabundant(12))
print(templist)