"""a. Determinar la entropía a priori y la de la salida
b. Obtener la equivocación o ruido y la pérdida
c. Calcular la entropía afín a través de sus relaciones
d. Verificar la reciprocidad de la información mutua
e. Analizar los resultados obtenidos en cada caso"""
import math 

p1=[0.7,0.3]
p2=[0.5,0.5]
p3=[0.25, 0.50, 0.25 ]
p4=[0.25,0.25,0.25,0.25]
mat1=[[0.7,0.3],[0.4,0.6]]
mat2=[[0.3,0.3,0.4],[0.3,0.3,0.4]]
mat3=[[1.0,0.0,0.0,0.0],[0.0,0.5,0.5,0.0],[0.0,0.0,0.0,1.0]]
mat4=[[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]

def entropia(P):
    H=0
    for p in P:
        if p>0:
            H-=p*math.log2(p)
    return H
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

def ruido(P,M): #H(B/A)
    H=0
    for i in range(len(P)):
        H+=P[i]*entropia(M[i])
    return H


def equivocacion(P,M): #H(A/B)
    salida = probabilidades_salida(P,M)
    entropias=H_posteriori(P,M)

    H=0
    for j in range(len(salida)):
        H+=salida[j]*entropias[j]

    return H

def H_priori(P):
    H=0
    for p in P:
        if p>0:
            H-=p*math.log2(p)
    return H

print("Hpriori1:",H_priori(p1))
print("Hpost1:",H_posteriori(p1,mat1))
print("equi1:",equivocacion(p1,mat1))
print("ruido1:",ruido(p1,mat1))

print("\nHpriori2:",H_priori(p2))
print("Hpost2:",H_posteriori(p2,mat2))
print("equi2:",equivocacion(p2,mat2))
print("ruido2:",ruido(p2,mat2))

print("\nHpriori3:",H_priori(p3))
print("Hpost3:",H_posteriori(p3,mat3))
print("equi3:",equivocacion(p3,mat3))
print("ruido3:",ruido(p3,mat3))

print("\nHpriori3:",H_priori(p4))
print("Hpost3:",H_posteriori(p4,mat4))
print("equi4:",equivocacion(p4,mat4))
print("ruido4:",ruido(p4,mat4))