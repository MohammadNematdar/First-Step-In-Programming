n = int(input('n: '))
r = float(input('r: '))
a1 = float(input('a1: '))

for i in range(1,n+1):
    s = a1*((1 - r**n)/(1-r))
print(s)
