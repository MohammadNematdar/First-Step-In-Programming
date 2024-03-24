

for i in range(100,1000):
    flag = 0
    for j in range(2,i):
        if i%j == 0:
            flag = 1
            break
    if flag == 0:
        i = str(i)
        p = int(i[2]) + int(i[1])
        if p < 9:
            print(i)
