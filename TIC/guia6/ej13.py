"""13. Calcular las entropías a priori y a posteriori de los siguientes canales:"""
import math


p1=[ 0.14, 0.52, 0.34 ]
p2=[ 0.25, 0.25, 0.50 ]
p3=[ 0.12, 0.24, 0.14, 0.50 ]

mat1=[[0.5,0.3,0.2],[0,0.4,0.6],[0.2,0.8,0]]
mat2=[[0.25,0.25,0.25,0.25],[0.25,0.25,0,0.5],[0.5,0,0.5,0]]
mat3=[[0.25,0.15,0.3,0.3],[0.23,0.27,0.25,0.25],[0.1,0.4,0.25,0.25],[0.34,0.26,0.2,0.2]]

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

def H_priori(P):
    H=0
    for p in P:
        if p>0:
            H-=p*math.log2(p)
    return H

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

print("Hpriori1:",H_priori(p1))
print("Hpriori2:",H_priori(p2))
print("Hpriori3:",H_priori(p3))

print("Hpost1:",H_posteriori(p1,mat1))
print("Hpost2:",H_posteriori(p2,mat2))
print("Hpost3:",H_posteriori(p3,mat3))