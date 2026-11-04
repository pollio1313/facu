#Desarrollar una función en Python que reciba:
#  una lista con el alfabeto de una fuente,
#  otra con su distribución de probabilidades y un número entero N. 
# Esta función debe generar dos nuevas listas con la extensión de orden N y su distribución de probabilidades.
import math

c= ['A','B','C','D']
p3=[0.1, 0.3, 0.4, 0.2]

def entropia(l):
    acum=0
    for i in l:
        entro = i * math.log2(1/i)
        acum= acum+entro
    return acum


def extenderNrecur(ListaC,ListaP,n):
    NuevoAlfabeto=[]
    NuevoP=[]
    if n== 1:
        return ListaC,ListaP
    else:
        ant,Probant=extenderNrecur(ListaC,ListaP,n-1)
        for x in range(len(ant)):
            for y in range(len(ListaC)):
                NuevoAlfabeto.append(ant[x]+ListaC[y])
                NuevoP.append(Probant[x]*ListaP[y])
    return NuevoAlfabeto,NuevoP



listaCext,listaPext=extenderNrecur(c,p3,4)
print("\nListaExt=",listaCext)
print("\n listaP=",listaPext)