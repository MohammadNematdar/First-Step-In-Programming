
while True:
    n = int(input('Please enter a number (n <= 9): '))
    if n > 0 and n <= 9:
        break

s = ''
counter = 0
c = 1
while counter < n:
    m = input('{0}.Please enter a number between 1 to 9: '.format(c))
    if int(m) <= 0:
        pass
    else:
        s = s + m
        counter += 1
        c += 1
l = []
for i in s:
    for j in s:
        for p in s:
            if i != j and i != p and j != p:
                l.append(i+j+p)


print(l)