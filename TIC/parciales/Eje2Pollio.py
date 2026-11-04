"""Dados la distribución de probabilidades de una fuente y el siguiente código:

Comprobar si cumple la inecuación de Kraft-McMillan
Calcular la entropía de la fuente y la longitud media del código
Determinar si se trata de un código compacto
Proponer otro código compacto con el mismo alfabeto para la fuente"""


import math
import random

p=[1/9, 1/3, 1/9, 1/3, 1/9]
alf=['AB','B','AC','C','AA']
alfconj={'AB','B','AC','C','AA'}
print(p,alf)

def LongitudesChicas(cod):
    listaLi=[]
    for i in cod:
        listaLi.append(len(i))
    return listaLi

def alfabetocod(cad):  
    listaA=[]
    for k in cad:
        for i in k:
            if not (i in listaA):
                listaA.append(i)
    return listaA

def SumatoriaKraft(cod):
    r=len(alfabetocod(cod))
    print("r:",r)
    l=LongitudesChicas(cod)
    print("l:",l)
    sum=0
    for i in l:
        sum+= r**(-i)
    return sum

print("a) ",SumatoriaKraft(alf))

def entropiaR(l,r):             #espera la lista de probabilidades y a r que es la base
    acum=0
    
    for i in l:
        entro = i * math.log((1/i),r)
        acum= acum+entro
    return acum

print("b) Hr:",entropiaR(p,3))

def Longitud(Prob,cod):
    sum=0
    for i in range(len(Prob)):
        sum+=Prob[i]*len(cod[i])
    return sum


print("c) L=",Longitud(p,alf))

def Univocamente(C):
    C=set(C)
    anteriores=[]
    S=set()
    for x in C:
        for y in C:
            if x.startswith(y):
                sufijo= x[len(y):]
            if y.startswith(x):
                sufijo=y[len(x):]
            if sufijo != '':
                S.add(sufijo)
    fin=False
    UD=True
    while (not fin) and S:
        #print("S=",S)
        
        #caso de S interseccion C
        if S & C:
            UD=False
            fin=True
        #caso que un sufijo este en otro S
        elif any(S & anterior for anterior in anteriores):
            UD=True
            fin=True
        else:
            anteriores.append(S)
            nuevo=set()
            for x in S:
                for y in C:
                    #print("x: ",x,"  y: ",y)
                    if x.startswith(y):
                        sufijo= x[len(y):]
                    if y.startswith(x):
                        sufijo=y[len(x):]
                        #print("sufijo:",sufijo)
                    if sufijo !='':
                        nuevo.add(sufijo)
            S=nuevo
    return UD

#revisa si es Insta, hay q verificar los otro por separado
#pasa saber si es instantaneo reviso q ninguna palabra sea prefijo de la otra
def instantaneo (C):
    insta=True
    for x in C:
        for y in C:
            if x.startswith(y) and x!=y:
                insta=False
    return insta
#mismo revisa si es no singular, lo hace viendo si el largo de la lista es igual al largo de la list con un set.
def NoSingular(C):
    if len(C)==len(set(C)):
        nosing=True
    else:
        nosing=False
    return nosing

def compacto(C,prob):
    EsCompacto=True

    for i in range(len(prob)):
        if not(math.ceil(Informacion(prob[i]))>=len(C[i])):
            EsCompacto=False
    return EsCompacto

def Informacion(probabilidad):
    info = math.log2(1/probabilidad)
    return info


print("NoSingular: ",NoSingular(alf),"  UD: ",Univocamente(alfconj),"    Instantaneo: ",instantaneo(alf),"   compacto: ",compacto(alf,p))

