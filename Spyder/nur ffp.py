# gauß ffp
import numpy as np

# funktion
def funktion(g, h1, h2, l, m=1):
    return m * g * (h1 - h2)/l

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

werte = [9.81, 0.106, 0.108, 0.8]  # datensatz
std = [0.05, 0.001, 0.001, 0.001]  # stdabw

# gradienten berechnen
gradients = num_ableitung(funktion, werte)

# ffp
sigma_f = np.sqrt(np.sum([(g * s)**2 for g, s in zip(gradients, std)]))

print(f"Fehler Funktion:", sigma_f)

















