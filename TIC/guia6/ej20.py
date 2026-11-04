
import math

# ==========================================
# FUNCIONES GENERALES
# ==========================================

def entropia(P):
    H = 0

    for p in P:
        if p > 0:
            H -= p * math.log2(p)

    return H


def probabilidades_salida(M, P):
    salida = []

    for j in range(len(M[0])):
        suma = 0

        for i in range(len(M)):
            suma += P[i] * M[i][j]

        salida.append(suma)

    return salida


def equivocacion(M, P):
    conjunta = []

    for i in range(len(M)):
        fila = []

        for j in range(len(M[i])):
            fila.append(P[i] * M[i][j])

        conjunta.extend(fila)

    py = probabilidades_salida(M, P)

    return entropia(conjunta) - entropia(py)


def informacion_mutua(M, P):
    Hx = entropia(P)
    He = equivocacion(M, P)

    return Hx - He


def canal_compuesto(M1, M2):
    resultado = []

    for i in range(len(M1)):
        fila = []

        for j in range(len(M2[0])):
            suma = 0

            for k in range(len(M2)):
                suma += M1[i][k] * M2[k][j]

            fila.append(suma)

        resultado.append(fila)

    return resultado


def mostrar_matriz(M):
    for fila in M:
        print(["{:.4f}".format(x) for x in fila])


# ==========================================
# DATOS DEL EJERCICIO
# ==========================================

P1 = [0.5, 0.5]

M1 = [
    [0.7, 0.0, 0.3, 0.0],
    [0.2, 0.6, 0.0, 0.2]
]

M2 = [
    [0.9, 0.0, 0.1],
    [0.0, 1.0, 0.0],
    [0.1, 0.1, 0.8],
    [0.0, 0.5, 0.5]
]


# ==========================================
# 1. EQUIVOCACION E INFORMACION MUTUA
# ==========================================

print("========== CANAL 1 ==========")

E1 = equivocacion(M1, P1)
I1 = informacion_mutua(M1, P1)

print("Equivocacion:", E1)
print("Informacion mutua:", I1)


print("\n========== CANAL 2 ==========")

# La priori del segundo canal es la salida del primero
P2 = probabilidades_salida(M1, P1)

print("Probabilidades a priori:", P2)

E2 = equivocacion(M2, P2)
I2 = informacion_mutua(M2, P2)

print("Equivocacion:", E2)
print("Informacion mutua:", I2)


# ==========================================
# 2. MATRIZ DEL CANAL COMPUESTO
# ==========================================

print("\n========== CANAL COMPUESTO ==========")

MC = canal_compuesto(M1, M2)

mostrar_matriz(MC)


# ==========================================
# 3. EQUIVOCACION E INFORMACION MUTUA
#    DEL CANAL COMPUESTO
# ==========================================

print("\n========== RESULTADOS COMPUESTO ==========")

EC = equivocacion(MC, P1)
IC = informacion_mutua(MC, P1)

print("Equivocacion:", EC)
print("Informacion mutua:", IC)


# ==========================================
# 4. COMPARACION DE RESULTADOS
# ==========================================

print("\n========== COMPARACION ==========")

print("Equivocacion canal 1:", E1)
print("Equivocacion canal 2:", E2)
print("Equivocacion compuesto:", EC)

print("\nInformacion mutua canal 1:", I1)
print("Informacion mutua canal 2:", I2)
print("Informacion mutua compuesto:", IC)
