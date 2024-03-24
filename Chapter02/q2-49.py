m = int(input('m: '))
n = int(input('n: '))
k = int(input('k: '))
s = 0
if n >= m:
    Max = n
    Min = m + 1
else:
    Max = m
    Min = n + 1

for i in range(Min,Max):
    if i%k == 0:
        s = 0
        for j in range(1,i):
            if i%j == 0:
                s = s + j
        if s == i:
            print(i)
        
