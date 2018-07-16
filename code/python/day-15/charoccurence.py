string = str(input('Enter the string:'))
occur={}
for i in range(len(string)):#check for every character in the string
    check=string[i]
    count=0
    for j in range(len(string)):#whenever that particular character occurs in the string
        if(string[j]==check):
            count+=1#increment the counter
    if((string[j]) not in occur):
        occur[string[i]]=count#if the key is already not present in the dictionary, add it

for i in occur:#printing the dictionary
        print(str(i)+' occurs '+str(occur[i])+' times')

    
