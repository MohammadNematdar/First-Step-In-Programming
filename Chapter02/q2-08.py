from math import sqrt,pi
a = int(input('enter the 1st side of the triangle: '))
b = int(input('enter the 2nd side of the triangle: '))
c = int(input('enter the 3rd side of the triangle: '))
p = a + b + c
A = sqrt(p*(p-a)*(p-b)*(p-c))
R = (a*b*c)/(4*A)# the radius of peripheral circle
area = pi*(R**2)
perimeter = 2*pi*R
print("perimeter: {0}, area: {1}".format(perimeter,area))
