import numpy as np
import ax_parameters  as par
from scipy.special import roots_gegenbauer
import repelem_tile as rep
import ax_basis as bs
import scipy.special as sp
from scipy.optimize import fsolve

LR = par.LR
PR = par.PR
PX = par.PX
PZ = par.PZ
LZ = par.LZ
LX = par.LX
repelem = rep.repelem
LZ = par.LZ
LRHO = par.LRHO
LR = par.LR
PZ = par.PZ
PR = par.PR
N = par.N
SBr = bs.SBr
dSBr = bs.dSBr
ddSBr = bs.ddSBr
SBz = bs.SBz
dSBz = bs.dSBz
ddSBz = bs.ddSBz
# N = 60                                                   # Truncation ordem
                                          # Map parameter 


##Chebyshev collocation points

def SB_colpoints(n):
    return np.cos(np.arange(2*n + 4)*np.pi /(2*n + 3))

##Chebyshev collocation points in z
col = SB_colpoints(PZ)
#col = np.cos(np.arange(2*N + 4)*math.pi /(2*N + 3))      # collocation points (Verificado)

colr = col[1:PZ+2]

z1 = LZ * colr/(np.sqrt(1-colr**2))                       # physical domain (Verificado)  
z = np.flip(z1)

##Chebyshev collocation points in r

# def SB_zpoints(n):
#     return np.cos(np.arange(2*n + 4)*np.pi /(2*n + 3))

col = SB_colpoints(PR)
#col = np.cos(np.arange(2*N + 4)*math.pi /(2*N + 3))      # collocation points (Verificado)

colr = col[1:PR+2]

colr1 = LR * colr/(np.sqrt(1-colr**2))                       # physical domain (Verificado)  
r = np.flip(colr1)

###Legendre polynomials in x

# #collocation points for x
# P_prime = sp.legendre(2 * PX + 1).deriv()
# x_roots = fsolve(P_prime, np.cos(np.pi * (np.arange(1, 2 * PX + 2) / (2 * PX + 2))))
# x_col_prel = np.concatenate(([-1], np.sort(x_roots), [1]))
# x__col = -np.flip(x_col_prel[:PX + 1])
#print('x__col=', x__col)  #confere

# Base Matrix (Tchebyshev Polinomials) in z: 

SB_z = np.zeros([PZ+1,PZ+1])
zSB = np.zeros([PZ+1,PZ+1])
zzSB = np.zeros([PZ+1,PZ+1])

for i in range(PZ+1):
  SB_z[i,] = SBz(i,z)                                                 

for i in range(PZ+1):
  zSB[i,] = dSBz(i,z)

for i in range(PZ+1):
  zzSB[i,] = ddSBz(i,z)                     

### Base Matrix (Tchebyshev Polinomials) in r: 

SB_r = np.zeros([PR+1,PR+1])
rSB = np.zeros([PR+1,PR+1])
rrSB = np.zeros([PR+1,PR+1])

for i in range(PR+1):
  SB_r[i,] = SBr(i,r)                                                 

for i in range(PR+1):
  rSB[i,] = dSBr(i,r)

for i in range(PR+1):
  rrSB[i,] = ddSBr(i,r)                     

### Base Matrix (Legendre Polynomials) in x:

# P = np.zeros((PX + 1, PX + 1))
# P_x = np.zeros((PX + 1, PX + 1))
# P_xx = np.zeros((PX + 1, PX + 1))

# for i in range(PX + 1):
#     P[i,] = sp.legendre(i)(x__col / LX)  # Avaliação dos polinômios de Legendre
#     P_x[i,] = sp.legendre(i).deriv()(x__col / LX) * (1 / LX)  # Primeira derivada
#     P_xx[i,] = sp.legendre(i).deriv().deriv()(x__col / LX) * (1 / LX**2)  # Segunda derivada

##Cylindrical basis

SB_cyl = np.tile(SB_z,(PR+1,PR+1)) * repelem(SB_r,(PZ+1,PZ+1))

dzSB_cyl = np.tile(zSB,(PR+1,PR+1)) * repelem(SB_r,(PZ+1,PZ+1))
dzzSB_cyl = np.tile(zzSB,(PR+1,PR+1)) * repelem(SB_r,(PZ+1,PZ+1))

drSB_cyl = np.tile(SB_z,(PR+1,PR+1)) * repelem(rSB,(PZ+1,PZ+1))
drrSB_cyl = np.tile(SB_z,(PR+1,PR+1)) * repelem(rrSB,(PZ+1,PZ+1))

SB_cyl_inv = np.linalg.inv(SB_cyl)

# print(SB_cyl.shape)

### Spherical Basis

# Basis_sph = np.tile(P,(PR+1,PR+1)) * repelem(SB_r,(PX+1,PX+1))

# dxBasis_sph = np.tile(P_x,(PR+1,PR+1)) * repelem(SB_r,(PX+1,PX+1))
# dxxBasis_sph = np.tile(P_xx,(PR+1,PR+1)) * repelem(SB_r,(PX+1,PX+1))

# drBasis_sph = np.tile(P,(PR+1,PR+1)) * repelem(rSB,(PX+1,PX+1))
# drrBasis_sph = np.tile(P,(PR+1,PR+1)) * repelem(rrSB,(PX+1,PX+1))

# Basis_sph_inv = np.linalg.inv(Basis_sph)