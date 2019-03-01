tree = [0,1,2,5,10,20,50,100,200]

def traverse(node,coin = 0,templist = list(),totallist = list()):
    coin += tree[node]
    templist.append(tree[node])
    if coin == 200:
        a = templist.copy()
        a.sort()
        if a not in totallist:
            totallist.append(a.copy())
            print(templist)
            print('DONE',len(totallist))
        templist.pop()
        coin -= tree[node]
        return
    if coin > 200:
        templist.pop()
        coin -= tree[node]
        return
    traverse(1,coin,templist,totallist)
    traverse(2,coin,templist,totallist)
    traverse(3,coin,templist,totallist)
    traverse(4,coin,templist,totallist)
    traverse(5,coin,templist,totallist)
    traverse(6,coin,templist,totallist)
    traverse(7,coin,templist,totallist)
    traverse(8,coin,templist,totallist)
    templist.pop()
    coin -= tree[node]
    return
traverse(0)
print('DONE!!!')
#compare and delete duplicates
#find length of list