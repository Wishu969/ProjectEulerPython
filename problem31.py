tree = [200,100,50,20,10,5,2,1]
class datalist:
    def __init__(self): self.datalist = tuple()
    def push(self,n): self.datalist += (n, )
    def pop(self): 
        temp = list(self.datalist)
        temp.pop()
        self.datalist = tuple(temp)
    def sort(self): 
        temp = list(self.datalist)
        temp.sort()
        self.datalist = tuple(temp)
    def contains(self,n): return True if n in list(self.datalist) else False
    def getTuple(self): return self.datalist
    def setTuple(self,t): self.datalist = t

def traverse(node,coin = 0,templist = datalist(),totallist = datalist()):
    coin += tree[node]
    templist.push(tree[node])
    if coin == 200:
        templist.sort()
        print(templist.getTuple())
        if templist.getTuple() not in totallist.getTuple():
            totallist.push(templist.getTuple())
            #print(totallist.getTuple())
        templist.pop()
        coin -= tree[node]
        return 0
    elif coin > 200:
        templist.pop()
        coin -= tree[node]
        return 0
    else:
        traverse(1,coin,templist,totallist)
        traverse(2,coin,templist,totallist)
        traverse(3,coin,templist,totallist)
        traverse(4,coin,templist,totallist)
        #print(totallist.getTuple())


traverse(1)

#compare and delete duplicates
#find length of list