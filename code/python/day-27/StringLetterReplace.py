s=str(input())
ch=str(input())
choice=ch.split(' ')
ssplit=list(s)
for i in range(len(ssplit)):
    if(i+1==int(choice[0])):
        ssplit[i]=str(choice[1])
final=''.join(x for x in ssplit)
print(final)