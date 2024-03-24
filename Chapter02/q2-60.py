import decimal
x = -1
while x <= 0:
    x = int(input('the number should be greater than 0: '))

while x >= 0.2:
    x = float(decimal.Decimal(str(x)) - decimal.Decimal(str(0.2)))
    print(x)
