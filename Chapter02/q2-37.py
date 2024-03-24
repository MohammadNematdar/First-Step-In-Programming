n = int(input('n: '))
sum0 = 0
counter = 0
for i in range(n):
    number = int(input('enter number: '))
    sum0 = sum0 + number
    counter = counter + 1
mean = sum0 / counter
print(mean)
