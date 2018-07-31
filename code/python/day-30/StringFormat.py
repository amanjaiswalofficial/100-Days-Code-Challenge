n=int(input())
binary=[]
for i in range(n+1):
    print((str(i)).rjust(2,' ')+'\t'+(str(oct(i))[2:]).rjust(2,' ')+'\t'+(str(hex(i)).upper()[2:]).rjust(2,' ')+'\t'+(str(bin(i))[2:]).center(5,' '))
