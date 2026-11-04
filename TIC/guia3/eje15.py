"""15. Verificar si los códigos del ejercicio 8 son compactos y obtener conclusiones de acuerdo a
los resultados obtenidos previamente."""
import math


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




cod1=['==','<','<=','>','>=','<>']
cod2=[')','[]',']]','([','[()]','([)]']
cod3=['/','*','-','*','++','+-']
cod4=['.,',';',',,',':','...',',:;']
prob={0.1,0.5,0.1,0.2,0.05,0.05}
probS=[0.1,0.5,0.1,0.2,0.05,0.05]
print("NS=",NoSingular(cod1),"  UD=",Univocamente(cod1),"  In=",instantaneo(cod1),"  Comp=",compacto(cod1,probS))
print("NS=",NoSingular(cod2),"  UD=",Univocamente(cod2),"  In=",instantaneo(cod2),"  Comp=",compacto(cod2,probS))
print("NS=",NoSingular(cod3),"  UD=",Univocamente(cod3),"  In=",instantaneo(cod3),"  Comp=",compacto(cod3,probS))
print("NS=",NoSingular(cod4),"  UD=",Univocamente(cod4),"  In=",instantaneo(cod4),"  Comp=",compacto(cod4,probS))

#El unico que es instanteno y puede verse si es compacto es el ultimo, alguno de los priemros no llegan ni a NS


