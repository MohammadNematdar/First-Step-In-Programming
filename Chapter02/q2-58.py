s = 0
counter = 0
while True:
    n = int(input('please enter a number: '))
    if n == 0:
        break
    else:
        counter = counter + 1
        s = s + n

mean = s/counter
print('mean: {0}',format(mean))
