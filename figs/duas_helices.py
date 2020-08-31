# Plotagem paramétrica de uma curva
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6*np.pi, 201)

x = np.cos(t)
y = np.sin(t)
z = np.sin(2*t)

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

ax1.plot(x, y, z)
ax2.plot(y, x, z)

ax1.view_init(25, 20) # Elevação e azimute

ax1.set_xticks([-2, -1, 0, 1, 2])
ax1.set_yticks([-2, -1, 0, 1, 2])
ax1.set_zticks([0, 5, 10, 15, 20])


ax2.view_init(25, 20) # Elevação e azimute

ax2.set_xticks([-2, -1, 0, 1, 2])
ax2.set_yticks([-2, -1, 0, 1, 2])
ax2.set_zticks([0, 5, 10, 15, 20])

#fig.suptitle('Hélice circular uniforme dextrogira')
fig.set_facecolor('white')
#plt.show()
plt.savefig('duas_helices.png', dpi=200)
