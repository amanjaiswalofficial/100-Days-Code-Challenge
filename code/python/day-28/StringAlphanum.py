"""Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
str.isalnum() return true or false based on it
other methods: isupper() islower() isalpha() isdigit()"""
s1=s2=s3=s4=s5=False
strin=str(input())
for i in strin:
    
    if(i.isalnum()):
        s1=True
    if(strin.isalpha()):
        s2=True
    if(strin.isdigit()):
        s3=True
    if(strin.islower()):
        s4 = True
    if(strin.isupper()):
        s5 = True
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
