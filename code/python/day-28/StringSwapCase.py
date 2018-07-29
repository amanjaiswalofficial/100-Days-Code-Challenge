strin=str(input())
convrt=''

for i in strin:
    if(i.islower()):
        i=str.upper(i)
        convrt+=i
    elif(i.isupper()):
        i=str.lower(i)
        convrt+=i
    else:
        convrt += i

print(convrt)
