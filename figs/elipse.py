# Plotagem paramétrica de uma curva
import numpy as np
import matplotlib.pyplot as plt

a = 4
b = 2

t = np.linspace(0, 2*np.pi, 101)

x = a*np.cos(t)
y = b*np.sin(t)

fig, ax = plt.subplots()

ax.plot(x, y)


fig.set_facecolor('white')
plt.axis('scaled')
plt.show()
plt.savefig('elipse.png', dpi=200)
