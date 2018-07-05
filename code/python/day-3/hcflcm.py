a=[]
for i in range(1, 5):
    a.append(int(input()))

#function to calculate hcf of 2 numbers
def hcf(a,b):
    for i in range(1,max(a,b)+1):
        if (a%i==0 and b%i==0):
            gcd=i
    return gcd

#function to calculate lcm of 2 numbers
def lcm(a, b):
    gcd = hcf(a,b)
    lcms = (a*b)/gcd
    return int(lcms)

hcfs=lcms=a[0]
#calling the above 2 functions to calculate hcf and lcm for the whole set of 4 numbers
#here, both are calculated for 2 numbers at once
#where one is the new number from the list and other is the hcf/lcm from previous set of 2 numbers
for i in range(0,len(a)):
    hcfs=hcf(hcfs,a[i])
    lcms=lcm(lcms,a[i])

#printing the output
print('HCF: '+str(hcfs))
print('LCM: '+str(lcms))

