from math import floor
a = int(input('1st number: '))
b = int(input('2nd number: '))
flag = 0
if a > 0 and a == floor(a):
        flag = 1

if b < -3:
    flag = 1

if flag == 1:
    c = b**a
    print(c)
