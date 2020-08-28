def fattoriale(a):
    ris = 1
    for i in range(1, a + 1):
        ris *= i
    return ris


def binomiale(a, b):
    if a < b:
        raise Exception('binomiale non valido')

    sopra = 1
    for i in range(b + 1, a + 1):
        sopra *= i

    sotto = 1
    for i in range(1, a - b + 1):
        sotto *= i

    return sopra // sotto


def multinomiale(sopra, sotto):
    den = 1
    for num in sotto:
        den *= fattoriale(num)
    return fattoriale(sopra) // den
