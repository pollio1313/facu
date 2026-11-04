"""10. Calcular las sumatorias de la inecuación de Kraft de los códigos de los ejercicios 7 y 8. 
Analizar los resultados obtenidos en función de su clasificación.
"""
import math


def LongitudesChicas(cod):
    listaLi=[]
    for i in cod:
        listaLi.append(len(i))
    return listaLi

def alfabetocod(cad):       #entran el codigo y sale una lista con los caracteres
    listaA=[]
    for k in cad:
        for i in k:
            if not (i in listaA):
                listaA.append(i)
    return listaA


def SumatoriaKraft(cod):
    r=len(alfabetocod(cod))
    l=LongitudesChicas(cod)
    sum=0
    for i in l:
        sum+= r**(-i)
    return sum


S1=["011","000","010","101","001","100"]
S2=["110","100","101","001","110","010"]
S3=["10","1100","0101","1011","0","110"]
S4=["1101","10","1111","1100","1110","0"]
S5=["011","0111","01","0","011111","01111"]
S6=["1110","0","110","1101","1011","10"]

cod1=['==','<','<=','>','>=','<>']
cod2=[')','[]',']]','([','[()]','([)]']
cod3=['/','*','-','*','++','+-']
cod4=['.,',';',',,',':','...',',:;']

print("cod1: ",SumatoriaKraft(cod1))
print("cod2: ",SumatoriaKraft(cod2))
print("cod3: ",SumatoriaKraft(cod3))
print("cod4: ",SumatoriaKraft(cod4))

print("S1: ",SumatoriaKraft(S1))
print("S2: ",SumatoriaKraft(S2))
print("S3: ",SumatoriaKraft(S3))
print("S4: ",SumatoriaKraft(S4))
print("S5: ",SumatoriaKraft(S5))
print("S6: ",SumatoriaKraft(S6))