n = int(input('1st number: '))
m = int(input('2nd number: '))

if n > m:
    Max = n
    Min = m + 1
else:
    Max = m
    Min = n + 1

for i in range(Min,Max):
    if i%7 == 0:
        print(i)
