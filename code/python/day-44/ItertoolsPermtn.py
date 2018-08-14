from itertools import permutations
"""#print(list(permutations([1,2,3])))

lst=list(map(int,input().split()))
app=[]
for count in range(len(lst)):
    if(count==0):
        temp=list(permutations(lst,0))
        xtra=list((i for i in temp).split(','))
        print(xtra)
    else:
        temp=(list(permutations(lst,count+1)))
        app.extend(temp)
print(app)"""
final=[]#to store the final output
inpt=list(map(str,input().split()))#to take input seperated by space one is the string other count
num=int(inpt[1])#to get the count
sample=list(permutations(inpt[0],num))#to permutate the input string based on the count
for i in sample:
    tmp=''
    for j in i:
        tmp+=j#combine the letters of each element
    final.append(tmp)#append the results to the final answer
for i in final:
    print(i,end='\n')#print the final output
