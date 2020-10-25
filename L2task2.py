aaa = input('vvdite tsifri: ')
bbb = aaa.split()
ccc =[]
if len(bbb) % 2 != 0:
    k = bbb.pop()
    for i in bbb:
        c=bbb.index(i)
        if c % 2 == 0:
            i = bbb[c + 1]
            ccc.append(i)
        elif c % 2 != 0:
            i = bbb[c - 1]
            ccc.append(i)
    ccc.append(k)
    print(ccc)
else:
    for i in bbb:
        c=bbb.index(i)
        if c % 2 == 0:
            i = bbb[c + 1]
            ccc.append(i)
        elif c % 2 != 0:
            i = bbb[c - 1]
            ccc.append(i)
    print(ccc)
