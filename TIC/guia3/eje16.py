"""
16. Implementar una función en Python que reciba como parámetros: un número entero N y
dos listas paralelas que contengan las palabras código de una codificación y sus respectivas probabilidades, 
y genere aleatoriamente un posible mensaje de N símbolos codificados emitido por dicha fuente.
"""

import math
import random


def simulacion(n,listaA,listaP):
    mensaje = random.choices(listaA,weights=listaP,k=n)
    mensaje = ''.join(mensaje)
    return mensaje



probS=[0.1,0.5,0.1,0.2,0.05,0.05]
cod4=['.,',';',',,',':','...',',:;']
print(simulacion(25,cod4,probS))

