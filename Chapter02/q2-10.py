from math import log,floor
n = int(input('enter a number: '))
digits = floor(log(n,10)) + 1
print('The number of digits of the requested number is: {0}'.format(digits))
