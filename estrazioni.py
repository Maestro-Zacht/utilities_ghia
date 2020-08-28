import itertools
import random
from .combinatoria import binomiale


def estrai(lista=None, n=1):
    """estrae n elementi da un iterabile e li restituisce"""
    if n < 1:
        raise Exception('Non è possibile estrarre meno di 1 persona')

    elif lista is None:
        lista = range(1, n + 1)

    elif n > len(lista):
        n = len(lista)

    prova = itertools.combinations(lista, n)
    i = itertools.count(1)
    estratto = random.randint(1, binomiale(len(lista), n))

    while True:
        if next(i) == estratto:
            return next(prova)
        next(prova)
