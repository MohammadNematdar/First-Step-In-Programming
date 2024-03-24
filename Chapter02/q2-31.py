a = int(input('1st number: '))
b = int(input('2nd number: '))
c = int(input('3rd number: '))

if a%7 == 0 or b%7 == 0 or c%7 == 0:
    m = (a+b+c)/3
    print(m)
else:
    print('non of the entered numbers are divisible to 7')
