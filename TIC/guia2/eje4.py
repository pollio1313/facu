'''Dadas las siguientes fuentes de memoria nula:
Alfabeto {x, y, z} {0, 1} {A, B, C, D} 
Probabilidades {0.5, 0.1, 0.4} {0.5, 0.5} {0.1, 0.3, 0.4, 0.2}

a. Obtener la cantidad de información de cada símbolo
b. Calcular la entropía de la fuente'''
import math

def Informacion(probabilidad):          #espera un solo valor de probabilidad
    info = math.log2(1/probabilidad)
    return info

def entropia(l):                #espera una lista de probabilidades
    acum=0
    for i in l:
        entro = i * math.log2(1/i)
        acum= acum+entro
    return acum

def InformacionAlfabeto(prob):    #espera una lista de probabilidades
    info=[]
    for i in prob:
        info.append(math.log2(1/i))
    return info

a =['x','y','z']
b =['0','1']
c= ['A','B','C','D']
p1=[0.5, 0.1, 0.4]
p2=[0.5, 0.5]
p3=[0.1, 0.3, 0.4, 0.2]
info1=[]
info2=[]
info3=[]
info1=InformacionAlfabeto(p1)
info2=InformacionAlfabeto(p2)
info3=InformacionAlfabeto(p3)
print("info1:",info1,"\ninfo2:",info2,"\ninfo3:",info3)
print("\n H(a)=",entropia(p1),"   H(b)=",entropia(p2),"   H(c)=",entropia(p3))