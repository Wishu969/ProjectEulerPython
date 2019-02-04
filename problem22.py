database = open("ProjectEuler\Database\databaseNames.txt","r")
namelist = database.readline().split(',')
sortedlist = sorted(namelist)
total = 0
for name in sortedlist:
    n = 0
    i = 0
    for letter in str(name):
        n += (ord(letter) - 64)
    n += 60
    i = sortedlist.index(name) + 1
    total += n*i
print(total)
database.close()