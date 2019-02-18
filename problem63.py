#solved
t = 0
for n in range(1,2000):
    for i in range(1,2000):
        p = n**i
        if i == len(str(p)):
            print('{} ^ {} = {}'.format(n,i,p))
            t += 1
        if i < len(str(p)):
            break
print(t)