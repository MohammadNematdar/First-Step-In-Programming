a = int(input('1st number: '))
b = int(input('2nd number: '))
c = int(input('3rd number: '))
d = int(input('4th number: '))
if a > 0 and b > 0 and c > 0 and d > 0:
    division = (a*b)//(c*d)
    print(division)
else:
    print('one or more of the entered numbers are negative or 0') 
