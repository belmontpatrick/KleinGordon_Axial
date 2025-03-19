import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def surface(x,y):
    return 50 - (x**2 + y**2)

def gaussian(A0, x,y):
    return A0*np.exp( - ((x-2)/10)**2 + ((y-2)/10)**2)

N = 1000
A0 = 2

# x_values = np.linspace(-1.6,1.6,N)
# y_values = np.linspace(-1.6,1.6,N)

x_values = np.linspace(-10,10,N)
y_values = np.linspace(-10,10,N)

X, Y = np.meshgrid(x_values,y_values)

Z = gaussian(A0,X,Y)

# Z = surface(X,Y)

# plt.contourf(X, Y, Z, levels = 500, cmap = 'viridis')
# plt.colorbar(label = 'Amplitude')

ax = plt.axes(projection = '3d')
ax.plot_surface(X, Y, Z, cmap=cm.viridis)
plt.show()
