#solved
counter = 1
finallist = []
for n in range(7,100):
    temp = 0
    for i in range(2,10):
        total = 0
        temp = n**i
        for char in str(temp): total += ord(char)-48
        if total == n:
            finallist.append(temp)
            counter += 1
finallist.sort()
for a in finallist: print(finallist.index(a) + 1,a)