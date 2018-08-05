n = int(input())#no of elements in set
sets = set(map(int, input().split()))#elements seperated by a space
#val=str(input())
command = []
inputcommand = int(input())#no of commands
for i in range(inputcommand):
    command.append(str(input()))#storing commands in a list
for x in command:
    t = x.split(' ')#splitting each command to check 1st word
    if(t[0] == 'pop'):#if first word is pop
        sets.pop()
    elif(t[0] == 'remove'):#if first word is remove
        sets.remove(int(t[1]))
    elif(t[0] == 'discard'):#if first word is discard
        sets.discard(int(t[1]))
    print(sets)
if(sets):#if set is not empty
    sum=0    
    for i in sets:
        sum+=i
    print(sum)#print the sum
else:
    print(0)#print 0



