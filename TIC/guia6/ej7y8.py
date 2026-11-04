"""Realizar funciones en Python que reciban como parámetros: 
una lista con las probabilidades a priori y la matriz de probabilidades condicionales del canal, y devuelvan:
a. Una lista con las probabilidades de los símbolos de salida
b. Una matriz con las probabilidades a posteriori del canal
c. Una matriz con las probabilidades de los eventos simultáneos
"""
"""Obtener las probabilidades de los símbolos de salida de los canales propuestos en los ejercicios 1 y 3. 
Comparar los resultados obtenidos de dos maneras distintas: a partir de las secuencias de salida y utilizando
 las probabilidades a priori y la matriz del canal."""


import math
import random

entrada="abcacaabbcacaabcacaaabcaca"
salida="01010110011001000100010011"
entrada1="1101011001101010010101010100011111"
entrada2="110101100110101100110101100111110011"
salida1="1001111111100011101101010111110110"
salida2="110021102110022010220121122100112011"
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

print(matriz_canal(entrada,salida),"\n alf y p:",prob_priori(entrada))
alf,prob=prob_priori(entrada)
mat=matriz_canal(entrada,salida)

alf,prob1=prob_priori(entrada1)
mat1=matriz_canal(entrada1,salida1)

alf,prob2=prob_priori(entrada2)
mat2=matriz_canal(entrada2,salida2)

print(" Ppriori:",probabilidades_salida(prob,mat),"\n Pposterior:",probabilidades_posteriori(prob,mat),"\n Pconjuntas:",probabilidades_conjuntas(prob,mat))


print(" Ppriori:",probabilidades_salida(prob1,mat1),"\n Pposterior:",probabilidades_posteriori(prob1,mat1),"\n Pconjuntas:",probabilidades_conjuntas(prob1,mat1))


print(" Ppriori:",probabilidades_salida(prob2,mat2),"\n Pposterior:",probabilidades_posteriori(prob2,mat2),"\n Pconjuntas:",probabilidades_conjuntas(prob2,mat2))