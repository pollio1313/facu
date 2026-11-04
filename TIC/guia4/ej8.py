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

P=[0.2,0.15,0.1,0.3,0.25]
C1=["01","111","110","101","100"]
C2=["00","01","10","110","111"]
C3=["0110","010","0111","1","00"]
C4=["11","001","000","10","01"]

print(rendimientoRedundancia(C1,P),"\n",rendimientoRedundancia(C2,P),"\n",rendimientoRedundancia(C3,P),"\n",rendimientoRedundancia(C4,P),"\n")
