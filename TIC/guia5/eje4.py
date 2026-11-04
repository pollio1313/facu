import math
import random

P=[ 0.385, 0.154, 0.128, 0.154, 0.179 ]

def entropia(l):
    acum=0
    for i in l:
        entro = i * math.log2(1/i)
        acum= acum+entro
    return acum

def shannonFano(probabilidades):
    elementos = []

    for i in range(len(probabilidades)):
        elementos.append([probabilidades[i], i])

    elementos.sort(reverse=True)

    codigo = [""] * len(probabilidades)

    def codificar(grupo, bits):
        if len(grupo) == 1:
            codigo[grupo[0][1]] = bits
            return

        mejorCorte = 1
        menorDiferencia = float("inf")

        for i in range(1, len(grupo)):
            sumaIzquierda = 0
            sumaDerecha = 0

            for j in range(i):
                sumaIzquierda += grupo[j][0]

            for j in range(i, len(grupo)):
                sumaDerecha += grupo[j][0]

            diferencia = abs(sumaIzquierda - sumaDerecha)

            if diferencia < menorDiferencia:
                menorDiferencia = diferencia
                mejorCorte = i

        izquierda = grupo[:mejorCorte]
        derecha = grupo[mejorCorte:]

        codificar(izquierda, bits + "0")
        codificar(derecha, bits + "1")

    codificar(elementos, "")

    return codigo

def huffman(probabilidades):
    nodos = []

    for i in range(len(probabilidades)):
        nodos.append([probabilidades[i], i])

    while len(nodos) > 1:
        nodos.sort(key=lambda nodo: nodo[0])

        menor1 = nodos.pop(0)
        menor2 = nodos.pop(0)

        nuevo = [menor1[0] + menor2[0], menor1, menor2]
        nodos.append(nuevo)

    codigo = [""] * len(probabilidades)

    def recorrer(nodo, bits):
        if len(nodo) == 2:
            codigo[nodo[1]] = bits
        else:
            recorrer(nodo[1], bits + "0")
            recorrer(nodo[2], bits + "1")

    recorrer(nodos[0], "")

    return codigo

def Longitud(Prob,cod):
    sum=0
    for i in range(len(Prob)):
        sum+=Prob[i]*len(cod[i])
    return sum

def rendimientoRedundancia(C,P):
    n=entropia(P)/Longitud(P,C)
    r=1-n
    return n,r

print("a: H(S)=",entropia(P))
print("b: huffman=",huffman(P))
print("c: shannonFano=",shannonFano(P))
print("Lhuff=",Longitud(P,huffman(P)),"Lshann=",Longitud(P,shannonFano(P)))
print(" n y r=",rendimientoRedundancia(huffman(P),P)," n y r=",rendimientoRedundancia(shannonFano(P),P))
