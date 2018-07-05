import random
def questionans():
    #taking 2 random numbers between 1 to 100
    num1=int(round(random.uniform(0, 1),2)*100+1)
    num2=int(round(random.uniform(0,1),2)*100+1)
    #taking a number between 1 to 5 to select one out of 5 operations
    #meaning between + * - / and %
    op = int(round(random.uniform(0, 1), 2)*5+1)
    if(op==1):#if op is +
        ans=int(num1+num2)
        opn='+'
    elif(op==2):#if op is *
        ans=int(num1*num2)
        opn='*'
    elif(op == 3):  # if op is -
        ans=int(num1-num2)
        opn='-'
    elif(op == 4):  # if op is /
        ans=int(num1/num2)
        opn='/'
    elif(op == 5):  # if op is %
        ans=int(num1%num2)
        opn='%'
    print('Q- '+str(num1)+' '+opn+' '+str(num2)+'?')#printing the question to user
    user=int(input('A- '))#taking user answer
    if(user==ans):#if user's answer is correct
        print('Correct Answer\n')
        questionans()
    else:
        print('Incorrect\n')#if the user's answer is incorrect
        questionans()

questionans()#calling method for the first time
