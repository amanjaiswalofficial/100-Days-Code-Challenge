s=str(input())
l = len(s)
sample = []
lst = []
stscore = 0
kvscore = 0
strn = ''
for i in range(0, len(s)):
    for j in range(0, i+1):
        letter = s[j:i+1]
        sample.append(letter)
        if letter not in lst:
            lst.append(letter)
for i in lst:
    strn = i
    if(strn[0] in {'A', 'E', 'I', 'O', 'U'}):
        kvscore += sample.count(strn)
    else:
        stscore += sample.count(strn)
if(stscore > kvscore):
    print('Stuart '+str(stscore))
elif(stscore < kvscore):
    print('Kevin '+str(kvscore))
else:
    print('Draw')