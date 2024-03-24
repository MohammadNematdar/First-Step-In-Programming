a = int(input('1st side: ' ))
b = int(input('2nd side: ' ))
c = int(input('3rd side: ' ))
if a == b or b == c or a == c:
    print('this is an isosceles triangle')
else:
    print('it isn\'t isosceles triangle')
