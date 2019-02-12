def isPrime(n = 2):
    for num in range(2,(int)(n**0.5) +1):
        if n % num == 0:
            return 0
    return n

temp = 0
totalprime = 0
cnt = 1
while temp < 100:
    cnt += 1
    temp += isPrime(cnt)
    if isPrime(temp) != 0:
        totalprime = temp

print(totalprime)