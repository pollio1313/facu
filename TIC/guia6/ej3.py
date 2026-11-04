"""1. Un canal recibe mensajes construidos con un alfabeto de tres símbolos A = { a, b, c } 
y genera una salida mediante un alfabeto de dos símbolos B = { 0,1 }. 
La entrada del canal se caracteriza por la siguiente secuencia: abcacaabbcacaabcacaaabcaca,
que genera la siguiente secuencia de salida: 01010110011001000100010011.
Determinar las probabilidades a priori y la matriz del canal."""

import math
import random

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

entrada1="1101011001101010010101010100011111"
entrada2="110101100110101100110101100111110011"
salida1="1001111111100011101101010111110110"
salida2="110021102110022010220121122100112011"


def prob_priori(entrada):
    probabilidades={}
    total=len(entrada)
    for simbolo in entrada:
        if simbolo not in probabilidades:
            probabilidades[simbolo] = entrada.count(simbolo)/total

    return probabilidades

def abecedario(entrada):
    return sorted(set(entrada))




print(matriz_canal(entrada1,salida1),"\n    ",prob_priori(entrada1))
print(matriz_canal(entrada2,salida2),"\n    ",prob_priori(entrada2))
