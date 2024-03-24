n = input('Please enter a number: ')
m = ''
l = list(n)
l.sort(reverse=True)
for i in l:
    m = m + i
print(m)