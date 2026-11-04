"""
12. Calcular la entropía de la fuente y la longitud media de cada código del ejercicio 8.
Analizar los resultados obtenidos en función de su clasificación.
"""

import math


def Longitud(Prob,cod):
    sum=0
    for i in range(len(Prob)):
        sum+=Prob[i]*len(cod[i])
    return sum

def entropiaR(l,r):             #espera la lista de probabilidades y a r que es la base 
    acum=0
    
    for i in l:
        entro = i * math.log((1/i),r)
        
        acum= acum+entro
    return acum

def alfabetocod(cad):       #entran el codigo y sale una lista con los caracteres
    listaA=[]
    for k in cad:
        for i in k:
            if not (i in listaA):
                listaA.append(i)
    return listaA

cod1=['==','<','<=','>','>=','<>']
cod2=[')','[]',']]','([','[()]','([)]']
cod3=['/','*','-','*','++','+-']
cod4=['.,',';',',,',':','...',',:;']
prob=[0.1,0.5,0.1,0.2,0.05,0.05]

print(len(alfabetocod(cod1)),"  H(cod1): ",entropiaR(prob,len(alfabetocod(cod1))))
print(len(alfabetocod(cod2)),"  H(cod2):",entropiaR(prob,len(alfabetocod(cod2))))
print(len(alfabetocod(cod3)),"  H(cod3):",entropiaR(prob,len(alfabetocod(cod3))))
print(len(alfabetocod(cod4)),"  H(cod4):",entropiaR(prob,len(alfabetocod(cod4))))

print("longitusM: ",Longitud(prob,cod1))
print("longitusM: ",Longitud(prob,cod2))
print("longitusM: ",Longitud(prob,cod3))
print("longitusM: ",Longitud(prob,cod4))
