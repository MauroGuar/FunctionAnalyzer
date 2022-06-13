import matplotlib.pyplot as plt
import numpy as np

# Separar los numeros del gráfico entre 100 pixeles y aplicar un rango para X ente -10 y 10
x = np.linspace(-2,2,100)

# La función
y = np.sin(x)

# Colocar los ejes en el centro
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Graficar la función
plt.plot(x,y, 'y', label='y=e^x')
plt.legend(loc='upper left')

# Mostrar la función
plt.show()