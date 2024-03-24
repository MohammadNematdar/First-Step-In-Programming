from random import random

l = 0.25
r = 0.5
u = 0.75
d = 1.0
X = 0
Y = 0
while pow(Y**2 + X**2,0.5) <= 4:
    rand = random()
    #print(rand)
    if rand <= l:
        X -= 1
    elif l < rand and rand <= r:
        X += 1
    elif r < rand and rand <= u:
        Y += 1
    elif rand > u:
        Y -= 1

print('X: ', X, 'Y: ', Y)
