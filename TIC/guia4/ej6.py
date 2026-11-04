import math
import random

def entropia(l):
    acum=0
    for i in l:
        entro = i * math.log2(1/i)
        acum= acum+entro
    return acum
def Longitud(Prob,cod):
    sum=0
    for i in range(len(Prob)):
        sum+=Prob[i]*len(cod[i])
    return sum

def rendimientoRedundancia(C,P):
    n=entropia(P)/Longitud(P,C)
    r=1-n
    return n,r

P=[0.5,0.2,0.3]
C1=["11","010","00"]
C2=["10","001","110","0000","0001","111","0110","0111"]

print(rendimientoRedundancia(C1,P))
