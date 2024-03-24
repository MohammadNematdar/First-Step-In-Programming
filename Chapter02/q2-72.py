from math import floor
a = float(input('please enter a number: '))
while not (a > 0 and a == floor(a)):
           a = int(input('the number must be natural!!!: '))

b = float(input('please enter another number: '))
while not (b > 0 and b == floor(b)):
           b = int(input('the number must be natural!!!: '))
a = int(a)
b = int(b)



if a >= b:
    Max = a
    Min = b
else:
    Max = b
    Min = a
l = []
M = 0
for i in range(Max):
    M = M + Max
    l.append(M)
#print(l)
m = 0
flag = 0
for j in range(Max):
    if flag == 1:
        break
    m = m + Min
    for p in l:
        if m == p:
            print(m)
            flag = 1
            break
