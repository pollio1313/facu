"""4. Dado un canal binario con entradas equiprobables y
cuyas salidas siempre son iguales a las entradas, obtener las probabilidades de salida, 
a posteriori y de los eventos simultáneos. Analizar los resultados obtenidos."""

import math
import random

def probabilidades_salida(P,M):
    salida=[]

    for j in range(len(M[0])):
        prob=0
        for i in range(len(P)):
            prob += P[i] *M[i][j]
        salida.append(prob)
    return salida


def probabilidades_posteriori(P,M):
    salida=probabilidades_salida(P,M)
    posteriori = []

    for i in range(len(P)):
        fila =[]
        for j in range(len(salida)):
            if salida[j] != 0:
                fila.append(P[i]*M[i][j]/ salida[j])
            else:
                fila.append(0)
        posteriori.append(fila)
    return posteriori

def probabilidades_conjuntas(P,M):
    conjunta=[]
    for i in range(len(P)):
        fila = []
        for j in range(len(M[i])):
            fila.append(P[i]*M[i][j])
        conjunta.append(fila)
    return conjunta


matrizCanal=[[1,0],[0,1]]
prob=[0.5,0.5]
