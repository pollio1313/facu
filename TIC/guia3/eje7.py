"""Fuente
        Código 1 Código 2 Código 3 Código 4 Código 5 Código 6
S1      011     110         10      1101        011     1110
S2      000     100         1100    10          0111    0
S3      010     101         0101    1111        01      110
S4      101     001         1011    1100        0       1101
S5      001     110         0       1110        011111  1011
S6      100     010         110     0           01111   10
"""


import math


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


S1=["011","000","010","101","001","100"]
S2=["110","100","101","001","110","010"]
S3=["10","1100","0101","1011","0","110"]
S4=["1101","10","1111","1100","1110","0"]
S5=["011","0111","01","0","011111","01111"]
S6=["1110","0","110","1101","1011","10"]
print("NS=",NoSingular(S1),"  UD=",Univocamente(S1),"  In=",instantaneo(S1))
print("NS=",NoSingular(S2),"  UD=",Univocamente(S2),"  In=",instantaneo(S2))
print("NS=",NoSingular(S3),"  UD=",Univocamente(S3),"  In=",instantaneo(S3))
print("NS=",NoSingular(S4),"  UD=",Univocamente(S4),"  In=",instantaneo(S4))
print("NS=",NoSingular(S5),"  UD=",Univocamente(S5),"  In=",instantaneo(S5))
print("NS=",NoSingular(S6),"  UD=",Univocamente(S6),"  In=",instantaneo(S6))