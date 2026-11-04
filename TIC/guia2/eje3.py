'''Suponiendo una fuente de memoria nula, 
dada por el resultado de la tirada de un dado, calcular la entropía en los siguientes casos:
a. Los sucesos son equiprobables
b. Las probabilidades son: P(1) = 1/9, P(2) = 1/6, P(3) = 1/9, P(4) = 1/9, P(5) = 1/6 y
 P(6) = 1/3'''
import math

probabilidades=[1/6,1/6,1/6,1/6,1/6,1/6]
prob2= [1/9,1/6,1/9,1/9,1/6,1/3]
def entropiaH(P):
    entro=0
    for i in P:
        entro=entro + i * math.log2(1/i)
    return entro

print("H(S):",entropiaH(probabilidades))
print("\nH(S):",entropiaH(prob2))
