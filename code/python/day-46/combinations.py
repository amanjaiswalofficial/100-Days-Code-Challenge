from itertools import combinations
x=[]
result=[]
strn=list(map(str,input().split()))
length=strn[1]
string=strn[0]
for i in range(1,3):
    x.extend(list(combinations(string,i)))
for i in x:
    strn=''
    for j in i:
        strn=strn+j
    result.append(strn)
result.sort()

for j in range(1,int(length)+1):
    tmp=[]
    for i in result:
        if(len(i)==j):
            tmp.append(i)
    tmp.sort()
    for x in tmp:
        print(x)