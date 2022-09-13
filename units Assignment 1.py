#Assignment 1:
from amuse.units import units
#set the solar mass and the radius of the obrit
mstar = 1 | units.MSun
r=1|units.Au
#declare the gravitational constant
G = 6.67e-11 | units.m**3 * units.kg**-1 * units.s**-2
#calculate the orbital velocity
V= (G * mstar / r).sqrt()
print("the orbital velocity is",V.in_(units.kms))
#the orbital velocity is 29.7789148834 kms

