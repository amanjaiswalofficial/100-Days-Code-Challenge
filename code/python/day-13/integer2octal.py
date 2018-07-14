n=int(input('Enter number to convert into octal:'))

temp=[]
b=[]
i=0
while(n>0):#dividing continuously by 8, and adding remainder to the answer list
    rem=int(n%8)
    temp=b.copy()
    b=[rem]
    b.extend(temp)
    n=int(n/8)
for i in range(len(b)):
    print(b[i],end='')