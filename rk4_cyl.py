import numpy as np
import dynsys_cyl as ds
import time_grid_cyl as tg
import plot_var_mod as plot
import cylax_initialdata as ini
import ax_collocations as col
import ax_parameters as par

PR = par.PR
PX = par.PX
N = tg.N
h = tg.h
M = plot.M
phi = ds.phi
KG_cyl = ds.KG_cyl
# SB_cyl_plot = plot.SB_cyl_plot
SBphi_plot = plot.SBphi_plot
a0cyl = ini.a0cyl
da0cyl = ini.da0cyl
SBphi = col.SBphi

phiset_cyl = np.zeros([N, ((PR+1)*(PX+1))])  # Assuming a0cyl is of size M

for i in range(N):  # Runge Kutta 4th order

  phi_ = phi(a0cyl)
  dda_ = KG_cyl(a0cyl)
  L1 = h*(da0cyl)
  K1 = h*(dda_)

  phi_ = phi(a0cyl + L1/2)
  dda_ = KG_cyl(a0cyl + L1/2)
  L2 = h*(da0cyl + K1/2)
  K2 = h*(dda_)

  phi_ = phi(a0cyl + L2/2)
  dda_ = KG_cyl(a0cyl + L2/2)
  L3 = h*(da0cyl + K2/2)
  K3 = h*(dda_)

  phi_ = phi(a0cyl + L3)
  dda_ = KG_cyl(a0cyl + L3)
  L4 = h*(da0cyl + K3)   ##da before
  K4 = h*(dda_)

#   da0 = da0 + 1/6 * (K1 + 2*K2 + 2*K3 + K4)
#   a0 = a0 + 1/6 * (L1 + 2*L2 + 2*L3 + L4)

  da0cyl = da0cyl + 1/6 * (K1 + 2*K2 + 2*K3 + K4)
  a0cyl = a0cyl + 1/6 * (L1 + 2*L2 + 2*L3 + L4)

  phiset_cyl[i,:] = np.dot(a0cyl.T, SBphi_plot)
  
  #     # Store the current values of a0cyl and da0cyl
  # a0cyl_set[i, :] = a0cyl
  # da0cyl_set[i, :] = da0cyl

np.savetxt("datatest.txt", phiset_cyl, fmt="%.16e", delimiter="\t")

# acyl = np.zeros([(PR+1)*(PX+1), N])  # Assuming a0cyl is of size M
# dacyl = np.zeros([N, M])  # Assuming da0cyl is of size M

# for i in range(N):  # Runge Kutta 4th order

#   phi_ = Pi(a0cyl)
#   dda_ = KG_cyl(a0cyl)
#   L1 = h*(da0cyl)
#   K1 = h*(dda_)

#   phi_ = Pi(a0cyl + L1/2)
#   dda_ = KG_cyl(a0cyl + L1/2)
#   L2 = h*(da0cyl + K1/2)
#   K2 = h*(dda_)

#   phi_ = Pi(a0cyl + L2/2)
#   dda_ = KG_cyl(a0cyl + L2/2)
#   L3 = h*(da0cyl + K2/2)
#   K3 = h*(dda_)

#   phi_ = Pi(a0cyl + L3)
#   dda_ = KG_cyl(a0cyl + L3)
#   L4 = h*(da0cyl + K3)   ##da before
#   K4 = h*(dda_)

# #   da0 = da0 + 1/6 * (K1 + 2*K2 + 2*K3 + K4)
# #   a0 = a0 + 1/6 * (L1 + 2*L2 + 2*L3 + L4)

#   dacyl[i] = da0cyl + 1/6 * (K1 + 2*K2 + 2*K3 + K4)
#   acyl[i] = a0cyl + 1/6 * (L1 + 2*L2 + 2*L3 + L4)
  
#   #     # Store the current values of a0cyl and da0cyl
#   # a0cyl_set[i, :] = a0cyl
#   # da0cyl_set[i, :] = da0cyl

# np.savetxt("a0cylset.txt", acyl, fmt="%.16e", delimiter="\t")
# np.savetxt("da0cylset.txt", dacyl, fmt="%.16e", delimiter="\t")

# a0cyl = np.zeros([N, M])  # Assuming a0cyl is of size M
# da0cyl = np.zeros([N, M])  # Assuming da0cyl is of size M

# for i in range(N):  # Runge Kutta 4th order

#   phi_ = np.dot(SBphi,a0cyl)
#   dda_ = KG_cyl(a0cyl)
#   L1 = h*(da0cyl)
#   K1 = h*(dda_)

#   phi_ = np.dot(SBphi, a0cyl + L1/2)
#   dda_ = KG_cyl(a0cyl + L1/2)
#   L2 = h*(da0cyl + K1/2)
#   K2 = h*(dda_)

#   phi_ = np.dot(SBphi, a0cyl + L2/2)
#   dda_ = KG_cyl(a0cyl + L2/2)
#   L3 = h*(da0cyl + K2/2)
#   K3 = h*(dda_)

#   phi_ = np.dot(SBphi, a0cyl + L3)
#   dda_ = KG_cyl(a0cyl + L3)
#   L4 = h*(da0cyl + K3)   ##da before
#   K4 = h*(dda_)

# #   da0 = da0 + 1/6 * (K1 + 2*K2 + 2*K3 + K4)
# #   a0 = a0 + 1/6 * (L1 + 2*L2 + 2*L3 + L4)

#   da0cyl[i] = da0cyl + 1/6 * (K1 + 2*K2 + 2*K3 + K4)
#   a0cyl[i] = a0cyl + 1/6 * (L1 + 2*L2 + 2*L3 + L4)
  
#   #     # Store the current values of a0cyl and da0cyl
#   # a0cyl_set[i, :] = a0cyl
#   # da0cyl_set[i, :] = da0cyl

# np.savetxt("a0cylset.txt", a0cyl, fmt="%.16e", delimiter="\t")
# np.savetxt("da0cylset.txt", da0cyl, fmt="%.16e", delimiter="\t")
