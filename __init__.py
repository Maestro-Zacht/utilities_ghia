from .estrazioni import estrai
from .combinatoria import fattoriale, binomiale, multinomiale
from .tdn import fattorizzazione, is_primo, phi
from .logs import my_logger
from math import log10


def conta_cifre(n):
    if n > 0:
        R = int(log10(n)) + 1
    elif n == 0:
        return 1
    else:
        R = int(log10(-n)) + 1

    if 10**(R - 1) > n:
        R -= 1

    return R
