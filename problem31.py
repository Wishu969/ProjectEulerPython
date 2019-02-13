#unsolved
tree = [200,100,50,20,10,5,2,1]
#find good datastructure
#should be able to compare
#nested structure allowed
#must have push(),pop() or append(),remove()
#USE TUPLE AND LIST
class datalist:
    def __init__(self): self.datalist = tuple()
    def push(self,n): self.datalist += (n, )
    def pop(self): self.datalist = tuple(list(self.datalist).pop())
    def sort(self): self.datalist = tuple(list(self.datalist).sort())
    def contains(self,n): return True if n in list(self.datalist) else False


def traverse(node,coin = 0,templist = datalist(),totallist = datalist()):
    coin += tree[node]
    templist.push(tree[node])
    if coin == 200:
        print(templist)
        if templist not in totallist:
            totallist.append(templist)
            print(totallist)
        templist.discard(tree[node])
        coin -= tree[node]
        return 0
    elif coin > 200:
        templist.discard(tree[node])
        coin -= tree[node]
        return 0
    else:
        traverse(1,coin,templist,totallist)
        traverse(2,coin,templist,totallist)


traverse(1)

#compare and delete duplicates
#find length of list