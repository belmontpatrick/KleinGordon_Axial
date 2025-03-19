import numpy as np
import ax_basis as bs
import repelem_tile as rep
import matplotlib.pyplot as plt
import ax_parameters as par

SBz = bs.SBz
SBr = bs.SBr
dSBz = bs.dSBz
dSBr = bs.dSBr
ddSBr = bs.ddSBr
ddSBz = bs.ddSBz
repelem = rep.repelem
PR = par.PR
PZ = par.PZ

M = 100

rplot = np.linspace(0.000001,10,M)
zplot = np.linspace(0.000001,10,M)

Rplot, Zplot = np.meshgrid(rplot, zplot, indexing = 'ij') 

SBz_plot = np.zeros([M,M])   ###PZ + 1, M
SBr_plot = np.zeros([M,M])   ###PR + 1, M
dSBz_plot = np.zeros([M,M])
dSBr_plot = np.zeros([M,M])
ddSBz_plot = np.zeros([M,M])
ddSBr_plot = np.zeros([M,M])

for i in range(M):
  SBr_plot[i,] = SBr(i,rplot) 

for i in range(M):
  SBz_plot[i,] = SBr(i,zplot)

for i in range(M):
  dSBr_plot[i,] = dSBr(i,rplot) 

for i in range(M):
  ddSBr_plot[i,] = SBr(i,zplot) 

for i in range(M):
  dSBz_plot[i,] = SBr(i,zplot)

for i in range(M):
  ddSBz_plot[i,] = SBr(i,zplot)

# psirplot = SBr_plot[]

SB_cyl_plot = np.tile(SBz_plot,(M,M)) * repelem(SBr_plot,(M,M))

SB_cyl_inv_plot = np.linalg.inv(SB_cyl_plot)

# print(SB_cyl_plot.shape)