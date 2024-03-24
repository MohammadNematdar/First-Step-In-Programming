
for i in range(100,1000):
    i = str(i)
    yekan = int(i[2])
    sadgan = int(i[0])
    if abs(sadgan - yekan) < 3:
        print(int(i))
