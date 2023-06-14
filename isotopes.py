import numpy as np

class Isotope:
    def __init__(self, name):
        self.name = name
    
    def alpha_lv(self, Tc):
        TK = Tc + 273.15
        if self.name == "18O":
            ln_a = 0.35041 * (1e6 / TK ** 3) - 1.6664 * (1e3 / TK ** 2) + 6.7123 / TK - 0.007685
        elif self.name == "2H":
            ln_a = 1.1588 * (TK ** 3 / 1e9) - 1.6201 * (TK ** 2 / 1e6) + 0.79484 * (TK/1e3) + 2.9992 * (1e6 / TK ** 3) - 0.16104
        else:
            ln_a = np.nan
    
        return np.exp(ln_a)

    def eps_eq(self, Tc):
        return (self.alpha_lv(Tc) - 1) * 1000.
    
    def eps_k(self, RH):
        if self.name == "18O":
            Ck = 14.2 # permil
        elif self.name == "2H":
            Ck = 12.5 # permil
        else:
            Ck = np.nan

        return (1 - RH) * Ck
    
    def eps_tot(self, Tc, RH):
        return self.eps_eq(Tc) + self.eps_k(RH)

    def delta_e(self, Tc, RH, delta_w, delta_atm):
        num = self.alpha_lv(Tc) * delta_w - RH * delta_atm - self.eps_tot(Tc, RH)
        den = 1 - RH + self.eps_k(RH) / 1000
        
        return num / den
