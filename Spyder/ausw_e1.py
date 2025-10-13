import numpy as np

u_werte = [2.1,2.3,2.3,2.4,2.5,2.5,2.6,2.6,2.6,2.7,2.7,2.7,2.8,2.8,1.9]
a_werte = [0.45,0.9,1.5,3.4,4.2,5,5.4,6.6,7,7.2,7.2,7.2,7,6.4,6,5.8,5.6,4.8,4.2,3.2]
f_werte = [1,2,3,4,4.6,5.2,5.5,6.5,7,7.3,7.5,7.7,8,9,9.4,9.6,9.8,11,12,15]
t_werte = [2.4,0.54,0.7,0.5,0.33,0.3,0.24,0.12,0.07,0.02,0,-0.02,-0.04,-0.1,-0.12,-0.13,-0.14,-0.15,-0.16,-0.13]

def formel(f):
        return 0.004 * np.pi * f
    
def berechne_nte_paare(f_werte):
    ergebnisse = []
    for f in list(f_werte):
        ergebnis = formel(f)
        ergebnisse.append(ergebnis)
    return ergebnisse

resultate = berechne_nte_paare(f_werte)
print(resultate)

def formell(a, r=100):
    return a / r

def berechne(a_werte):
    ergebnissse = []
    for a in list(a_werte):
        ergebniss = formell(a, r=100)
        ergebnissse.append(ergebniss)
    return ergebnissse

resultatte = berechne(a_werte)
print(resultatte)

def forrmel(t, f):
    return 2 * np.pi * t * f * 1e3

def berechne_mte_paare(t_werte, f_werte):
    erjebnisse = []
    for t, f in zip(t_werte, f_werte):
        erjebnis = forrmel(t, f)
        erjebnisse.append(erjebnis)
    return erjebnisse
    
resultade = berechne_mte_paare(t_werte, f_werte)
print(resultade)
