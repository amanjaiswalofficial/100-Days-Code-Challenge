num1=input('Enter 1st number:')
num2=input('Enter 2nd number:')
ch=input('Enter the operation symbol(+,-,*,/):')
def calc(var,a,b):
    switcher = {
                '+': a+b, 
                '-': a-b,
                '*': a*b,
                '/': a/b 
    }

    return switcher.get(var,"Invalid Choice")
print('The output is: '+ str(calc(str(ch),int(num1),int(num2))))
