import numpy as np

# Daten
daten_sys_l = [115, 119, 120, 103, 105]  
daten_dia_l = [82, 83, 80, 69, 74]
daten_pul_l = [64, 60, 64, 60, 61]
daten_sys_r = [111, 111 , 1]  
daten_dia_r = [68, 66, ]
daten_pul_r = [56, 56, ]


# Berechnung Mittelwert und Standardabweichung Mittelwert
def mittelwert_und_std(daten):
    mittelwert = np.mean(daten)
    std_abw_mittelwert = np.std(daten, ddof=1) / np.sqrt(len(daten))
    return mittelwert, std_abw_mittelwert

# Mittelwert und Standardabweichung
mittelwert_sys_l, std_sys_l = mittelwert_und_std(daten_sys_l)
mittelwert_dia_l, std_dia_l = mittelwert_und_std(daten_dia_l)
mittelwert_pul_l, std_pul_l = mittelwert_und_std(daten_pul_l)
mittelwert_sys_r, std_sys_r = mittelwert_und_std(daten_sys_r)
mittelwert_dia_r, std_dia_r = mittelwert_und_std(daten_dia_r)
mittelwert_pul_r, std_pul_r = mittelwert_und_std(daten_pul_r)
print(f"Mittelwert sys_l: {mittelwert_sys_l:.5f}, Standardabweichung Mittelwert: {std_sys_l:.5f}")
print(f"Mittelwert dia_l: {mittelwert_dia_l:.5f}, Standardabweichung Mittelwert: {std_dia_l:.5f}")
print(f"Mittelwert pul_l: {mittelwert_pul_l:.5f}, Standardabweichung Mittelwert: {std_pul_l:.5f}")
print(f"Mittelwert sys_r: {mittelwert_sys_r:.5f}, Standardabweichung Mittelwert: {std_sys_r:.5f}")
print(f"Mittelwert dia_r: {mittelwert_dia_r:.5f}, Standardabweichung Mittelwert: {std_dia_r:.5f}")
print(f"Mittelwert pul_r: {mittelwert_pul_r:.5f}, Standardabweichung Mittelwert: {std_pul_r:.5f}")