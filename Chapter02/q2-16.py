# xr = ((v^2)* sin(2a))/g # range
# xm = ((v^2)*(sin(a)^2))/g # peak
# https://article.tebyan.net/252933/%D9%85%D8%AD%D8%A7%D8%B3%D8%A8%D9%87-%D9%85%D8%AE%D8%AA%D8%B5%D8%A7%D8%AA-%D9%86%D9%82%D8%B7%D9%87-%D8%A7%D9%88%D8%AC
from math import sin,radians
v = int(input('v: '))
a = int(input('a: '))
g = 9.8
xr = ((v**2)* sin(2*radians(a)))/g
xm = ((v**2)*(sin(radians(a))**2))/(2*g)

print('xr: {0}, xm: {1}'.format(xr,xm))
