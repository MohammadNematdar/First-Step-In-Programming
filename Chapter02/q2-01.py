from math import pi
a = int(input('enter the radius hemisphere: '))
area = 0.5*(4*pi*(a**2)) + pi*(a**2)
volume = 0.5*(4/3)*pi*(a**3)
print("The Volume of the hemisphere is {0} and the area is {1}".format(volume,area))

