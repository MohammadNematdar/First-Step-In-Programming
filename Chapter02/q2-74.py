i = int(input('enter a number: '))
j = int(input('enter another number: '))
while True:
    x = input("Please enter the operator: \n Addition = a, Subtraction = s, Multiple = m, Division = d: ")
    if (x.upper() == "M") or (x.upper() == "S") or (x.upper() == "A") or (x.upper() == "D"):
        break
if x.upper() == "M":
    M = i*j
    print(M)
elif x.upper() == "S":
    S = i - j
    print(S)
elif x.upper() == "A":
    A = i + j
    print(A)
elif x.upper() == "D":
    try:
        D = i/j
        print(D)
    except ZeroDivisionError:
        print( 'you entered zero for Divisor and you have ZeroDivisionError!')

        
