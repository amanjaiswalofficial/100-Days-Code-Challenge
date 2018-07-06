principle=float(input('Enter the principle amount:'))
rate=(float(input('Enter the rate (in %):')))/100
time=int(input('Enter the time in years:'))
nooftime=int(input('No. of times it\'s compounded per year:'))
intst=principle*((1+rate/nooftime)**(nooftime*time)) - principle
print('Compound interest (excluding principle amount) is: ₹'+str(intst))
