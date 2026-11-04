"""
14. Realizar una función booleana en Python que reciba como parámetros dos listas paralelas
que contengan las palabras código de una codificación y sus respectivas probabilidades, y
determine si se trata de un código compacto.
"""

import math

def Informacion(probabilidad):          #espera un solo valor de probabilidad
    info = math.log2(1/probabilidad)
    return info

def compacto(C,prob):
    EsCompacto=True

    for i in range(len(prob)):
        if not(round(Informacion(prob[i]))>=len(C[i])):
            EsCompacto=False
    return EsCompacto