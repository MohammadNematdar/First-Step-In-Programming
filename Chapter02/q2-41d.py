n = int(input('enter the number: '))

a1 = 1
sum0 = 0
for i in range(1,n+1):
    sum0 = sum0 + i*((-1)**(i+1))
    
print(sum0)
