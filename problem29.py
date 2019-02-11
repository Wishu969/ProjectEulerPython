#solved
distinct = []
for a in range(2,101):
    for b in range(2,101):
        c = a**b
        if c not in distinct:
            distinct.append(c)
distinct.sort()
print(len(distinct))