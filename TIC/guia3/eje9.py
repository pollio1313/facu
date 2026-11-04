"""9. Dada una lista que contiene las palabras código de una codificación,
 implementar funciones en Python que resuelvan lo siguiente:
a. obtener una cadena de caracteres con el alfabeto código.
b. generar otra lista con las longitudes de las palabras (utilizar comprensión de listas).
c. calcular la sumatoria de la inecuación de Kraft (utilizar las funciones anteriores)."""
import math


def alfabetocod(cad):
    listaA=[]
    for i in cad:
        if not (i in listaA):
            listaA.append(i)
    return listaA

def Longitud(Prob,cod):
    for i in range(len(Prob)):
        sum=Prob[i]*len(cod[i])
    return sum

def LongitudesChicas(cod):
    listaLi=[]
    for i in cod:
        listaLi.append(len(i))
    return listaLi

def SumatoriaKraft(cod):
    r=len(alfabetocod(cod))
    l=LongitudesChicas(cod)
    sum=0
    for i in l:
        sum+= r**(-i)
    return sum



cod2msj=')[]]]([[()]([)]'
cod2=[')','[]',']]','([','[()]','([)]']

print("alfabetoCodigo:",alfabetocod(cod2msj)," \nLongitud",LongitudesChicas(cod2),"\n SumatoriaKraft:",SumatoriaKraft(cod2))
