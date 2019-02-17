#proper divisor
#limit 28123
#sum of TWO numbers
def isabundant(n):
    temp = 0
    for i in range(1,(int)(n/2) + 1):
        if n % i == 0: temp += i
    return True if temp > n else False

templist = []
a = 0
b = 0
x = 0
while b < 28123:
    if isabundant(x):
        templist.append(x)
        a,b = b,b+a
    x += 1
print(templist)