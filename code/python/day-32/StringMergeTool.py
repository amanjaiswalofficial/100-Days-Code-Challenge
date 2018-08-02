strn=str(input())
n=int(input())
j,temp='',''
lst,final=[],[]
t=0
for i in strn:
    if(t<=n-2):
        temp+=i
        #print(str(t)+': '+temp)
        t+=1
    else:
        temp+=i
        lst.append(temp)
        temp = ''
        t = 0
#print(lst)
for x in lst:
    y=list(x)
    for z in y:
        i=y.index(z)
        y.remove(z)
        if z in y:
            y.remove(z)
        y.insert(i,z)
    z=''.join(x for x in y)
    final.append(z)
for i in final:
    print(i,end='\n')
