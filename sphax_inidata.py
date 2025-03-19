import numpy as np
import ax_parameters as par
import ax_collocations as col

r0 = par.r0
x0 = par.x0
A0 = par.A0
PR = par.PR
PX = par.PX
SIGMA_R = par.SIGMA_R
SIGMA_X = par.SIGMA_X
x_col = col.x_col_prel
r = col.r
Basis_sph_inv = col.Basis_sph_inv
Basis_sph = col.Basis_sph

R, X = np.meshgrid(r,x_col,indexing = 'ij')


def gaussiansph(A0,x,y,sigma_r,sigma_x):
    return A0 * (np.exp( - (((x-r0)**2 / sigma_r**2) + ((y - x0)**2 / sigma_x**2)) ) )

sphgaussian0 = gaussiansph(A0,R,X,SIGMA_R,SIGMA_X)

sphg0_rep = sphgaussian0.reshape(-1,1)

a0sph = np.dot(Basis_sph_inv,sphg0_rep)

phisph0 = np.dot(Basis_sph,a0sph)

da0sph = np.zeros([PR*PX])

