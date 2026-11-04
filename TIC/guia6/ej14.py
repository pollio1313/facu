import math
import random

#espera las probabilidades de la fuente y devuevle al entropia de la fuente es decir PRIORI
def entropia(probabilidades):
    h = 0

    for p in probabilidades:
        if p > 0:
            h -= p * math.log2(p)

    return h

#espera las probabilidades de la fuente y la amtriz del canal y te devuelve la entropia a POSTERIORI, es decir la entropia despues de pasar por el canal
def entropia_salida(probabilidades, matriz):
    salida = []

    for j in range(len(matriz[0])):
        p = 0

        for i in range(len(probabilidades)):
            p += probabilidades[i] * matriz[i][j]

        salida.append(p)

    return entropia(salida)
#H(B/A)
def ruido(probabilidades, matriz):
    h = 0

    for i in range(len(probabilidades)):
        h += probabilidades[i] * entropia(matriz[i])

    return h
#H(A/B)
def equivocacion(probabilidades, matriz):
    h = 0

    for j in range(len(matriz[0])):
        py = 0

        for i in range(len(probabilidades)):
            py += probabilidades[i] * matriz[i][j]

        if py > 0:
            posteriori = []

            for i in range(len(probabilidades)):
                posteriori.append(probabilidades[i] * matriz[i][j] / py)

            h += py * entropia(posteriori)

    return h

def informacion(probabilidades, matriz):
    return entropia(probabilidades) - equivocacion(probabilidades, matriz)

def entropia_conjunta(PA, matriz):
    HA = entropia(PA)
    HB = entropia_salida(PA, matriz)
    I = informacion(PA, matriz)

    return HA + HB - I


C1_P = [0.70, 0.30]
C1_M = [
    [0.7, 0.3],
    [0.4, 0.6]
]

C2_P = [0.50, 0.50]
C2_M = [
    [0.3, 0.3, 0.4],
    [0.3, 0.3, 0.4]
]

C3_P = [0.25, 0.50, 0.25]
C3_M = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.5, 0.5, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]

C4_P = [0.25, 0.25, 0.25, 0.25]
C4_M = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
]

print("--------------CANAL 1------------")
print("a)Hpriori:",entropia(C1_P),"  Hsalida:",entropia_salida(C1_P,C1_M))
print("b)ruido:",ruido(C1_P,C1_M),"  equivocacion:",equivocacion(C1_P,C1_M))
print("c)H(A,B):",entropia_conjunta(C1_P,C1_M))
print("I(A,B)=I(B,A)  ",informacion(C1_P,C1_M)," = ",entropia_salida(C1_P,C1_M)-ruido(C1_P,C1_M))

print("--------------CANAL 2------------")
print("a)Hpriori:",entropia(C2_P),"  Hsalida:",entropia_salida(C2_P,C2_M))
print("b)ruido:",ruido(C2_P,C2_M),"  equivocacion:",equivocacion(C2_P,C2_M))
print("c)H(A,B):",entropia_conjunta(C2_P,C2_M))
print("I(A,B)=I(B,A)  ",informacion(C2_P,C2_M)," = ",entropia_salida(C2_P,C2_M)-ruido(C2_P,C2_M))


print("--------------CANAL 3------------")
print("a)Hpriori:",entropia(C3_P),"  Hsalida:",entropia_salida(C3_P,C3_M))
print("b)ruido:",ruido(C3_P,C3_M),"  equivocacion:",equivocacion(C3_P,C3_M))
print("c)H(A,B):",entropia_conjunta(C3_P,C3_M))
print("I(A,B)=I(B,A)  ",informacion(C3_P,C3_M)," = ",entropia_salida(C3_P,C3_M)-ruido(C3_P,C3_M))


print("--------------CANAL 4------------")
print("a)Hpriori:",entropia(C4_P),"  Hsalida:",entropia_salida(C4_P,C4_M))
print("b)ruido:",ruido(C4_P,C4_M),"  equivocacion:",equivocacion(C4_P,C4_M))
print("c)H(A,B):",entropia_conjunta(C4_P,C4_M))
print("I(A,B)=I(B,A)  ",informacion(C4_P,C4_M)," = ",entropia_salida(C4_P,C4_M)-ruido(C4_P,C4_M))

# CANAL 1:
# Presenta una transmisión poco eficiente, ya que introduce bastante
# incertidumbre tanto en la salida como en la recuperación del mensaje original.
# La información mutua es muy baja, por lo que transmite muy poca información útil.


# CANAL 2:
# Las filas de la matriz son iguales, por lo que la salida es independiente
# de la entrada. Esto significa que conocer el mensaje enviado no aporta
# información sobre el mensaje recibido. No transmite información útil.


# CANAL 3:
# Permite recuperar perfectamente el mensaje original, ya que cada entrada
# produce salidas que no se comparten con otras entradas. Sin embargo,
# introduce incertidumbre porque una de las entradas puede generar dos
# posibles símbolos de salida.


# CANAL 4:
# Es un canal determinista, ya que cada entrada produce siempre una única
# salida. Sin embargo, pierde información porque dos entradas diferentes
# generan el mismo símbolo de salida, impidiendo recuperar siempre
# el mensaje original.