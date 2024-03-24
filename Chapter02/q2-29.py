from math import sqrt
x = int(input('1st number: '))
y = int(input('2nd number: '))
z = int(input('3rd number: '))

x0 = 0
y0 = 0
z0 = 0
d = sqrt((x - x0)**2 + (y - y0)**2 + (z - z0)**2)

if d > 10:
    z_axis = sqrt(x**2 + y**2)
    print(z_axis)
else:
    print('the distance is below 10')
