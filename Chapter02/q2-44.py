N = int(input('N: '))

a_soorat = 1
a_makhraj = 0
s = 0
for i in range(1,N+1):
    a_makhraj = a_makhraj + i
    s = s + a_soorat/a_makhraj

print(s)
