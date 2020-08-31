# Quiver
import matplotlib.pyplot as plt
import numpy as np


N = 11
x = np.linspace(-1, 1, N)
y = np.linspace(0, 1, N)

X = np.zeros((N, N), dtype=float)
Y = np.zeros((N, N), dtype=float)
F1 = np.zeros((N, N), dtype=float) # Componente x do campo
F2 = np.zeros((N, N), dtype=float) # Componente y do campo


for i in range(N):
    for j in range(N):
        X[i, j] = x[i]
        Y[i, j] = y[j]

        F1[i, j] = np.sqrt(y[i])
        F2[i, j] = 0

fig, ax = plt.subplots()
ax.quiver(X, Y, F1, F2)
fig.set_facecolor('white')
#plt.show()
fig.savefig('exemplo_1_4_2.png', dpi=200)
