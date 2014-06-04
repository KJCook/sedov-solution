convert_to_cgs(double rho_code, double P_code, double *rho_cgs, double *T_GK){
  double mu = 0.5;
  double mH = 1.6733e-24;
  double kb = 1.380658e-16;
  double kappa = 3.02e13;
  double Rsun = 6.96e10;
  double Msun = 1.99e33;
  double gamma = 5.0/3.0;

  *rho_cgs = rho_code * Msun / (Rsun*Rsun*Rsun);
  *T_GK = 1.0e-9 * kappa*pow(rho,gamma-1.0)*mu*mH/kb;
}
