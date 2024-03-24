n = int(input('enter the number: '))

a1_soorat = 2
a1_makhraj = 3
sum0 = 0
for i in range(1,n+1):
    sum0 = sum0 + a1_soorat/a1_makhraj
    a1_soorat = a1_soorat + (2*(i+1) - 1)
    a1_makhraj = a1_makhraj + 2
    
print(sum0)
