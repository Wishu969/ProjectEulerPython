main = []
for m in range(97,123):
    main.append(m)
#69 is space 32
for x in [69]:
    t = []
    for a in range(97,123):
        c = x ^ a
        if (c > 64 and c < 91) or (c > 96 and c < 123):        
            t.append(a)
    poplist = []
    for i in range(len(main)):
        if main[i] not in t:
            poplist.append(i)
    popped = 0
    for a in poplist:
        a -= popped
        main.pop(a)
        popped+=1

print(*main)
for a in range(97,123):
    pass
    #print(chr(69^a))
print(69^101)
#print('test'+chr(1)+'TEST')