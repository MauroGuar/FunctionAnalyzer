import matplotlib.pyplot as plt
import numpy as np

# Separate the numbers of the graph by 100 pixels and apply a range for X between -10 and 10
x = np.arange(-11,11,1)

func = str(input("\nFunction: "))

# The function itself (y = f(x))
y = eval(func)

# Place the axes in the center
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Graph the function
plt.plot(x,y, 'y')

# Show the function
plt.show()