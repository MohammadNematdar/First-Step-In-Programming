n = int(input('PLEASE ENTER A NUMBER: '))
sum_odds = 0
for i in range(0,n):
    if i%2 != 0:
        sum_odds = sum_odds + i
print(sum_odds)
