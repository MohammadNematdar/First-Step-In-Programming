from math import floor
n = float(input('n: '))
if n > 0 and n == floor(n):
    n = -n
    print('-n: ',n)
else:
    print('the number that you entered is not natural!!!!')
