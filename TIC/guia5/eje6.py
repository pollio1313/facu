import math
import random

a="ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB"
b="AOEAOEOOOOEOAOEOOEOOEOAOAOEOEUUUIEOEOEO"

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
    comb=sorted(zip(listaA,listaP))
    listaA,listaP=zip(*comb)
    return listaA,listaP



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

def codificarMensaje(alfabeto,codigo,mensaje):
    bits=""

    for caracter in mensaje:
        posicion = alfabeto.index(caracter)
        bits+= codigo[posicion]
    
    return bits

def decodificarMensaje(alfabeto,codigo,mensaje):
    resultado=""
    actual=""

    for bit in mensaje:
        actual+= bit

        if actual in codigo:
            posicion = codigo.index(actual)
            resultado+= alfabeto[posicion]
            actual=""
    
    return resultado


deco1="ABACBAACABABAACBABA"
deco2= "BACBAAABAAACBABACAB"
deco3="CBAABACBABAAACABABA"

S1,P1=alfabeto(a)
print("S:",S1," ShannonFano: ",shannonFano(P1)," Huffman: ",huffman(P1))
cod1=codificarMensaje(S1,shannonFano(P1),deco1)
print("codificaciones",cod1)
print("deco:",decodificarMensaje(S1,shannonFano(P1),cod1))