from math import floor
count = 0
Snumber = []
prompt = 'please enter a Square number: '
while count < 10:
    number = int(input(prompt))
    if pow(number,1/2) == floor(pow(number,1/2)):
        Snumber.append(number)
        count = count + 1
        prompt = 'please enter another Square number: '
    else:
        prompt = 'You must enter a Square number: '

row = 1
for i in Snumber:
    print(row,': ', i)
    row += 1
    
