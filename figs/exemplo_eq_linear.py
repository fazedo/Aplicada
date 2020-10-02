import matplotlib.pyplot as plt

f = lambda x: 3 - 2*x
fig, ax  = plt.subplots()
ax.plot([0, f(0)], [2, f(2)], color='blue')

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')

ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

# Adiciona rótulo aos eixos
#ax.set_xlabel("x", fontsize=14)
#ax.set_ylabel("y", fontsize=14)

#
ax.grid()
plt.savefig("exemplo_eq_linear.png", dpi=400)



plt.show()
# plt.savefig(nome_arquivo)
