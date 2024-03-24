from math import floor
n = int(input('please enter the 1st number: ' ))
m = int(input('please enter the 2nd number: ' ))

if n >= m:
    Max = n
    Min = m
else:
    Max = m
    Min = n
Remnant = Max - floor(Max/Min)*Min
print(Remnant)
