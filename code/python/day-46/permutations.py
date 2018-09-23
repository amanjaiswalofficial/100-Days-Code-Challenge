from itertools import permutations
lists=list(map(str,input().split()))
num=int(lists[1])
strn=lists[0]
final=list(permutations(strn,2))
finalist=list()
for i in final:
    tmp=i[0]+i[1]
    finalist.append(tmp)
finalist.sort()
for x in finalist:
    print(x)
