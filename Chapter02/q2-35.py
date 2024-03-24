vs = int(input('source velocity: '))
v0 = int(input('listener: '))
v = 340

source_d = input('enter the direction (right or left): ')
observer_d = input('enter the observer direction (right or left): ')

if source_d == 'right' or source_d.upper() == 'R':
    if observer_d == 'right' or observer_d.upper() == 'R':
        f = (v + v0)/(v + vs)
    elif observer_d == 'left' or observer_d.upper() == 'L':
        f = (v - v0)/(v + vs)
elif source_d == 'left' or source_d.upper() == 'L':
    if observer_d == 'right' or observer_d.upper() == 'R':
        f = (v + v0)/(v - vs)
    elif observer_d == 'left' or observer_d.upper() == 'L':
        f = (v - v0)/(v - vs)
print('listener frequency / source frequency: ', f )
