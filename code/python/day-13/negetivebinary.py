import sys
n = int(input('Enter Number to convert to Binary:'))
binary = 0
a = []
b = []
flag=True
copy=n

def printfile(b):
    for i in range(len(b)):
        print(b[i], end="")

if(n>=0):#if number is positive then no change in process, simply convert
    while(n>0):
        rem=int(n%2)#find out the remainder whether its 0 or 1
        a=b.copy()#copy the already existing list of numbers
        b=[]#empty the 2nd list
        b.append(rem)#add the new rem in the beginning
        b.extend(a)#append the existing list to it's end
        n=int(n/2)
    printfile(b)

else:#if number is negetive, then
    n=abs(n)#take the original number
    while(n > 0):#convert it into binary
        rem = int(n % 2)  # find out the remainder whether its 0 or 1
        a = b.copy()  # copy the already existing list of numbers
        b = []  # empty the 2nd list
        b.append(rem)  # add the new rem in the beginning
        b.extend(a)  # append the existing list to it's end
        n = int(n/2)

    if(abs(copy)<256):#if binary is less than 8 digits, then append 0's in the beginning to make it 8 digit binary
        temp=[0]*(8-len(b))
    else:#if binary is greater than 8 digits, append remaining 0 to make it 16 digit binary
        temp=[0]*(16-len(b))
    x = b
    b = temp   
    for y in range(len(x)):
        b.append(x[y])


    #finding the one's compliment
    comp = []
    for i in range(len(b)):
        if(b[i]==0):
            comp.append(1)
        elif(b[i]==1):
            comp.append(0)



    def add(a, i):
        if(a[i] == 0):
                a[i] = 1
                printfile(a)
                sys.exit()
        elif(a[i]==1 and i!=len(a)):
                a[i]=0
                add(a,i-1)
    
    #adding 1 to the compliment to make it 2's compliment
    def addone(a):
        for i in range(len(a)-1, -1, -1):
            add(a,i)
            
    addone(comp)




