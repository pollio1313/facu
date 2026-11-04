"""12. Obtener las entropías a priori y a posteriori de los canales de los ejercicios 1, 3 y 6."""

import math
import random

entrada="abcacaabbcacaabcacaaabcaca"
salida="01010110011001000100010011"
entrada1="1101011001101010010101010100011111"
entrada2="110101100110101100110101100111110011"
salida1="1001111111100011101101010111110110"
salida2="110021102110022010220121122100112011"
mat6=[[0.4,0.4,0.2],[0.3,0.2,0.5],[0.3,0.4,0.3]]
prob6=[0.3,0.3,0.4]
def abecedario(entrada):
    return sorted(set(entrada))

def matriz_canal (entrada,salida):      #me devuelve de a filas
    simbolos_entrada= sorted(set(entrada))
    simbolos_salida=sorted(set(salida))
    matriz=[]

    for x in simbolos_entrada:
        fila=[]

        for y in simbolos_salida:
            cantidad=0
            total=0
            for i in range(len(entrada)):
                if entrada[i]==x:
                    total+=1
                    if salida[i]==y:
                        cantidad +=1
            if total >0:
                fila.append(cantidad/total)
            else:
                fila.append(0)
        
        matriz.append(fila)
    
    return matriz

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

def prob_priori(entrada):
    alfabeto= sorted (set(entrada))
    total= len(entrada)
    probabilidades = []

    for simbolo in alfabeto:
        probabilidades.append(entrada.count(simbolo)/total)

    return alfabeto,probabilidades

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

alf,prob=prob_priori(entrada)
mat=matriz_canal(entrada,salida)

alf,prob1=prob_priori(entrada1)
mat1=matriz_canal(entrada1,salida1)

alf,prob2=prob_priori(entrada2)
mat2=matriz_canal(entrada2,salida2)

print("1)",H_posteriori(prob,mat))
print("3)",H_posteriori(prob1,mat1))
print("3)",H_posteriori(prob2,mat2))
print("6)",H_posteriori(prob6,mat6))
