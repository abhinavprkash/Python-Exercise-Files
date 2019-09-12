fname = input('Enter File: ')
if len(fname)<1 : fname = 'words.txt'
hand =  open(fname)
di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        #oldcount = di.get(w,0)
        #print(w,'old',oldcount)
        #newcount = oldcount +1
        #di[w]= newcount
        #idiom: retieve/create/update centre
        di[w]= di.get(w,0)+1
        #print(w,'newld',di[w])
        #if w in di:
        #    di[w]= di[w]+1
        #    print('**Existing**')
        #else:
        #    di[w]=1
        #    print('**New**')
        #print(w,di[w])

print(di)

#for most common word and its count
largest= -1
for k,v in di.items():
    print(k,v)
    if v > largest :
        largest = v
        theword = k

print(theword,largest)