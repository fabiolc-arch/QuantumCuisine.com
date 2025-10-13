import numpy as np

# Funktion
def funktion(dLdT, L0):
    return dLdT / L0

# Daten
daten_s = [20.0, 20.1, 20.0, 20.2, 20.1] 
daten_t = [0.0585, 0.0588, 0.0586, 0.0587, 0.0586]

# Berechnung Mittelwert und Standardabweichung Mittelwert
def mittelwert_und_std(daten):
    mittelwert = np.mean(daten)
    std_abw_mittelwert = np.std(daten, ddof=1) / np.sqrt(len(daten))
    return mittelwert, std_abw_mittelwert

# Mittelwert und Standardabweichung
mittelwert_s, std_s = mittelwert_und_std(daten_s)
mittelwert_t, std_t = mittelwert_und_std(daten_t)

werte = [mittelwert_s, mittelwert_t]
std = [std_s, std_t]

# numerische ableitung
def num_ableitung(funktion, werte, delta=1e-6):
    gradients = []
    for i in range(len(werte)):
        werte_oben = werte.copy()
        werte_unten = werte.copy()
        werte_oben[i] += delta
        werte_unten[i] -= delta
        grad = (funktion(*werte_oben) - funktion(*werte_unten)) / (2 * delta)
        gradients.append(grad)
    return gradients

# Gradienten berechnen
gradients = num_ableitung(funktion, werte)

# ffp
sigma_f = np.sqrt(np.sum([(g * s)**2 for g, s in zip(gradients, std)]))

print(f"Mittelwert s: {mittelwert_s:.5f}, Standardabweichung Mittelwert: {std_s:.5f}")
print(f"Mittelwert t: {mittelwert_t:.5f}, Standardabweichung Mittelwert: {std_t:.5f}")
print(f"Fehler Funktion: {sigma_f:.6f}")



