import sys

n=int(input('Enter no. of terms:'))
a=[]
for i in range(n):
    a.append(int(input()))
#sort the list
a.sort()
num=0
for i in range(n):#going through each element
    if(a[i]==num):
        num+=1#if every num value is present in the list, inc the value of num
    else:
        print('\n'+'Missing Term:'+str(num))#if any num value is not in the list, then print it and exit
        sys.exit()#function to exit
print('\n'+'Missing Term:'+str(num))#if all the elements are present from 0 to n-1, meaning n is the next missing element, hence print it
