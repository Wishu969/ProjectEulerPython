distinct = []

for a in range(2,6):
    for b in range(2,6):
        if a**b not in distinct:
            distinct.append(a**b)
            
distinct.sort()
print(distinct)