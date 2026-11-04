#Dada una fuente binaria sin memoria, calcular la entropía en los siguientes casos e
#interpretar los resultados obtenidos:
#a. ω=0.25 b. ω=0.75 c. ω=0.5 d. ω=1 e. ω=0

import math
def entropiaBinaria(w):
    if (w==0) | (w==1):
        return 0
    else:
        return (w*math.log2(1/w)+(1-w)*math.log2(1/(1-w)))

print("\nHbin(0.25):",entropiaBinaria(0.25),"\nHbin(0.75):",entropiaBinaria(0.75),"\nHbin(0.50):",entropiaBinaria(0.5),"\nHbin(1):",entropiaBinaria(1),"\nHbin(0):",entropiaBinaria(0))

#que seria la interpretacion?

#a
#b
#c  
#d  en este caso solo es probable que ocurra siempre uno de los dos bits, por ende H seria 0
#e  en este caso solo es probable que ocurra siempre uno de los dos bits, por ende H seria 0