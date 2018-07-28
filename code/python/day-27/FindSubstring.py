main=str(input())
check=str(input())
l1=len(main)
l2=len(check)
count=0
i=0
print(l1)
print(l2)
for i in range(0,l1-l2+1):
    print('here')
    print('i: '+str(i)+' l2: '+str(l2)+'l1: '+str(l1))
    if(check==main[i:i+l2]):
        count+=1
    
print(count)