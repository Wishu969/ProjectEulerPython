#solved
def fraction(n, d = 1):
    for _ in range(10000):
        x = (int)(d/n)
        if x != 0:
            yield x
            if d % n == 0: 
                return
            else:
                d = d % n
        else:
            d *= 10

def get_recursion(fractionNumber):
    fractionList = list(map(int,fraction(fractionNumber)))
    for begin in range(0,len(fractionList) - 1):
        for new in range(1,len(fractionList) - 2):
            try:
                length = fractionList.index(fractionList[begin],new+1,len(fractionList) - 1)
                recursionTest = fractionList[begin:length]
                recusrsionTest2 = fractionList[length:(length*2)-begin]
                if recursionTest == recusrsionTest2:
                    return recusrsionTest2
            except: pass
    return [0]

high = 0 
temp = []
highlist = []
for i in range(1,1000):
    temp = get_recursion(i)
    if len(temp) > high: 
        high = len(temp)
        highlist = temp.copy()
        print(i)
        #print(''.join(str(e) for e in temp))