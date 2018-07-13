n=int(input('Enter Number to convert to Binary:'))
binary=0
while(n>1):
    rem=n%2
    binary=binary*10+1
    n=n/2
print(binary)