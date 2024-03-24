sum_3_digits = 0
counter = 0
for i in range(100,1000):
    sum_3_digits = sum_3_digits + i
    counter = counter + 1
mean = sum_3_digits/counter
print(mean)
