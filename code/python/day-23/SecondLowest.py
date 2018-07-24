if __name__ == '__main__':
    num = int(input())
    name = []
    score = []
    for i in range(0, num):
        name.append(input())
        score.append(float(input()))

    low = seclow = float(32768)
    for i in range(len(score)):
        if(score[i] < low):
             low = score[i]

    for i in range(len(score)):
        if(score[i] < seclow and score[i] > low and seclow != low):
            seclow = score[i]
    names=[]
    for i in range(len(name)-1,-1,-1):
        if(score[i] == seclow):
            names.append(name[i])
        
    names.sort()
    for i in range(len(names)):
        print(names[i])
            
