import math
import random



#ayuda


P=[0.5,0.2,0.3]
C1=["11","010","00"]
C2=["10","001","110","0000","0001","111","0110","0111"]

def extenderNrecur(ListaC,ListaP,n):
    NuevoAlfabeto=[]
    NuevoP=[]
    if n== 1:
        return ListaC,ListaP
    else:
        ant,Probant=extenderNrecur(ListaC,ListaP,n-1)
        for x in range(len(ant)):
            for y in range(len(ListaC)):
                NuevoAlfabeto.append(ant[x]+ListaC[y])
                NuevoP.append(Probant[x]*ListaP[y])
    return NuevoAlfabeto,NuevoP

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

def shanonN(S,P,n):
    S2,P2=extenderNrecur(S,P,n)
    print("n=1      ",entropia(P)," < ",Longitud(P,S)/n," < ",entropia(P)+1/n)
    print("n=2      ",entropia(P2)," < ",Longitud(P2,S2)," < ",entropia(P2)+1)

def shanon(S,Sextendido,P,Pextendido,n):
    print("n=1      ",entropia(P)," < ",Longitud(P,S)/n," < ",entropia(P)+1/n)
    print("n=2      ",entropia(Pextendido)," < ",Longitud(Pextendido,Sextendido)," < ",entropia(Pextendido)+1)

shanonN(C1,P,2)
shanon(C1,C2,P,P,2)