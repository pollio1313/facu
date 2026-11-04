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

c1=["00","01","10","11"]
c2=["000","100","101","111"]
c3=["0000","0011","1010","0101"]

print(distancia_minima(c1),"  ",distancia_minima(c2),"  ",distancia_minima(c3),"  ")
print("alpha: ",DetectarErrores(distancia_minima(c1)),"    beta: ",CantCorregible(distancia_minima(c1)),"\n")
print("alpha: ",DetectarErrores(distancia_minima(c2)),"    beta: ",CantCorregible(distancia_minima(c2)),"\n")
print("alpha: ",DetectarErrores(distancia_minima(c3)),"    beta: ",CantCorregible(distancia_minima(c3)),"\n")