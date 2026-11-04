import math
import random

def tasaCompresion (mensaje,codificacion):
    tam_original = len(mensaje.encode("utf-8"))
    tam_comprimido = len(codificacion)

    if tam_comprimido ==0:
        return 0
    
    return tam_original/ tam_comprimido
