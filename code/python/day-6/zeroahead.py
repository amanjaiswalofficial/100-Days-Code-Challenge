n = int(input('Enter the number of elements:'))
arr = []
#taking input from the user
for x in range(n):
    arr.append(int(input()))
b=[]
j=0#first index
last = len(arr)#last index
for i in range(len(arr)):
    if(arr[i]==0):#if the element is 0, then push it in the beginning
        b.insert(j,arr[i])
        j+=1
    elif(arr[i]==1):#if the element is 1, then push it to the end
        b.insert(last,arr[i])
        last-=1
print('original array: '+str(arr))
print('new array: '+str(b))

