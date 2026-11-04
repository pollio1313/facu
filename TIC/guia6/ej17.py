import math
import random

# CANAL 1
C1_P = [1/4, 1/4, 1/4, 1/4]

C1_M = [
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0]
]


# CANAL 2
C2_P = [1/3, 1/3, 1/3]

C2_M = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.2, 0.0, 0.8],
    [0.0, 0.0, 1.0, 0.0]
]


# CANAL 3
C3_P = [1/3, 1/3, 1/3]

C3_M = [
    [0.3, 0.5, 0.2],
    [0.2, 0.3, 0.5],
    [0.5, 0.2, 0.3]
]


# CANAL 4
C4_P = [1/4, 1/4, 1/4, 1/4]

C4_M = [
    [0.0, 0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]


def analizar_canal(M):
    determinante = True
    sin_ruido = True

    # Verificar si es determinante (filas)
    for fila in M:
        salidas = 0

        for p in fila:
            if p > 0:
                salidas += 1

        if salidas > 1:
            determinante = False

    # Verificar si no tiene ruido (columnas)
    for j in range(len(M[0])):
        entradas = 0

        for i in range(len(M)):
            if M[i][j] > 0:
                entradas += 1

        if entradas > 1:
            sin_ruido = False

    if determinante and sin_ruido:
        print("Ambos")
    elif determinante:
        print("Determinante")
    elif sin_ruido:
        print("Sin ruido")
    else:
        print("Ninguno")

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
# Matriz de probabilidades conjuntas
def conjunta(P, M):
    J = []

    for i in range(len(P)):
        fila = []

        for j in range(len(M[0])):
            fila.append(P[i] * M[i][j])

        J.append(fila)

    return J

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

analizar_canal(C1_M)
print("ruido: ",ruido_15(C1_P,C1_M),"  perdida: ",equivocacion_15(C1_P,C1_M)," Info: ",informacion_15(C1_P,C1_M),"\n")
analizar_canal(C2_M)
print("ruido: ",ruido_15(C2_P,C2_M),"  perdida: ",equivocacion_15(C2_P,C2_M)," Info: ",informacion_15(C2_P,C2_M),"\n")
analizar_canal(C3_M)
print("ruido: ",ruido_15(C3_P,C3_M),"  perdida: ",equivocacion_15(C3_P,C3_M)," Info: ",informacion_15(C3_P,C3_M),"\n")
analizar_canal(C4_M)
print("ruido: ",ruido_15(C4_P,C4_M),"  perdida: ",equivocacion_15(C4_P,C4_M)," Info: ",informacion_15(C4_P,C4_M),"\n")