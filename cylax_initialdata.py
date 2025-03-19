import numpy as np
import ax_collocations as col
import ax_parameters as par
import matplotlib.pyplot as plt
import plot_var_mod as plot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

A0 = par.A0
r0 = par.r0
z0 = par.z0
SIGMA_R = par.SIGMA_R
SIGMA_Z = par.SIGMA_Z
PR = par.PR
r = col.r
z = col.z
SB_cyl_inv = col.SB_cyl_inv
SB_cyl = col.SB_cyl
M = plot.M
SB_cyl_inv_plot = plot.SB_cyl_inv_plot
SB_cyl_plot = plot.SB_cyl_plot
Rplot = plot.Rplot
Zplot = plot.Zplot
PR = par.PR
PZ = par.PZ


R, Z = np.meshgrid(r,z,indexing = 'ij')

##Defining the initial data

def cyl_gauss(A0,x,y,sigma_r,sigma_z):
    return A0 * (np.exp( - (((x-r0)**2 / sigma_r**2) + ((y - z0)**2 / sigma_z**2)) ) )

gauss0cyl = cyl_gauss(A0,R,Z,SIGMA_R,SIGMA_Z)

g0cyl_rep = gauss0cyl.reshape(-1,1) ##transforms it in a collumn vector

a0cyl = np.dot(SB_cyl_inv,g0cyl_rep)

phicyl0 = np.dot(SB_cyl,a0cyl)

da0cyl = np.zeros([PR*PZ])

# print(g0cyl_rep.shape)
# print(SB_cyl_inv.shape)

print(gauss0cyl)
print(g0cyl_rep)

###Plotting
# g0cylplot = cyl_gauss(A0,Rplot,Zplot,SIGMA_R,SIGMA_Z)
# g0cylplot_rep = g0cylplot.reshape(-1,1)


# a0cylplot = np.dot(SB_cyl_inv_plot,g0cylplot_rep)

# inidatacylplot = np.dot(SB_cyl_plot,a0cylplot)

# inidatacylplot = inidatacylplot.reshape(100, 100)

# print(inidatacylplot.shape)
# print(g0cylplot.shape)

# ax = plt.axes(projection = '3d')
# ax.plot_surface(Rplot, Zplot, inidatacylplot, cmap=cm.viridis)

# ##Setting axis limits
# ax.set_xlim([0, 4])  # Set x-axis limits
# ax.set_ylim([0, 4])  # Set y-axis limits

# ##Setting axis ticks

# ax.set_xticks(np.arange(0, 4, 10))
# ax.set_yticks(np.arange(0, 4, 10))

# #Add grid lines
# ax.grid(True, linestyle='--', alpha=0.0)

# plt.show()

# print(a0cylplot.shape)
