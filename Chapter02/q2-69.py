from math import floor,factorial
N = float(input('Please enter a natural number: '))

while not (N > 0 and N == floor(N)):
           N = int(input('the number must be natural!!!: '))

l = []
N = str(N)
for i in range(0,len(N)-2):
    l.append(N[i])
#print(l)
fac = 0
for i in l:
    #print(i)
    fac = fac + factorial(int(i))
print(fac)
