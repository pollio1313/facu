import math
import random

def hamming(C1,C2):
    if len(C1) != len(C2):
        return -1
    distancia=0

    for i in range(len(C1)):
        if C1[i] != C2[i]:
            distancia+=1
    
    return distancia

def distancia_minima(C):
    minimo = len(C[0])
    for i in range(len(C)):
        for j in range(i+1,len(C)):
            d=hamming(C[i],C[j])
            if d<minimo:
                minimo=d

    return minimo

def DetectarErrores(dmin):
    return dmin-1

def CantCorregible(dmin):
    return math.floor((dmin-1)/2)

S=["01001001","01111011","11001110","11011101"]
dmin=distancia_minima(S)
print("Dmin=",dmin,"  alpha: ",DetectarErrores(dmin),"  beta: ",CantCorregible(dmin))