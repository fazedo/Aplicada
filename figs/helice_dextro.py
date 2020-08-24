# Plotagem paramétrica de uma curva
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6*np.pi, 201)

x = np.cos(t)
y = np.sin(t)
z = t

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot(x, y, z)

ax.view_init(25, 20) # Elevação e azimute

#ax.set_xticks([-2, -1, 0, 1, 2])
#ax.set_yticks([-2, -1, 0, 1, 2])
ax.set_zticks([0, 5, 10, 15, 20])

#fig.suptitle('Hélice circular uniforme dextrogira')
fig.set_facecolor('white')
plt.show()
#plt.savefig('helice_dextro.png', dpi=200)
