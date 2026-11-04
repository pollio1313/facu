
import math


Ppriori1=[ 2/5, 3/5 ]
mat1=[[3/5,2/5],[1/3,2/3]]

Ppriori2=[3/4, 1/4 ]
mat2=[[2/3,1/3],[1/10,9/10]]

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

print("Hpriori1:",H_priori(Ppriori1))
print("Hpriori:2",H_priori(Ppriori2))

print("Hpost1:",H_posteriori(Ppriori1,mat1))
print("Hpost2:",H_posteriori(Ppriori2,mat2))


