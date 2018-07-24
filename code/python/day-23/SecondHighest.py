if __name__ == '__main__':
    n = int(input('Enter no. of elements: '))
    arr=[]
    for i in range(0,n):
        arr.append(int(input()))
    high=sechigh=-32768

    for i in range(len(arr)):
        if(high<arr[i]):
            high=arr[i]
            print('Now high is '+str(high))
    for i in range(len(arr)):
        if(sechigh<arr[i] and arr[i]!=high):
            sechigh=arr[i]
    print(str(sechigh))