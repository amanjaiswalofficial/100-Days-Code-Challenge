n=int(input('No. of elements:'))
a=[]
for i in range(n):
    a.append(int(input()))
for i in range(1, n):
    k = a[i]
    j = i-1
    while(j >= 0 and a[j] > k):
        a[j+1] = a[j]
        j -= 1
    a[j+1] = k
print(a)
