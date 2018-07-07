n = int(input('Enter the number of elements:'))
arr = []
#taking input from the user
for x in range(n):
    arr.append(int(input()))
b=[]#initializing an empty list
j=0#first index
last = len(arr)#last index
for i in range(len(arr)):
    if(arr[i]!=0):#check if element is not 0, true, then push it to the beginning
        b.insert(j,arr[i])
        j+=1
    elif(arr[i]==0):#if it is 0, push it to the end
        b.insert(last,arr[i])
        last-=1
print('original array: '+str(arr))
print('new array: '+str(b))

