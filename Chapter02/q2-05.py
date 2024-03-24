from math import sqrt
a = int(input('enter the 1st triangle\'s side: '))
b = int(input('enter the 2nd triangle\'s side: '))
c = int(input('enter the 3rd triangle\'s side: '))
p = a + b + c
S = sqrt(p*(p-a)*(p-b)*(p-c))
print("The area of the triangle is: ", S)
