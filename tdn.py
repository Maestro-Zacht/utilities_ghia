from math import sqrt

elenco_numeri_primi = []
numeri_primi_caricati = False


def is_primo(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def fattorizzazione(num):
    if not numeri_primi_caricati:
        with open('D:\\programmazione\\file per path\\utilities_ghia\\ris_feef.txt') as f:
            for numero in f.readlines():
                elenco_numeri_primi.append(int(numero))
        numeri_primi_caricati = True

    fattori = []
    for i in elenco_numeri_primi:
        if num % i == 0:
            fattori.append([i, 1])
            mul = i**2
            while num % mul == 0:
                mul *= i
                fattori[-1][1] += 1
            num //= fattori[-1][0]**fattori[-1][1]
        if num == 1:
            break
    return fattori


def phi(num):
    fatt = fattorizzazione(num)
    R = 1
    for base, esponente in fatt:
        R *= base**(esponente - 1) * (base - 1)
    return R
