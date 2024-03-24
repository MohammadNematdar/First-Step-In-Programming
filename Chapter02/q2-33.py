energy = int(input('Energy (less than 8 Mev): '))
A = int(input('A: '))
density = int(input('Density: '))

while energy > 8:
    energy = int(input('enter Energy less than 8 Mev: ')) 

if energy <= 4:
    Range_air = 0.56*energy
elif 4 < energy and energy < 8:
    Range_air = 1.24*energy - 2.62
Range_med = 0.56*pow(density,1/3)*(Range_air/density)

print(Range_med)
