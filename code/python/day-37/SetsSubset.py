inputcommand = int(input())  # no of commands
lst=[]
for i in range(inputcommand):
    # taking instruction where first input is no of elements in the set
    st1 = int(input())
    inpt1 = set(map(int, input().split()))  # storing the input set for the first set
    st2=int(input())#count for set 2
    inpt2 = set(map(int, input().split())) #storint the input set for the second set
    if inpt1.issubset(inpt2):# if the first set is subset of second subset
        lst.append('True')#add true to the list
    else:
        lst.append('False')#add false to the list

for x in lst:
    print(x)#print list, containing true and false values

