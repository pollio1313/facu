import math

M1 = [
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]
M5 = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.2, 0.0, 0.8],
    [0.0, 0.0, 1.0, 0.0]
]
M6 = [
    [0.3, 0.5, 0.2],
    [0.2, 0.3, 0.5],
    [0.5, 0.2, 0.3]
]
M7 = [
    [0.0, 0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]
def capacidad(M, tolerancia=1e-10):
    n = len(M)
    m = len(M[0])

    P = [1/n] * n

    diferencia = 1
    while diferencia > tolerancia:
        Q = [0] * m

        for j in range(m):
            for i in range(n):
                Q[j] += P[i] * M[i][j]

        D = [0] * n

        for i in range(n):
            for j in range(m):
                if M[i][j] > 0 and Q[j] > 0:
                    D[i] += M[i][j] * math.log2(M[i][j] / Q[j])

        nueva = [P[i] * 2**D[i] for i in range(n)]

        suma = sum(nueva)
        nueva = [p/suma for p in nueva]

        diferencia = max(abs(nueva[i] - P[i]) for i in range(n))
        P = nueva

    Q = [sum(P[i] * M[i][j] for i in range(n)) for j in range(m)]

    I = 0
    for i in range(n):
        for j in range(m):
            if M[i][j] > 0 and Q[j] > 0:
                I += P[i] * M[i][j] * math.log2(M[i][j] / Q[j])

    return I


print("Información mutua:", capacidad(M1), "bits")

print("Información mutua:", capacidad(M5), "bits")

print("Información mutua:", capacidad(M6), "bits")

print("Información mutua:", capacidad(M7), "bits")