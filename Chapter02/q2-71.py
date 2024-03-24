a = int(input('مقسوم: '))
b = int(input('مقسوم عليه: '))
counter = 0
while a >= b:
    a = a - b
    counter += 1
print(counter)
    
