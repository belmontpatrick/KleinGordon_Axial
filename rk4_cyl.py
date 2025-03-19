import numpy as np
import dynsys_cyl as ds
import time_grid_cyl as tg
import plot_var_mod as plot
import cylax_initialdata as ini

N = tg.N
h = tg.h
M = plot.M
Pi = ds.Pi
KG_cyl = ds.KG_cyl
SB_cyl_plot = plot.SB_cyl_plot
a0cyl = ini.a0cyl
da0cyl = ini.da0cyl


phi_set = np.zeros([N,M])

for i in range(N):  # Runge Kutta 4th order

  phi_ = Pi(a0cyl)
  dda_ = KG_cyl(a0cyl)
  L1 = h*(da0cyl)
  K1 = h*(dda_)

  phi_ = Pi(a0cyl + L1/2)
  dda_ = KG_cyl(a0cyl + L1/2)
  L2 = h*(da0cyl + K1/2)
  K2 = h*(dda_)

  phi_ = Pi(a0cyl + L2/2)
  dda_ = KG_cyl(a0cyl + L2/2)
  L3 = h*(da0cyl + K2/2)
  K3 = h*(dda_)

  phi_ = Pi(a0cyl + L3)
  dda_ = KG_cyl(a0cyl + L3)
  L4 = h*(da0cyl + K3)   ##da before
  K4 = h*(dda_)

#   da0 = da0 + 1/6 * (K1 + 2*K2 + 2*K3 + K4)
#   a0 = a0 + 1/6 * (L1 + 2*L2 + 2*L3 + L4)

  da0 = da0 + 1/6 * (K1 + 2*K2 + 2*K3 + K4)
  a0 = a0 + 1/6 * (L1 + 2*L2 + 2*L3 + L4)
  phi_set[i,:] = np.dot(a0cyl, SB_cyl_plot)

