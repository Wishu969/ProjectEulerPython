#Considering natural numbers of the form, ab, 
# where a, b < 100, what is the maximum digital sum?
maxsum = 0
temp = 0
for a in range(1,100):
    for b in range(1,100):
        temp = a ** b
        total = 0
        for char in (str)(temp):
            total += (int)(char)
        if maxsum < total: maxsum = total
print(maxsum)