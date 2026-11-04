#Realizar una función en Python que reciba como parámetro el valor ω de una fuente binaria de memoria nula y,
#utilizando las funciones desarrolladas en el ejercicio 1, calcule la entropía de la fuente.

import math

def entropiaBinaria(w):
    return (w*math.log2(1/w)+(1-w)*math.log2(1/(1-w)))


print("entropia fuente Binaria:",entropiaBinaria(0.3))