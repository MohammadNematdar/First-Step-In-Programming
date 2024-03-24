G = int(input('G base: '))
C = int(input('C base: '))
A = int(input('A base: '))
T = int(input('T base: '))

if C - G > 0:
    print('The numbers of extra C:',C-G)
elif C - G < 0:
    print('The numbers of extra G:',G-C)
else:
    print('There is no extra C or G')

if A - T > 0:
    print('The numbers of extra A:',A-T)
elif C - G < 0:
    print('The numbers of extra T:',T-A)
else:
    print('There is no extra T or A')