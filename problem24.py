#milionth lexicographic permutation
totalperm = []
def perm(perm_list,length,totalperm):
    if length <= 1:
        temp = ""
        for i in perm_list:
            temp += str(i)
        totalperm.append(temp)
        #print(perm_list)
        return 0
    for number in range(0,length):
        perm(perm_list,length - 1,totalperm)
        if length % 2 != 0:
            perm_list[0],perm_list[length-1] = perm_list[length-1],perm_list[0]
        else:
            perm_list[number], perm_list[length-1] = perm_list[length-1],perm_list[number]

test = [0,1,2,3,4,5,6,7,8,9]
perm(test,len(test),totalperm)
print('howdy')
totalperm.sort()
print(totalperm)
print(totalperm[999999])