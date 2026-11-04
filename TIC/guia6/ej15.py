"""
15. Implementar funciones en Python que reciban como parámetros: una lista con las
probabilidades a priori y la matriz de probabilidades condicionales del canal, y calculen por
definición (es decir, a partir de las probabilidades, no de sus relaciones):
a. La equivocación o ruido
b. La pérdida
c. La entropía afín
d. La información mutua
"""

import math


# Matriz de probabilidades conjuntas
def conjunta(P, M):
    J = []

    for i in range(len(P)):
        fila = []

        for j in range(len(M[0])):
            fila.append(P[i] * M[i][j])

        J.append(fila)

    return J


# a) Ruido: H(B|A)
def ruido_15(P, M):
    h = 0
    J = conjunta(P, M)

    for i in range(len(P)):
        for j in range(len(M[0])):
            if J[i][j] > 0:
                h -= J[i][j] * math.log2(M[i][j])

    return h


# b) Equivocacion: H(A|B)
def equivocacion_15(P, M):
    h = 0
    J = conjunta(P, M)

    PB = [
        sum(J[i][j] for i in range(len(P)))
        for j in range(len(M[0]))
    ]

    for i in range(len(P)):
        for j in range(len(PB)):
            if J[i][j] > 0:
                h += J[i][j] * math.log2(PB[j] / J[i][j])

    return h


# d) Informacion mutua: I(A;B)
def informacion_15(P, M):
    I = 0
    J = conjunta(P, M)

    PB = [
        sum(J[i][j] for i in range(len(P)))
        for j in range(len(M[0]))
    ]

    for i in range(len(P)):
        for j in range(len(PB)):
            if J[i][j] > 0:
                I += J[i][j] * math.log2(
                    J[i][j] / (P[i] * PB[j])
                )

    return I

