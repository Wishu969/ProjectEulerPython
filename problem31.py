#unsolved
tree = [200,100,50,20,10,5,2,1]
totallist = []
templist = set()
#find good datastructure
#should be able to compare
#nested structure allowed
#must have push(),pop() or append(),remove()



def traverse(node,coin):
    coin += tree[node]
    templist.add(tree[node])
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
        traverse(1,coin)
        traverse(2,coin)

coin = 0
traverse(1,coin)
print(totallist)
#compare and delete duplicates
#find length of list