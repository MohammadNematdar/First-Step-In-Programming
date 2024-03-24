import numpy as np

n = int(input('n: '))
m = int(input('m: '))

l = []
for i in range(n):
    R = int(input('{0}. enter a number: '.format(i)))
    l.append(R)

#print(l)

sub_groups = np.array(np.meshgrid(*[l]*m)).T.reshape(-1,m)
#print(sub_groups)
for i in sub_groups:
    print(i)