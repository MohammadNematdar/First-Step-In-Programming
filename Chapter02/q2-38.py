n = int(input('m: '))
m = int(input('n: '))
if n >= m:
    Max = n
    Min = m+1
else:
    Max = m
    Min = n+1
sum0 = 0
counter = 0

for i in range(Min,Max):
    sum0 = sum0 + i
    counter = counter + 1
mean = sum0 / counter
print(mean)
