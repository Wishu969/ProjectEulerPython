#solved
def isPalindrome(n):
    return True if list(str(n)) == list(reversed(list(str(n)))) else False

def base(n): return (int)(bin(n)[2:len(bin(n))])

a = 0
for i in range(1,1000000):
    if isPalindrome(i) and isPalindrome(base(i)):
        a += i

print(a)