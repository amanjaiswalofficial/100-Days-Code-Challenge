def maxMin(operations, x):#operation consist of a list of commands to be performed push and pop
    opn=[]#where as x is the set of all the elements
    inpt=[]
    opn=operations.copy()
    inpt=x.copy()
    sets=set()#output set
    final=[]#final list to output
    for x in range(len(opn)):#loop between the all the operations and elements
        tmp=inpt[x]
        if(opn[x] == 'push'):#if it is push tmp
            sets.add(tmp)
        if(opn[x]=='pop'):#if it is pop tmp
            sets.remove(tmp)
        maxm = max(sets)
        minm = min(sets)
        prod = maxm*minm
        final.append(prod)#adding desired result to the set

    return final#return the final set

