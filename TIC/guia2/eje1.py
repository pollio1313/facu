import math

lista= [0.1,0.2,0.3,0.4]


def Informacion(probabilidad):
    info = math.log2(1/probabilidad)
    return info

def entropia(l):
    acum=0
    for i in l:
        entro = i * math.log2(1/i)
        acum= acum+entro
    return acum

print("la info de P(L[1])=",lista[1],"es : ",Informacion(lista[3]))
print("la entropia de L[1] es:",entropia(lista))
