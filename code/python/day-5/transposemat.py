m=int(input('Enter the no. of rows:'))
n=int(input('Enter the no. of columns:'))
a=[[0 for x in range(m)] for y in range(n)]
b = [[0 for x in range(n)] for y in range(m)]
print('For the matrix of order: '+str(m)+'x'+str(n)+' enter the elements:')

#taking input from the user for the matrix of order m*n
mat = []
for i in range(m):
    row = []#list inside list for a 2-D matrix
    for j in range(n):
        row.append(int(input()))#append the input to the column list
    mat.append(row)#append the column list to the row

for row in mat:
    print(row)#row by row printing of the original matrix

#NOTES TO SELF
"""below is the logic for swapping and storing in a new matrix as transpose of the original matrix
in the inner list, the value will range between 0 to the row val, and in the outer list, it will
range from 0 to the max col val
so, the assignment take place as [0][0],[1][0],[2][0]..[0][1],[1][1],[2][1] and so on
"""
print('\nTransposed matrix:')
res = [[mat[j][i] for j in range(m)] for i in range(n)]
for row in res:
    print(row)

