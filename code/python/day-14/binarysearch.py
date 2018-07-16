def find(arr,a,b,x):
    while(a<=b):#while left index is less than right index
        mid=int(a+ (b-a)/2)#finding middle index for the number
        if(arr[mid] < x):#if number is less than middle element, then look in the first half of sorted array
            a=mid+1
        elif(arr[mid] > x):#if number is greater than middle element, look in the second half
            b=mid-1
        elif(arr[mid] == x):#if element found, return position
            return mid
    return -1#if not found anywhere in the array, return -1

n=int(input('Enter no. of elements:'))
arr=[]
sortedarr=[]
for i in range(n):
    arr.append(int(input()))

x=int(input('Enter number to search in the array:'))
print(arr)
#creating a copy of the original array
sortedarr=arr.copy()
sortedarr.sort()#sorting it
i=find(sortedarr,0,n-1,x)
if(i==-1):#element wasnt found
    print('Element not found')
else:#found, then it's location in the original array
    print('Element found at position: '+str(int(arr.index(x))+1))
