n=int(input('Enter Number to convert to Binary:'))
binary=0
a=[]
b=[]
while(n>0):
    rem=int(n%2)#find out the remainder whether its 0 or 1
    a=b.copy()#copy the already existing list of numbers
    b=[]#empty the 2nd list
    b.append(rem)#add the new rem in the beginning
    b.extend(a)#append the existing list to it's end
    n=int(n/2)

for i in range(len(b)):
    print(b[i],end="")
