n=int(input('No. of elements:'))
a=[]
for i in range(n):
    a.append(int(input()))
min=a[0]
for i in range(n):
    if(a[i]<min):
        j=i
    a[a.index(min)],a[j]=a[j],a[a.index(min)]  
print(a)
//