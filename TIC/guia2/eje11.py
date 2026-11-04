#En base a las fuentes del ejercicio 4, generar las extensiones de orden 2 y 3, 
#calcular sus entropías a partir de sus probabilidades y verificar que H (Sn) = n * H(S).

import math
from itertools import product
a =['x','y','z']
b =['0','1']
c= ['A','B','C','D']
p1=[0.5, 0.1, 0.4]
p2=[0.5, 0.5]
p3=[0.1, 0.3, 0.4, 0.2]



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

def entropiaExt(lProb):
    H=0
    for i in lProb:
        H+=i*math.log2(1/i)
    return H


aExt2,p1Ext2= extenderNrecur(a,p1,2)
aExt3,p1Ext3= extenderNrecur(a,p1,3)
bExt2,p2Ext2= extenderNrecur(b,p2,2)
bExt3,p2Ext3= extenderNrecur(b,p2,3)
cExt2,p3Ext2= extenderNrecur(c,p3,2)
cExt3,p3Ext3= extenderNrecur(c,p3,3)

print("\nH(a2)=",entropiaExt(p1Ext2),"\nH(b2)=",entropiaExt(p2Ext2),"\nH(c2)=",entropiaExt(p3Ext2))
print("\nH(a3)=",entropiaExt(p1Ext3),"\nH(b3)=",entropiaExt(p2Ext3),"\nH(c3)=",entropiaExt(p3Ext3))