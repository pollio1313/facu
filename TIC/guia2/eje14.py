"""Dada una matriz de transición (lista de listas), implementar funciones en Python que resuelvan lo siguiente:
a. generar una lista que represente el vector estacionario de la fuente.
b. calcular la entropía de la fuente (utilizar la función anterior)."""


import math

def MultVectMat(V,Matriz):
    
    resultado=[]

    for j in range(len(Matriz)):
        suma=0

        for i in range(len(V)):
            suma+= V[i]* Matriz[i][j]
        resultado.append(suma)

    return resultado

def estacionario(Matriz):
    V=[1/len(Matriz)] * len(Matriz) #lleno el vector con equiprobable
    
    nuevo = MultVectMat(V,Matriz)
    iguales = False
    while not iguales:
        V=nuevo
        nuevo=MultVectMat(V,Matriz)
        iguales=True
        for i in range(len(V)):
            if abs(V[i]-nuevo[i])>=0.001:
                iguales=False
        print("   V:",nuevo,"\n")
    return nuevo

def entropiaVe(Ve,Ma):
    suma=0
    for j in range(len(Ma)):
        sant=suma
        for i in range(len(Ve)):
            suma+= Ve[j]*Ma[j][i]*math.log2(1/Ma[j][i])
        print("   ",suma-sant)
    return suma

Ma=[[0.3,0.5,0.2],[0.1,0.7,0.2],[0.2,0.3,0.5]]
Ve=estacionario(Ma)
print("M:",Ma,"\nV:",Ve)
print ("H=",entropiaVe(Ve,Ma))
            