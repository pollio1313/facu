"""11. Dadas dos listas paralelas que contengan 
las palabras código de una codificación y sus respectivas probabilidades, 
codificar funciones en Python que calculen:
a. la entropía de la fuente
b. la longitud media del código"""

import math

def Longitud(Prob,cod):
    for i in range(len(Prob)):
        sum=Prob[i]*len(cod[i])
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





cod4=['.,',';',',,',':','...',',:;']
prob=[0.1,0.5,0.1,0.2,0.05,0.05]
print("entropia:",entropiaR(prob,len(alfabetocod(cod4))),"\n longitud media: ",Longitud(prob,cod4))
