num=int(input('Enter a number to find it\'s factors:'))
factors=[]
for i in range(1,num+1):
    if(num%i==0):
        factors.append(i)
print(factors)