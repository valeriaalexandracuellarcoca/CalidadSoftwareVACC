import math

def calcular_area_circulo(radio):
    if radio < 0:
        return None
    else:
        return round(math.pi * radio**2, 2)
    
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n %i== 0 :
            return False
    return True