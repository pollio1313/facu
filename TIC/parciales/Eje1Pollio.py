"""
Dada el siguiente mensaje emitido por una fuente de información:

Obtener la matriz de transición de la fuente
Determinar si se trata de una fuente de memoria nula o con memoria
Generar la extensión de orden 2 a partir de su distribución estacionaria
Calcular la entropía de la fuente y de la extensión obtenida

CCAABBCCAABBCCAABBCCAABBCCAABB
"""
import math
import random
msj1="CCAABBCCAABBCCAABBCCAABBCCAABB"

def MatrizTransicion(alf,msj):
    Mat=[[0 for _ in range(len(alf))] for _ in range(len(alf))] #lleno la matriz de 0

    #acumula 
    for i in range(len(msj)-1):
        actual = alf.index(msj[i])
        siguiente= alf.index(msj[i+1])
        Mat[actual][siguiente]+=1 

    for i in range(len(alf)):
        total= sum(Mat[i])
        if total!=0:
            for j in range(len(alf)):
                Mat[i][j]/=total
    return Mat

def alfabeto(cad):
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
    comb=sorted(zip(listaA,listaP))
    listaA,listaP=zip(*comb)
    return listaA,listaP

alf1,prob1=alfabeto(msj1)
mat1=MatrizTransicion(alf1,msj1)
print("a) Matriz de transicion (Impresa por columnas) ",mat1)


def tieneMem(M):
    igual=True
    for i in range(len(M)):
        for j in range(len(M)-1):
            if not M[j][i]==M[j+1][i]:
                igual=False
    
    return not igual

if tieneMem(mat1):
    print("b) TIENE MEMORIA")
else:
    print("b) NO TIENE MEMORIA")


def MultVectMat(V,Matriz):
    
    resultado=[]

    for j in range(len(Matriz)):
        suma=0

        for i in range(len(V)):
            suma+= V[i]* Matriz[i][j]
        resultado.append(suma)

    return resultado

def estacionario(Matriz):
    V=[1/len(Matriz)] * len(Matriz) #lleno el vector con equiprobable
    
    nuevo = MultVectMat(V,Matriz)
    iguales = False
    while not iguales:
        V=nuevo
        nuevo=MultVectMat(V,Matriz)
        iguales=True
        for i in range(len(V)):
            if abs(V[i]-nuevo[i])>=0.001:
                iguales=False
    return nuevo

Vestacionario1=estacionario(mat1)
print("c) Vector estacionario ",Vestacionario1)

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
                NuevoP.append(round(Probant[x]*ListaP[y],4))
    return NuevoAlfabeto,NuevoP


Nuevoalf,NuevaP=extenderNrecur(alf1,Vestacionario1,2)
print("d) extension orden 2",extenderNrecur(alf1,Vestacionario1,2))

def entropiaVe(Ve,Ma):
    suma=0
    for j in range(len(Ma)):
        sant=suma
        for i in range(len(Ve)):
            if Ma[j][i]!=0:
                suma+= Ve[j]*Ma[j][i]*math.log2(1/Ma[j][i])
    return suma

print("e) entropia(S):",entropiaVe(Vestacionario1,mat1))
def entropia(l):                #espera una lista de probabilidades
    acum=0
    for i in l:
        entro = i * math.log2(1/i)
        acum= acum+entro
    return acum
print("f) entropia(2S):",entropia(NuevaP))

