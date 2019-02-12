def getSum(n):
    temp = 0
    for char in (str)(n):
        temp += ((int)(char))**2
    return temp

print(getSum(442))