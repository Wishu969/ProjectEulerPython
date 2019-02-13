from enum import Enum
def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)
def getDays(year):
    return 365 + isLeapYear(year)
class day(Enum):
    monday = 1
    tuesday = 2
    wednesday = 3
    thursday = 4
    friday = 5
    saturday = 6
    sunday = 7

l = [3,0,3,2,3,2,3,3,2,3,2,3]
k = [3,1,3,2,3,2,3,3,2,3,2,3]
m = []
for year in range(1901,2001):
    if isLeapYear(year):
        m.extend(k)
    else:
        m.extend(l)
cnt = 0
a = 2
for i in m:
    a += i
    if a > 7: a-=7
    print(day(a))
    if a == 7: cnt += 1
print(cnt)