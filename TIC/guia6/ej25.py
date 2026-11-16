"""25. Implementar funciones en Python que reciban como parámetro la matriz de un canal y
calculen su capacidad en los siguientes casos:
a. Canal determinante
b. Canal sin ruido
"""

import math

def capacidad_determinante(M):
    salidas = 0

    for j in range(len(M[0])):
        existe = False

        for i in range(len(M)):
            if M[i][j] == 1:
                existe = True

        if existe:
            salidas += 1

    return math.log2(salidas)


def capacidad_sin_ruido(M):
    return math.log2(len(M))



M = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0]
]

print(capacidad_determinante(M))
print(capacidad_sin_ruido(M))