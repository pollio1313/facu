"""11. Desarrollar una función en Python que reciba como parámetros:
 una lista con las probabilidades a priori y la matriz de probabilidades condicionales del canal, 
y retorne una lista con las entropías a posteriori."""


import math

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

def H_posteriori(P,M):
    posteriori = probabilidades_posteriori(P,M)
    entropias=[]

    for j in range(len(M[0])):
        H=0

        for i in range(len(M)):
            p=posteriori[i][j]

            if p>0:
                H-=p*math.log2(p)
        entropias.append(H)
    return entropias

