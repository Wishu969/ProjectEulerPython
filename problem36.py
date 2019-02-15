def isPalindrome(n):
    return True if list(str(n)) == list(reversed(list(str(n)))) else False

def base(n):
    return (int)(bin(n)[2:len(bin(n))])


print(isPalindrome(base(3)))
#4 = 100
#3 =  11
#2 =  10
#1 =   1