database = open("databaseWords","r")
wordlist = database.readline().split(',')
print(wordlist[0])
