lis=[]
n=int(input())
for x in range(n):
    data=str(input())
    command=data.split(' ')
    if(command[0]=='insert'):
        lis.insert(int(command[1]),int(command[2]))
    elif(command[0]=='print'):
        print(lis)
    elif(command[0]=='remove'):
        lis.remove(int(command[1]))
    elif(command[0]=='append'):
        lis.append(int(command[1]))
    elif(command[0]=='sort'):
        lis.sort()
    elif(command[0]=='pop'):
        lis.pop()
    elif(command[0]=='reverse'):
        lis.reverse()
