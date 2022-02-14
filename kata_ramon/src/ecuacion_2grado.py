from math import sqrt

def raiz_segundo_grado(a, b, c):
    if a == 0:
        return None

    if b == c == 0:
        return 0
        
    if b == 0:
        if a == c:
            return None
        return (abs(c//a), c//a)

    if c == 0:
        return 0, -(b//a)

    raizCuadrada = b ** 2 - 4 * a * c
    if raizCuadrada >= 0:
        x = (-b + sqrt(raizCuadrada)) / (2 * a)
        y = (-b - sqrt(raizCuadrada)) / (2 * a)
        return x, y
    else:
        return None
    
    

