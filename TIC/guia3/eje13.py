"""13. Construir posibles códigos compactos para las siguientes fuentes:
a. utilizando el alfabeto código binario
b. utilizando el siguiente alfabeto código: X = { 1, 2, 3 }"""

import math

alf1=['A','B','C','D']
prob1=[0.5,0.25,0.125,0.125]
alf2=[1,2,3,4]
prob2=[0.333,0.333,0.167,0.167]

def LongitudesChicas(cod):
    listaLi=[]
    for i in cod:
        listaLi.append(len(i))
    return listaLi


def alfabetocod(cad):       #entran el codigo y sale una lista con los caracteres
    listaA=[]
    for k in cad:
        for i in k:
            if not (i in listaA):
                listaA.append(i)
    return listaA

def SumatoriaKraft(cod):
    r=len(alfabetocod(cod))
    l=LongitudesChicas(cod)
    sum=0
    for i in l:
        sum+= r**(-i)
    return sum




def NoSingular(C):
    if len(C)==len(set(C)):
        nosing=True
    else:
        nosing=False
    return nosing


#c
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


def instantaneo (C):
    insta=True
    for x in C:
        for y in C:
            if x.startswith(y) and x!=y:
                insta=False
    return insta

def Informacion(probabilidad):          #espera un solo valor de probabilidad
    info = math.log2(1/probabilidad)
    return info

def compacto(C,prob):
    EsCompacto=True

    for i in range(len(prob)):
        if not(round(Informacion(prob[i]))>=len(C[i])):
            EsCompacto=False
    return EsCompacto


codigo1=['0','10','110','111']
codigob=['1','21','3','23']
print("sumatoria de kraft: ",SumatoriaKraft(codigo1))
print("NS:",NoSingular(codigo1),"   UD:",Univocamente(codigo1),"   INST:",instantaneo(codigo1))
print("Compacto:",compacto(codigob,prob2))


