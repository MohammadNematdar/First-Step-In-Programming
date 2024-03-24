length = int(input('enter length in cm: '))
if length > 30:
    length_feet = length*0.0328084
    print(length_feet)
else:
    length_inches = length*0.393701
    print(length_inches)
