import numpy as np
import ax_collocations as col

dzzSB_cyl = col.dzzSB_cyl
drSB_cyl = col.drSB_cyl
drrSB_cyl = col.drrSB_cyl
R = col.r
SB_cyl = col.SB_cyl

def KG_cyl(c):

    drphi = np.dot(drSB_cyl,c)
    drrphi = np.dot(drrSB_cyl,c)
    dzzphi = np.dot(drrSB_cyl,c)

    RHS = drrphi + 1/R * drphi + dzzphi

    return np.dot(SB_cyl,RHS)

def Pi(c_dot):
    return np.dot(SB_cyl,c_dot)