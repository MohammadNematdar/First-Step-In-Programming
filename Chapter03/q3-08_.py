import numpy as np

n = int(input('n: '))
m = int(input('m: '))

arr_n = np.zeros((n,))
for i in range(n):
    arr_n[i] = int(input('{0}. enter a number: '.format(i)))

print(arr_n)

sub_groups = np.array(np.meshgrid(*[arr_n]*m)).T.reshape(-1,m)
for i in sub_groups:
    print(i)