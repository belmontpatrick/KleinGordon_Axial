# import sympy as sp
# import numpy as np

# r = sp.symbols('r')

# A0 = 0.0002
# r0 = 2

# gauss = A0 * sp.exp(-(r-r0)**2)

# dgauss = sp.diff(gauss,r)

# integrand = dgauss**2

# anal_energy = sp.Integral(integrand*2*np.pi*r**2,(r,0,sp.oo)).doit()

# num_anal_energy = sp.N(anal_energy)

# print(num_anal_energy)