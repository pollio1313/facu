import math
import random

def agregarParidad(caracter):
    ascii=ord(caracter)
    binario=format(ascii,"07b")

    unos=binario.count("1")

    if unos % 2==0:
        parida="0"
    else:
        paridad="1"

    return binario + paridad

def verificarParidad(byte):
    unos = byte.count("1")

    return unos %2 ==0



print(agregarParidad('h'), verificarParidad("11010001"))