x=set(map(int,input().split()))#original set
lst=[]
flag=True
num=int(input())#no of subsets to check that whether x is their superset
for i in range(num):
    sets=set(map(int,input().split()))#storing one set at a time
    lst.append(sets)#appending that whole set in a list as its element
for y in lst:
    if(not(x.issuperset(y))):#if for any subset x is not the superset, turn flag to false
        flag=False
    print(str(lst.index(y))+': '+str(flag))#print status of flag after each operation
print(flag)#print final flag value