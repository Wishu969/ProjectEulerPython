#milionth lexicographic permutation
def perm(n):
    perml = ()
    numlist = tuple(str(n))
    x = len(numlist)
    a = x-1
    perml.__add__(x)
    return x


print(perm('0123'))
#012
#021
#102
#120
#201
#210