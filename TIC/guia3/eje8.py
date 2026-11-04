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

"""def Longitud(Prob,cod):
    for i in range(len(Prob)):
        sum=Prob[i]*len(cod[i])
    return sum

def entropiaR(l,r):
    acum=0
    
    for i in l:
        entro = i * math.log(1/l,r)
        acum= acum+entro
    return acum
"""


cod1=['==','<','<=','>','>=','<>']
cod2=[')','[]',']]','([','[()]','([)]']
cod3=['/','*','-','*','++','+-']
cod4=['.,',';',',,',':','...',',:;']
prob={0.1,0.5,0.1,0.2,0.05,0.05}
print("NS=",NoSingular(cod1),"  UD=",Univocamente(cod1),"  In=",instantaneo(cod1))
print("NS=",NoSingular(cod2),"  UD=",Univocamente(cod2),"  In=",instantaneo(cod2))
print("NS=",NoSingular(cod3),"  UD=",Univocamente(cod3),"  In=",instantaneo(cod3))
print("NS=",NoSingular(cod4),"  UD=",Univocamente(cod4),"  In=",instantaneo(cod4))
#print("L=",Longitud(prob,cod1),"  Hr=",entropiaR(prob,3))