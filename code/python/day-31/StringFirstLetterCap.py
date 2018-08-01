x=str(input())
dcn={}
for i in range(len(x)):
    if(i==0 or x[i-1]==' '):
        dcn[i]=x[i].upper()
finalstr=''       
for j in range(len(x)):
    if (j in dcn.keys()):
        finalstr+=dcn[j]
    else:
        finalstr+=x[j]
print(finalstr)