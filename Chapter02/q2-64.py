num = input("please enter a number: ")
num = num.replace(',','.')

sign = '+'
if num[0] == '-':
    num = num.replace('-','')
    sign = '-'
n = num.split('.')
decimals = len(n[1])
digits = len(n[0])
print('Sign: ',sign)
print('Decimals: ',decimals)
print('Digits: ',digits)
