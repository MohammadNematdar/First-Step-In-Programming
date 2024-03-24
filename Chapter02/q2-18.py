from math import cos,sin

m = float(input('jerm jesm: '))
jahat = input('jahate harkate jesm:(bala or paen) ')
u = float(input('zarib estehkak jonbeshi jesm: '))
alpha = float(input("zavie sathe shibdar: "))
g = 9.8
if jahat == 'bala':
    a = -g*(sin(alpha) + u*(cos(alpha)))
else:
    a = g*(sin(alpha) - u*(cos(alpha)))

print('shetabe jesm barabar ba {:2f} ast.'.format(a))