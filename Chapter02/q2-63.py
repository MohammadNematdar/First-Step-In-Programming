counter = 0
Ssum = 4
num = 2
while counter < 20:
    flag = 0
    num += 1 
    for i in range(2,num):
        if num%i == 0:
            flag = 1
    if flag == 0:
        Ssum = Ssum + pow(num,2)
        counter += 1
print(Ssum)
        
        
        
