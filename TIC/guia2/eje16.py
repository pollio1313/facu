"""16. Para cada uno de los siguientes mensajes, estimar si podría haber sido emitido por una
fuente de memoria nula o una fuente con memoria y calcular su entropía: 
a. .;.:.:.::;:,::.;:,::,;,:;.:.;.;;:,.::.:,.:.;:::::.
b. +-/+/-//-/*-/**-*---////-+--*+*/-----/--+/++--*/-+
c. ]]]([[]))([(])]([]([([([)([([([[([))][([([[([)([(]
d. ;;,;,;:,,,.;,,.,,,::,;;;,:;.,,;:,,,:..;,;;.,;,,.:; 
e. -+-+*//++///*/-////+---////-+/+--+-+/-/+-+/-+*++// 
f. )[))[([()))()[[]](([[)))])))][))(][)[[[)()]))[)[])"""

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

def tieneMem(M):                        #esta bien esto?
    igual=True
    for i in range(len(M)):
        for j in range(len(M)-1):
            if not M[j][i]==M[j+1][i]:
                igual=False
    
    return not igual

def MultVectMat(V,Matriz):   #esta funcion la usa el estacionario, no hay q llamarla
    
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
        print("   V:",nuevo,"\n")
    return nuevo

def entropiaVe(Ve,Ma):
    suma=0
    for j in range(len(Ma)):
        sant=suma
        for i in range(len(Ve)):
            if Ma[j][i]!=0:
                suma+= Ve[j]*Ma[j][i]*math.log2(1/Ma[j][i])
        print("   ",suma-sant)
    return suma



"""las 3 de moemoria nula, me dieron 1,8424 creo q algo hice mal, las respuestas son 1,86 1,85 1,84"""
mensaje1=";;,;,;:,,,.;,,.,,,::,;;;,:;.,,;:,,,:..;,;;.,;,,.:;"
Alfabeto1,_=alfabeto(mensaje1)
Matriz1=MatrizTransicion(Alfabeto1,mensaje1)
VectorEstacionario1=estacionario(Matriz1)
Entropia1=entropiaVe(VectorEstacionario1,Matriz1)


print("Alffabeto1:",Alfabeto1,"\nMatriz1:",Matriz1)
if tieneMem(Matriz1):
    print("TIENE MEMORIA")
else:
    print("NO")
print("\nVectorEstacionario1: ",VectorEstacionario1,"\nH1:",Entropia1)
