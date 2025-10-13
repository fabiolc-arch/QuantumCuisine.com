# primes
import numpy as np

eingabe = int(input("Bitte geben Sie eine Liste ganzer Zahlen ein: "))

def ist_primzahl(n):
    for n in eingabe:
        if n < 2:
            return False
        for i in range(2, int(np.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True

primzahlenliste = list(map(ist_primzahl, eingabe))


print(f"Die Primzahlen sind: {primzahlenliste}")


        


    

