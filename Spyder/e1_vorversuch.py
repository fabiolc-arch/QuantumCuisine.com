import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Messdaten
nu_kHz = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 20, 24, 28, 1.5]) * 1e3  # Hz
UE = np.array([2.1, 2.3, 2.3, 2.4, 2.5, 2.5, 2.6, 2.6, 2.6, 2.7, 2.7, 2.7, 2.8, 2.8, 1.9])
IL = np.array([1.6, 1.5, 1.3, 1.2, 1.1, 1.0, 0.9, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 1.7]) / 100

# Konstanten
R = 100  # Ohm
omega = 2 * np.pi * nu_kHz
Z = UE / IL
Z_squared = Z**2
X_L_squared = Z_squared - R**2

# Linearisierung: X_L^2 = (omega*L)^2 => X_L^2 ~ omega^2 -> Fit y = a * x
x = omega**2
y = X_L_squared

# Fit
def linear(x, a): return a * x
popt, pcov = curve_fit(linear, x, y)
L = np.sqrt(popt[0])  # L in H

# Frequenzbereich für glatte Theoriekurve
nu_theo = np.linspace(min(nu_kHz), max(nu_kHz), 1000)
omega_theo = 2 * np.pi * nu_theo

# Theoretische Stromstärke
I_theo = UE.mean() / np.sqrt(R**2 + (omega_theo * L)**2)

print(f"L = {L:.6f} H")

# Plot
plt.errorbar(nu_kHz, IL, yerr=0.001, fmt='o', label='Messwerte')
plt.plot(nu_theo, I_theo, label=f"Theoriekurve", color='red')
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Stromstärke (A)")
plt.title("Stromstärke vs Frequenz")
plt.grid(True)
plt.legend()
plt.savefig("stromstaerke_vs_freq.pdf")


