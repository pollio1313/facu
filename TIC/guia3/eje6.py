"""6. Desarrollar funciones booleaneas en Python que reciban como parámetro una lista con palabras código y verifiquen si el código es:
a. no singular
b. instantáneo
c. unívocamente decodificable"""

import math


def NoSingular(C):
    if len(C)==len(set(C)):
        nosing=True
    else:
        nosing=False
    return nosing


#c
def Univocamente(C):
    
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
        print("S=",S)
        
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
                    if x.startswith(y):
                        sufijo= x[len(y):]
                    if y.startswith(x):
                        sufijo=y[len(x):]
                    if sufijo is not None:
                        nuevo.add(sufijo)
    return UD


def instantaneo (C):
    insta=True
    for x in C:
        for y in C:
            if x.startswith(y) and x!=y:
                insta=False
    return insta


cod1={"010","101","000","111"}
cod2={"110","001","11","00"}
print("es UD=",Univocamente(cod2),"    es Instantaneo= ",instantaneo(cod2))

