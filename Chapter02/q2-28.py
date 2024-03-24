from math import sqrt
x = int(input('please enter a number:  '))
if x<= 1:
    f = x**2 -4
elif 1 < x and x <= 4:
    f = 3*x + 2
else:
    f = sqrt(x)/5
print(f)
