from statistics import median
a = int(input('1st number: '))
b = int(input('2nd number: '))
c = int(input('3rd number: '))

greatestnum = str(max(a,b,c)) + median([str(a),str(b),str(c)]) +str(min(a,b,c))

print(int(greatestnum))
