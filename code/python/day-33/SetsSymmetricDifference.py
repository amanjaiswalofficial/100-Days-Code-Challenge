"""a=str(input())
lis=a.split(' ')
newlis=list(map(int,lis))
print(newlis)

#creating sets
#initializing:
myset=set()
myset1=set(['a','b','c','a'])
print(myset1)
myset1.add('a')#cant add existing element
print(myset1)
myset1.add(('a'))#no matter what, doesn't accept repeating element
print(myset1)
myset1.add((5,4))
print(myset1)

#update
myset1.update((1,2,3,4))
print(myset1)
myset1.update({1,7,8})
print(myset1)

#removing element
myset1.remove((5,4))
print(myset1)
#myset1.discard() #is similar to remove but doesnt return error if doesnt find anything to delete

set1=set((1,2,3,4))
set2=set((2,4,6,8))
print(set1)
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

#calculating symmetric difference
a=set([2,4,5,9])
b=set([2,4,11,12])
print(a.union(b) == b.union(a))
print(a.intersection(b)==b.intersection(a))
print(a.difference(b)==b.difference(a))"""

x=int(input())
a=set((input().split(' ')))
y=int(input())
b = set((input().split(' ')))
c=list(a.difference(b))
c.extend(list(b.difference(a)))
d=list(map(int,c))
d.sort()
for i in d:
    print(i,end='\n')
