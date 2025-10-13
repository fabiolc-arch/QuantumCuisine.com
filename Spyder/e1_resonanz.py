import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Daten
# Frequenz in kHz
nu_kHz = np.array([1, 2, 3, 4, 4.6, 5.2, 5.5, 6.5, 7, 7.3, 7.5, 7.7, 8, 9, 9.4, 9.6, 9.8, 11, 12, 15]) *1e3

# U_E in V
UE = np.array([2.8, 2.7, 2.7, 2.6, 2.5, 2.4, 2.3, 2.0, 1.9, 1.9, 1.9, 1.9, 1.9, 2.1, 2.2, 2.2, 2.2, 2.4, 2.5, 2.6])

# I_L in V
IL = np.array([0.45, 0.9, 1.45, 1.7, 2.1, 2.5, 2.7, 3.3, 3.5, 3.6, 3.6, 3.6, 3.5, 3.2, 3.0, 2.9, 2.8, 2.4, 2.1, 1.6]) / 100

omega = 2 * np.pi * nu_kHz

# Fitfunktion
def resonance_current(omega, R, L, C, U0):
    Z = np.sqrt(R**2 + (omega * L - 1/(omega * C))**2)
    return U0 / Z

# Fit
initial_guess = [100, 5e-3, 0.1e-6, 2.5]
popt, pcov = curve_fit(resonance_current, omega, IL, p0=initial_guess)
R_fit, L_fit, C_fit, U0_fit = popt

# Plot
plt.errorbar(omega, IL, yerr=0.002, fmt='o', label="Daten")
omega_fine = np.linspace(min(omega), max(omega), 1000)
plt.plot(omega_fine, resonance_current(omega_fine, *popt), label="Theoriekurve")
plt.xlabel("ω [rad/s]")
plt.ylabel("Strom [A]")
plt.title("Resonanzkurve")
plt.legend()
plt.grid()
plt.savefig("resonanzkurve.pdf")


