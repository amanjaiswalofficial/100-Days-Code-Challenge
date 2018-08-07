n=int(input())
lst=list(map(int,input().split()))#input in form of a list
div=int(len(lst)/n)
#print(div)
answer,count=0,0
sets=set(lst)#so that only distinct elements are taken as set
for i in sets:
    #print('i is '+str(i))
    for x in range(len(lst)):#check count of each set element in the list
        if(lst[x]==i):
            #print('i found time: '+str(count+1)+' time')
            count+=1
    if(count==1):#check if it's unique in the whole list
        answer=i#its the answer
    count=0

print(answer)#print the answer