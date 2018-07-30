strin=str(input())
num=int(input())
count = 0
for i in strin:
    while(count<=num-1):
        if(count<num-1):
            print(i,end='')
            count+=1
            break
        elif(count==num-1):
            print(i,end='')
            print()
            count=0
            break
    
