m = int(input('Please enter a number: '))

n = m
while True:
    m = m+1
    flag = 0
    for i in range(2,m):
        if m%i == 0:
            flag = 1
            break
    if flag == 0:
        print('{0} is the first primarly number right after {1}'.format(m,n))
        break
    
            
