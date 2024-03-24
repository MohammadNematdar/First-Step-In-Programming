from math import floor
N = float(input('Please enter a natural number: '))

while not (N > 0 and N == floor(N)):
           N = int(input('the number must be natural!!!: '))
index = -1
varoon = ''
N = str(N)
for i in range(len(N)):
    varoon = varoon + N[index]
    index -= 1
print(varoon)
