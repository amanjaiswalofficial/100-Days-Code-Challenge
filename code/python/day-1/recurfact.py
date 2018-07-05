num=int(input('Enter a number to calculate factorial:'))
#below function uses recursion
def fact(a):
    if(a>0):
       #while value of a is greater than 1
       return (a*fact(a-1))
    else:
        #when it finally becomes 1
        return 1
print(fact(num))