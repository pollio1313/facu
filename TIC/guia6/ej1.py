"""1. Un canal recibe mensajes construidos con un alfabeto de tres símbolos A = { a, b, c } 
y genera una salida mediante un alfabeto de dos símbolos B = { 0,1 }. 
La entrada del canal se caracteriza por la siguiente secuencia: abcacaabbcacaabcacaaabcaca,
que genera la siguiente secuencia de salida: 01010110011001000100010011.
Determinar las probabilidades a priori y la matriz del canal."""

import math
import random

def matriz_canal (entrada,salida):
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

abecedario="abcacaabbcacaabcacaaabcaca"
resultado="01010110011001000100010011"

print(matriz_canal(abecedario,resultado))