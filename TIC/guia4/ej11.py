import math
import random

C1=["0100100","0101000","0010010","0100000"]
C2=["0100100","0010010","0101000","0100001"]
C3=["0110000","0000011","0101101","0100110"]

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

dmin=distancia_minima(C1)
print("Dmin=",dmin,"  alpha: ",DetectarErrores(dmin),"  beta: ",CantCorregible(dmin))
dmin=distancia_minima(C2)
print("Dmin=",dmin,"  alpha: ",DetectarErrores(dmin),"  beta: ",CantCorregible(dmin))
dmin=distancia_minima(C3)
print("Dmin=",dmin,"  alpha: ",DetectarErrores(dmin),"  beta: ",CantCorregible(dmin))
