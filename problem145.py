# unfinished code 
#print does not equel example on project euler
#10,30,50,70,90 not allowed
def reverse(n):
    return int(str(n)[::-1])

def isUneven(n):
    for i in str(n):
        if (int(i) % 2 == 0):
            return False     
    return True

x = 0
for i in range(10**3):
    if i % 10 != 0:
    #print('{} + {} = {} ... {}'.format(i,reverse(i), i+reverse(i), isUneven(i+reverse(i))))
        if isUneven(i + reverse(i)):
            print('{}......{}'.format(i,i+reverse(i)))
            x += 1

print(x)
#improve algorithm 