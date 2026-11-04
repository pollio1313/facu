#ABDAACAABACADAABDAADABDAAABDCDCDCDC, 
#obtener las probabilidades de sus símbolos y calcular la entropía de la fuente.

import math
def alfabeto(cad):    #espera un mensaje y devuelve lista de caracteres y lista de probabilidades
    listaA=[]
    listaP=[]
    cont=0
    for i in cad:
        cont=cont+1
        if not (i in listaA):
            listaA.append(i)
            listaP.append(1)
        else:
            pos = listaA.index(i)
            listaP[pos] = listaP[pos]+1
    
    for i in range(len(listaP)):
        listaP[i]=listaP[i]/cont
    return listaA,listaP

def entropia(l):                #espera una lista de probabilidades
    acum=0
    for i in l:
        entro = i * math.log2(1/i)
        acum= acum+entro
    return acum


mensaje="ABDAACAABACADAABDAADABDAAABDCDCDCDC"
listaC,listaP=alfabeto(mensaje)
print("Caracteres:",listaC,"\nProbabilidades:",listaP)
print("H(S)=",entropia(listaP))