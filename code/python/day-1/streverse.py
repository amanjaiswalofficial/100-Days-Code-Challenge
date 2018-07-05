text=input('Enter a string:')
reverse=''
#to perform reverse of the string
#in range, first 2 arg define the range of values to be used, and the last determines the op to be performed
for i in range(len(text)-1,-1,-1):
    reverse+=text[i]
print(reverse)