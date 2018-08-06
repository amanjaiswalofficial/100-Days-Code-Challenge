n = int(input())  # no of elements in set
sets = set(map(int, input().split()))  # elements seperated by a space
inputcommand = int(input())  # no of commands
for i in range(inputcommand):
    st=str(input())#taking instruction where first word is the operation and other is count
    s=list(st.split())#splitting the string input to get the command and the set elemnt count
    inpt=set(map(int,input().split()))#storing the input set
    if(s[0] == 'intersection_update'):#if its intersection update
        sets.intersection_update(inpt)
    elif(s[0] == 'update'):#if it's update
        sets.update(inpt)
    elif(s[0] == 'symmetric_difference_update'):#sam logic as above
        sets.symmetric_difference_update(inpt)
    elif(s[0] == 'difference_update'):
        sets.difference_update(inpt)
    """print(inpt)
    print(sets)"""
sum=0
for x in sets:#calculating the sum of all the elements in the set
            sum+=x
print(count)#printing the sum


"""16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
"""
