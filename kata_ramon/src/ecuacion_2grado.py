from math import sqrt
from decimal import Decimal

def ecuacion_segundo_grado(a, b, c):
    if a == 0:
        return None

    if b == c == 0:
        return 0

    if c == 0:
        x = 0
        y = -b / a
        return x, y
    
    if b == 0:
        if Decimal(a).is_signed() ^ Decimal(c).is_signed():  # XOR
            x = sqrt(-c / a)
            y = -sqrt(-c / a)
            return x, y
        else:
            return None

    
    
    

