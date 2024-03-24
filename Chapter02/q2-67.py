
num = input('Please enter a number: ')
num = num.replace(',','.')
num = num.split('.')


print(num)
counter = 0
for i in num[1]:
    counter -= 1
    if int(i) % 2 == 0:
        print(i,10**(counter))
