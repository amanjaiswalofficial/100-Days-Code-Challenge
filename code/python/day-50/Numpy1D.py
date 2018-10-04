import numpy as np
a=np.array([0,1,2,3,4])

print(a)#prints the numpy array a

print(type(a)) #returns numpy array
print(a.dtype) #this shows the kind of value stored

b=np.array([1,1.1,2,2.2,3])
print(b.dtype) #returns float as it contains decimal vals as well

#similar functionalities

c=np.array([2,4,6,8,10])
c[2]=5
print(c)
d=c[1:4]
print(d)
d[1:3]=10,20
print(d)

#attributes of a numpy array
print(c.size)
print(c.shape)
print(c.mean())

#array operations
u=np.array([1,0,3])
v=np.array([3,4,1])
w=u+v#adding
print(w)
w=u-v#subtracting
print(w)
w=2*u#multiplying a scaler
print(w)
w=u*v#notmal product
print(w)
w=np.dot(u,v)#dot product
print(w)
w=u+1#adding a scaler number
print(w)

#linespace
#provides a set of values between 1st arg and 2nd arg, with divisions equal to 3rd arg
print(np.linspace(-5,5,num=5))