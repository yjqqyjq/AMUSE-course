#create a new particle
Jupyter=Particles(1)
#set up the propities
Jupyter.name = "Jupyter"
Jupyter.mass = 1.8982e+27| units.kg
Jupyter.position = (5.2038, 0, 0) | units.AU
#calculate the velocity
vorb = relative_orbital_velocity(sun.mass + Jupyter.mass, 
                                 Jupyter.position.sum())
Jupyter.velocity = (0, 1, 0) * vorb
solarsystem.add_particle(Jupyter)