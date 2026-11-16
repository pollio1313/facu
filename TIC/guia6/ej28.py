"""28. Calcular la probabilidad de error del siguiente canal, utilizando la regla de decisión de
máxima posibilidad. Considerar una distribución uniforme de probabilidades a priori.
0.6 0.4
0.2 0.8
"""
import math


#prob de error pero casos binarios creo
def probabilidad_error(M):
    error = 0
    prob_apriori = 1 / len(M)

    for j in range(len(M[0])):
        mayor = 0
        fila_elegida = 0

        for i in range(len(M)):
            if M[i][j] > mayor:
                mayor = M[i][j]
                fila_elegida = i

        for i in range(len(M)):
            if i != fila_elegida:
                error += prob_apriori * M[i][j]

    return error

M = [
    [0.6, 0.4],
    [0.2, 0.8]
]

error = probabilidad_error(M)

print("Probabilidad de error:", error)
print("Porcentaje de error:", error * 100, "%")