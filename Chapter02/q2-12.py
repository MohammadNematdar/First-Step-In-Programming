from math import pow
x = int(input("x: "))
print('f = x**3 + 1/(2*(x**(1/2))) + (4/7)(x**(1/3))')
f = x**3 + 1/(2*(pow(x,1/2))) + (4/7)*(pow(x,1/3))
fof = f**3 + 1/(2*(pow(f,1/2))) + (4/7)*(pow(f,1/3))     
print(fof)
