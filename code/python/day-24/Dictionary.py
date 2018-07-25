import math
dictn={}
name=''
n=int(input())
for x in range(n):
    name=str(input())
    phy=float(input())
    chem=float(input())
    maths=float(input())
    totalavg=float(phy+chem+maths)/3
    dictn[name]=totalavg
uinput=str(input())
for x in dictn:
    if(x==uinput):
        print(float(dictn[x]))
    