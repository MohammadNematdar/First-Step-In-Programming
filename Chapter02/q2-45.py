counter = 0
s = 0
for i in range(999,99,-1):
    if i%7 == 0:
        s = s + i
        counter = counter + 1
    if counter == 20:
        break

print(s)
