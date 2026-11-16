"""Realizar una función en Python que reciba como parámetros: la matriz de un canal binario
y un valor de paso, y estime la capacidad del canal mediante el cálculo de la información
mutua para un conjunto de probabilidades a priori distribuidas uniformemente según el
paso especificado. La función debe retornar el valor de capacidad estimado, junto con su
probabilidad asociada.
"""



import math

def capacidad_binaria(M, paso):
    capacidad = 0
    probabilidad_optima = None

    p = 0

    while p <= 1:
        P = [p, 1-p]

        # Probabilidades de salida
        PY = []

        for j in range(len(M[0])):
            prob = 0

            for i in range(2):
                prob += P[i] * M[i][j]

            PY.append(prob)

        # Entropía de salida
        HY = 0

        for prob in PY:
            if prob > 0:
                HY -= prob * math.log2(prob)

        # Entropía del ruido
        HYX = 0

        for i in range(2):
            H = 0

            for prob in M[i]:
                if prob > 0:
                    H -= prob * math.log2(prob)

            HYX += P[i] * H

        # Información mutua
        I = HY - HYX

        if I > capacidad:
            capacidad = I
            probabilidad_optima = P

        p += paso

    return capacidad, probabilidad_optima


M1 = [
    [0.60, 0.40],
    [0.20, 0.80]
]

M2 = [
    [0.25, 0.75],
    [0.90, 0.10]
]

M3 = [
    [0.51, 0.49],
    [0.72, 0.28]
]

M4 = [
    [0.77, 0.23],
    [0.20, 0.80]
]

canales = [M1, M2, M3, M4]

for i in range(len(canales)):
    C, P = capacidad_binaria(canales[i], 0.001)

    print("Canal", i+1)
    print("Capacidad:", C)
    print("Probabilidad a priori:", P)
    print()