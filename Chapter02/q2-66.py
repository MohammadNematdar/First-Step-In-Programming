num = input('Please enter a number: ').split('.')
num = "".join(num)
num = num.split(',')
num = "".join(num)
counter = 0
for i in num:
    if int(i)%2 == 0:
        #print(i)
        counter += 1
    
print(counter)