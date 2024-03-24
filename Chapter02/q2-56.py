from random import random
n = int(input('tedaad gam ha: '))
L = 0.25 # shift to left
R = 0.5  # shift to right
U = 0.75 # shift to up
D = 1    # shift to down
X = 0
Y = 0
for i in range(1,n+1):
    r = random()
    print(r)
    if r < L:
        X = X - 1
    elif r > L and r < R:
        X = X + 1
    elif r > R and r < U:
        Y = Y + 1
    elif r > U:
        Y = Y - 1
print('[',X,Y,']')
