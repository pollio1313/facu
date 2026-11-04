''' Implementar funciones en Python que resuelvan lo siguiente:
a. Dada una cadena de caracteres que representa un mensaje emitido por una fuente de memoria nula,
   devolver dos listas paralelas que contengan:
   el alfabeto de la fuente y las probabilidades de cada símbolo.

b. Dados un número entero N,
 una lista que contenga el alfabeto de una fuente y otra con las probabilidades de cada símbolo, 
 simular la generación de una cadena de caracteres de longitud N emitida por esa fuente.'''



'''no entiendo si tengo q asumir el alfabeto? o considerar como alfabeto todo lo q aparesca en el mensaje'''

import random
def alfabeto(cad):
    listaA=[]
    listaP=[]
    cont=0
    for i in cad:
        cont=cont+1
        if not (i in listaA):
            listaA.append(i)
            listaP.append(1)
        else:
            pos = listaA.index(i)
            listaP[pos] = listaP[pos]+1
    
    for i in range(len(listaP)):
        listaP[i]=listaP[i]/cont
    return listaA,listaP

def simulacion(n,listaA,listaP):
    mensaje = random.choices(listaA,weights=listaP,k=n)
    mensaje = ''.join(mensaje)
    return mensaje




cadena = "buen dia cabezon!, murciegalo, raton, dinosaurio"
listaA,listaP=alfabeto(cadena)
print("alfabeto:",listaA,"\n prob:",listaP,"\n")
n=10
msj=simulacion(n,listaA,listaP)
print("simulacion:",msj)