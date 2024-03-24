s = 0

for i in range(1000,10000):
    i = str(i)
    two_right_digits = i[2] + i[3]
    i = int(i)
    if int(two_right_digits)%7 == 0:
        s = s + i

print(s)
