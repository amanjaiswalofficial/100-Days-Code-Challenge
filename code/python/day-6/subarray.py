n=int(input('Enter the number of elements:'))
arr=[]
#taking input from the user
for x in range(n):
    arr.append(int(input()))
#initializing a list of list, for storing all the subarrays of array
combine=[[]]

for i in range(len(arr)):
    for j in range(i+1,len(arr)+1):
        sub=arr[i:j]
        combine.append(sub)

#checking in each subarray whether sum of it's elements is 0, if yes, print the subarray
for row in combine:
    sum = 0
    for l in range(len(row)):
        #going from 1st element in the subarray to the last, adding em to find the sum
        sum+=row[l]
    if(sum == 0  and len(row)>0):
        print(row)

