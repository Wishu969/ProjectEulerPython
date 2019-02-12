from multiprocessing import Pool

def reverse(n):
    return int(str(n)[::-1])

def isUneven(n):
    for i in str(n):
        if (int(i) % 2 == 0):
            return False     
    return True

def thread(start,limit):
    x = 0
    for i in range(start,limit):
        if i % 10 != 0:
            a = i + reverse(i)
            if isUneven(a):
                x += 1
    print(x)
    return x
l = [ ( 10**8 , 2* (10**8) ) , ( 2* (10**8) , 3* (10**8) ) , ( 3* (10**8) , 4* (10**8) ) , ( 4* (10**8) , 5* (10**8) ) ]
k = [ ( 5* (10**8) , 6* (10**8) ) , ( 6* (10**8) , 7* (10**8) ) , ( 7* (10**8) , 8* (10**8) ) , ( 8* (10**8) , 9* (10**8) ) , ( ( 9* (10**8) , 10**9 ) ) ]
a = 0
if __name__ == '__main__':
    p = Pool(6)
    for i in p.starmap(thread,l):
        a += i
    print(a)

    #18720 // 1-10**6
    #50000 // 10**6 - 10**7
    #734400 // 10**7 - 10**8