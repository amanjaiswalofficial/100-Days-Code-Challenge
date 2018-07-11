n=int(input('No. of elements:'))
a=[]
for i in range(n):
    a.append(int(input()))
for i in range(n):
    for j in range(0,n-1):
            if (a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]        
print(a)