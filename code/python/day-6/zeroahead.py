n = int(input('Enter the number of elements:'))
arr = []
#taking input from the user
for x in range(n):
    arr.append(int(input()))
b=[]
j=0
last = len(arr)
for i in range(len(arr)):
    if(arr[i]==0):
        b.insert(j,arr[i])
        j+=1
    elif(arr[i]==1):
        b.insert(last,arr[i])
        last-=1
print('original array: '+str(arr))
print('new array: '+str(b))

