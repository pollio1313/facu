import math
import random



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
    print(entropia(P)," < ",Longitud(P,S)," < ",entropia(P)+1)



S=["BA","CAB","A","CBA"]
P=[0.3,0.1,0.4,0.2]

S2,P2=extenderNrecur(S,P,3)

shanonN(S2,P2,3)

