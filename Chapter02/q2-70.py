from math import floor,factorial
N = float(input('Please enter a natural number: '))

while not (N > 0 and N == floor(N)):
           N = int(input('the number must be natural!!!: '))

s = 0
for i in str(int(N)):
    #print(i)
    s = s + pow(int(i),3)

if s == N:
    print(' the number you entered is ARMSTRONG!')
else:
    print('the number you entered isn\'t armstrong')
    
    
