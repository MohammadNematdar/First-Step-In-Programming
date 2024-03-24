n = int(input('1st number: '))
m = int(input('2nd number: '))
k = int(input('mazrab morede nazar: '))

if n > m:
    Max = n
    Min = m + 1
else:
    Max = m
    Min = n + 1

for i in range(Min,Max):
    if i%k == 0:
        print(i)
        
