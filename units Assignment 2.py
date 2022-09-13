#Assignment 2:
from amuse.units import units
#set the black hole mass and the radius of the obrit
mstar = 4*10**6 | units.MSun
r=970|units.AU
#declare the gravitational constant
G = 6.67e-11 | units.m**3 * units.kg**-1 * units.s**-2
#calculate the escape velocity
V= (2*G * mstar / r).sqrt()

print("The escape speed is:",V.in_(units.kms))
The escape speed is: 2704.38173911 kms
