import numpy as np
import ax_collocations as col

dzzSB_cyl = col.dzzSB_cyl
drSB_cyl = col.drSB_cyl
drrSB_cyl = col.drrSB_cyl
R = col.r
SB_cyl = col.SB_cyl
SB_cyl_inv = col.SB_cyl_inv
SBphi = col.SBphi
SBphi_inv = col.SBphi_inv
dzzSBphi = col.dzzSBphi
drSBphi = col.drSBphi
drrSBphi = col.drrSBphi

Rm = np.repeat(R,31)
Rr = Rm.reshape(-1,1)

def KG_cyl(c):

    drphi = np.dot(drSBphi,c)
    drrphi = np.dot(drrSBphi,c)
    dzzphi = np.dot(dzzSBphi,c)

    RHS = drrphi + drphi*1/Rr  + dzzphi

    return np.dot(SBphi_inv,RHS)

def phi(c):
    return np.dot(SBphi,c)





# def KG_cyl(c):

#     drphi = np.dot(drSB_cyl,c)
#     drrphi = np.dot(drrSB_cyl,c)
#     dzzphi = np.dot(dzzSB_cyl,c)

#     RHS = drrphi + drphi*1/Rr  + dzzphi

#     return np.dot(SB_cyl_inv,RHS)

# def Pi(c_dot):
#     return np.dot(SB_cyl_inv,c_dot)
