m=int(input('Enter the no. of rows:'))
n=int(input('Enter the no. of columns:'))
a=[[0 for x in range(m)] for y in range(n)]
print('For the matrix of order: '+str(m)+'x'+str(n)+' enter the elements:')

mat = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    mat.append(row)
print('Original matrix:')
for i in range(0,m):
    for j in range(0,n):
        print('%3d'%(mat[i][j]),end=' ')
    print()

temp=0
for i in range(m):
    for j in range(n):
        print(mat[j])


