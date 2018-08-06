m = int(input())  # no of elements in first set
x = set(map(int, input().split()))  # elements separated by a space
n = int(input())  # no of elements in 2nd set
y = set(map(int, input().split()))  # elements separated by a space
x = x.difference(y)  # perform difference
count = 0
for i in x:
    count += 1
print(count)  # display count