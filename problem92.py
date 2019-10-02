#solved
def chain(n):
    temp = 0
    for c in str(n):
        temp += int(c)**2
    return temp

def arrive(x):
    while(1):
        if x == 89:
            return True
        elif x == 1:
            return False
        else:
            x = chain(x)

counter = 0

for i in range(2,10**2): 
    if arrive(i): 
        counter += 1
print(counter)

for i in range(10**2,10**4): 
    if arrive(i): counter += 1
print(counter)

for i in range(10**4,10**5): 
    if arrive(i): counter += 1
print("test",counter)

for i in range(10**5,10**6): 
    if arrive(i): counter += 1
print("almost", counter)

for i in range(10**6,10**7): 
    if arrive(i): counter += 1
print("done", counter)