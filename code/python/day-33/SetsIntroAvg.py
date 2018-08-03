x=set('Hackerrank')
print(x)
x = set(['H', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k'])
print(x)
x = set(set(['H', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']))
print(x)
x = set([1, 2, 1, 2, 3, 4, 5, 6, 0, 9, 12, 22, 3])
print(x)#whenever give entry in sqaure, choose unique ones only
x = set((1, 2, 3, 4, 5, 5))
print(x)#whenever one element, or element in another () then no updation
x.add(6)
print(x)
x.discard(2)
print(x)
"""n=int(input())
lst=[]
sum = 0
for i in range(n):
    lst.append(int(input()))
x=set(lst)
for y in x:
    sum+=y
avg=sum/len(x)
print(avg)"""
