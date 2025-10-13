import math

# Beispielhafte Wertepaare für U (Volt) und I (Ampere)
U_values = [2.1,2.3,2.3,2.4,2.5,2.5,2.6,2.6,2.6,2.7,2.7,2.7,2.8,2.8,1.9]
I_values = [0.016, 0.015, 0.013, 0.012, 0.011, 0.01, 0.009, 0.009, 0.008, 0.007, 0.006, 0.005, 0.004, 0.003, 0.017]

# Konstante Fehler für U und I
delta_U = 0.1  # Volt
delta_I = 0.001  # Ampere

# Ergebnisliste
errors = []

print("Nr.\tU [V]\tI [A]\tDelta_chi")
for i in range(len(U_values)):
    U = U_values[i]
    I = I_values[i]

    # Partiellen Ableitungen
    dchi_dU = (2 * U) / (I**2)
    dchi_dI = (-2 * U**2) / (I**3)

    # Gesamtfehler
    delta_chi = math.sqrt((dchi_dU * delta_U)**2 + (dchi_dI * delta_I)**2)
    errors.append(delta_chi)

    print(f"{i+1:2d}\t{U:.2f}\t{I:.2f}\t{delta_chi:.5f}")

# Optional: Zugriff auf die Liste der Fehler
# print(errors)

