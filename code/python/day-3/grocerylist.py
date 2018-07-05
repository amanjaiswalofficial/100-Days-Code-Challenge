names=[]
amounts=[]
flag=False
file = open('grocery.txt', 'w+')#opening a file
n=int(input('No of items:'))#taking input for no of items to be stored
print('Enter the item names and their amount in KG:')
for i in range(0,n):#taking input in form of item name and then it's amount in kg
    name=str(input())
    names.append(name)
    amount=int(input())
    amounts.append(amount) 
    #for each successful entry, saving it to the file
    file.write(names[i]+' => '+str(amounts[i])+'KG\n')

file.close()
#reading the file and saving it in a list, line by line
file=open('grocery.txt','r')
if(file.mode=='r'):
    #content=file.read()
    f1=file.readlines()

#asking user to provide item name to search    
search=str(input('Enter the item to search:'))
#searching the lines whether it contains user's provided item
for i in range(0,len(f1)):
    #if item found
    if search in f1[i]:
        index=i
        flag=True
        break;
if(flag):
    #if item was found, then printing it's amount from the file
    print(str(amounts[index])+' KG')
else:
    #if item not found then,output 
    print('Item not in the file.')

file.close()
