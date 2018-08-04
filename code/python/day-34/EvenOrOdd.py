n = int(input())#no of elements to be stored
lst = []
lstodd = []
lsteven = []
for i in range(n):#store em in a list
    lst.append(int(input()))
for i in lst:#divide into 2 lists, one with even index elements and one with odd
    if((lst.index(i)) % 2):
        lsteven.append(i)
    else:
        lstodd.append(i)

reven, rodd = lsteven[0], lstodd[0]
count = False
for i in lstodd[1:]:#perform multiply once and add the other time and so on to the result val
    if(not(count)):
        rodd *= i#multiply the result
        count = True
    else:
        rodd += i#add the result
        count = False

count = False
for i in lsteven[1:]:#save with the even list
    if(not(count)):
        reven *= i
        count = True
    else:
        reven += i
        count = False
reven,rodd=rodd,reven
reven=reven%2
rodd=rodd%2
if(reven>rodd):#if even sum is greater than odd sum, print even or else odd
    print('EVEN')
else:
    print('ODD')