# x2 - x1 = 1/2at^2 + v0t
v0 = int(input('initial Velocity: '))
t = int(input('time: '))
a = int(input('acceleration: '))
n = int(input('n: '))
x = 0.5*a*n*(2*t - n) + v0*n
print(x)
