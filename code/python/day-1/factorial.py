num=int(input('Enter a number to find factorial:'))
fact=1
#below repeats a loop each time the value of fact changes, finally saving the result to fact
while(num>0):
    fact*=num
    num-=1
print(fact)