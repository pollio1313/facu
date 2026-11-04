""" Codificar funciones en Python que resuelvan los siguiente:
a. Dada una cadena de caracteres que representa un mensaje emitido por una fuente, devolver una lista con su alfabeto y su matriz de transición.
b. Dados un número entero N, una lista que contenga el alfabeto de una fuente y su matriz de transición, simular la generación de una cadena de caracteres de longitud N emitida por esa fuente.
c. Dada una matriz de transición y una tolerancia máxima, determinar si se trata de una fuente de memoria nula o una fuente con memoria.
"""
import math
import random
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

def generarMsj(N,alf,M):
    mensaje=""

    #simbolo inicial
    estado=random.randint(0,len(alf)-1)
    mensaje+=alf[estado]

    for i in range(N-1):
        r= random.random()
        acumulada=0
        nuevo_estado=0
        for j in range(len(alf)):
            acumulada+=M[estado][j]
            if r>=acumulada:
                nuevo_estado+=1
        estado=nuevo_estado
        mensaje+=alf[estado]
    return mensaje


msj="ABBCABACYUASUHASDGYWEDHUSYGDSDEESDHUISHDIIISHHEUSHDSSSSSSSSSSSSS"
Alfa,prob=alfabeto(msj)
Mat=MatrizTransicion(Alfa,msj)
print(Alfa,"\n",prob,"\n",Mat)

print("mensaje: ",generarMsj(15,Alfa,Mat))


