import numpy as np

def rho_cgs(rho_code, P_code):
    Msun = 1.99e33;
    Rsun = 6.96e10;
    return rho_code * Msun / Rsun**3;

def T_GK(rho_code, P_code):
    kb = 1.380658e-16;
    mu = 0.5;
    mH = 1.6733e-24;
    Msun = 1.99e33;
    Rsun = 6.96e10;
    P = P_code * Msun/Rsun;
    rho = rho_cgs(rho_code, P_code);
    T = mu*mH/kb * P/rho;
    return 1.0e-9 * T;

print rho_cgs(5.92028E+08,8.54297E+06)
print T_GK(5.92028E+08,8.54297E+06)
