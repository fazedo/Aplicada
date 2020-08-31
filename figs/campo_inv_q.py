# Quiver
import matplotlib.pyplot as plt
import numpy as np


N = 11
x = np.linspace(-1, 1, N)
y = np.linspace(-1, 1, N)

X = np.zeros((N, N), dtype=float)
Y = np.zeros((N, N), dtype=float)
F1 = np.zeros((N, N), dtype=float) # Componente x do campo
F2 = np.zeros((N, N), dtype=float) # Componente y do campo


for i in range(N):
    for j in range(N):
        X[i, j] = x[i]
        Y[i, j] = y[j]
        r = np.sqrt(x[i]**2 + y[j]**2)
        comprimento = 1/(r**2 + .5)     # Altera a escala para melhor visualizar
        if r > 0.1:                     # Evita raios muito grandes no centro
            F1[i, j] = comprimento * x[i]/r
            F2[i, j] = comprimento * y[j]/r

fig, ax = plt.subplots()
ax.quiver(X, Y, F1, F2)
fig.set_facecolor('white')
#plt.show()
fig.savefig('campo_inv_q.png', dpi=200)
