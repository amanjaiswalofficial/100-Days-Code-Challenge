num=str(input())
val=num.split(' ')
m=val[0]
n=val[1]
for i in range(m):
    for j in range(n):
        if(j<(n/2-1)) or j>(n/2+1)):
            print('-')
        elif(j<n/)