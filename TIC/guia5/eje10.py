import math
import random

def rlc(cadena):
    if len(cadena) == 0:
        return ""
    
    resultado = ""
    contador = 1

    for i in range(1, len(cadena)):
        if cadena[i] == cadena[i-1]:
            contador+=1
        else:
            resultado += cadena[i-1] + str(contador)
            contador= 1
        
    resultado += cadena[-1]+str(contador)
    return resultado

def tasaCompresion (mensaje,codificacion):
    tam_original = len(mensaje.encode("utf-8"))
    tam_comprimido = len(codificacion)

    if tam_comprimido ==0:
        return 0
    
    return tam_original/ tam_comprimido

msj1="XXXYZZZZ"
msj2="AAAABBBCCDAA"
msj3="UUOOOOAAAIEUUUU"

print(rlc(msj1))
print(rlc(msj2))
print(rlc(msj3))

print(tasaCompresion(msj1,rlc(msj1)))
print(tasaCompresion(msj2,rlc(msj2)))
print(tasaCompresion(msj3,rlc(msj3)))
