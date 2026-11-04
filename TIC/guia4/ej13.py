import math
import random

def revisaParidad(matriz):
    errores=[]
    filas =len(matriz)
    columnas = len (matriz[0])
    #verifica filas 
    for i in range(filas):
        if matriz[i].count("1") % 2 !=0:
            errores.append(("fila",i))
    #verifica columnas
    for j in  range(columnas):
        unos =0

        for i in range(filas):
            if matriz[i][j] == "1":
                unos +=1
        
        if unos % 2 !=0:
            errores.append(("columna",j))
    
    return len(errores) == 0,errores

def corregirParidad(matriz,fila_error,columna_error):
    matriz=list(matriz)

    fila = list(matriz[fila_error])
    if fila[columna_error]=="0":
        fila[columna_error]="1"
    else:
        fila[columna_error]="0"

    matriz[fila_error]= "".join(fila)
    return matriz

def matriz_a_ascii(matriz):
    palabra =""
    for fila in matriz:
        bits=fila[:-1]
        numero= int(bits,2)
        palabra+=chr(numero)
    return palabra

a=["00100001","10000111","10000010","10100110","10000010"]
b=["00101101","10011001","10001010","10011100","10000010"]
c=["00101010","10000010","10011010","10011111","10100101"]
d=["00010100","10010000","10011110","10011001","10000010"]
e=["00110101","10011010","10101011","10100100","10000010"]
f=["00001001","10101001","10100101","10001011","10100110"]
g=["00011101","10010011","10011101","10001100","10011111"]
h=["00111110","10000111","10010000","10000010","10101010"]
print(revisaParidad(a))
print(revisaParidad(b))
print(revisaParidad(c))
print(revisaParidad(d))
print(revisaParidad(e))
print(revisaParidad(f))
print(revisaParidad(g))
print(revisaParidad(h))

b=corregirParidad(b,2,2)
c=corregirParidad(c,0,4)

print(matriz_a_ascii(a)," ",matriz_a_ascii(b)," ",matriz_a_ascii(c))        #porq no esta la repsuesta