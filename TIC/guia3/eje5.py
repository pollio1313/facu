"""Dados los siguientes códigos para una fuente con un alfabeto de cuatro símbolos, verificar
si son unívocamente decodificables y/o instantáneos:"""


import math



def Univocamente(C):
    
    anteriores=[]
    S=set()
    for x in C:
        for y in C:
            if x.startswith(y):
                sufijo= x[len(y):]
            if y.startswith(x):
                sufijo=y[len(x):]
            if sufijo is not '':
                S.add(sufijo)
    fin=False
    UD=True
    while not fin:
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



cod1={"010","101","000","111"}
cod2={"110","001","11","00"}
print("es UD=",Univocamente(cod2))
