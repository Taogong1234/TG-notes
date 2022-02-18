import numpy as np
from matplotlib import pyplot as plt

nx=501
dx=2/(nx-1)
CFL=0.5
dt=CFL*dx
nt=int(0.8/dt)
c=1
    
u=np.ones(nx)
u[int(0.5/dx):int(1/dx+1)]=2
un=np.ones(nx) #u0

for n in range (nt):
    un=u.copy() 
    for i in range(1,nx):   
        u[i]=un[i]-c*dt/dx*(un[i]-un[i-1])    
plt.grid()
plt.plot(np.linspace(0,2,nx),u)
plt.show()