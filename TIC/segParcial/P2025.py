"""
a PROB SIMBOLOS, ENTROPIA FUENTE
b generar codigo binario optimo para la fuente
c determinar tasa de compresion que se obtiene codificando el mensaje
d generar codigo binario optimo de extension de orden 3
e calcular la longitud media, el rendimiento y la redundancia de cada codigo
f verificar si ambos codigos cumplen con el primer teorema de shannon

"""


import math
import random

msj="LJMMJLMJLJJMLMMLLKJL"

def prob_priori(entrada):
    alfabeto= sorted (set(entrada))
    total= len(entrada)
    probabilidades = []

    for simbolo in alfabeto:
        probabilidades.append(entrada.count(simbolo)/total)

    return alfabeto,probabilidades

def H_priori(P):
    H=0
    for p in P:
        if p>0:
            H-=p*math.log2(p)
    return H

def entropia(P):
    H=0
    for p in P:
        if p>0:
            H-=p*math.log2(p)
    return H

def tasaCompresion (mensaje,codificacion):
    tam_original = len(mensaje.encode("utf-8"))
    tam_comprimido = len(codificacion)

    if tam_comprimido ==0:
        return 0
    
    return tam_original/ tam_comprimido


#me devuelve el alafabeto codigo, hay q codificarlo despues, osea pasarlo por la otra funcion
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

def codificarMensaje(alf,cod,mensaje):
    tabla = dict(zip(alf,cod))
    bits = "".join(tabla[c] for c in mensaje)
    bits += "0" * ((8- len(bits) % 8) % 8)

    resultado = bytearray()
    for i in range(0, len(bits), 8):
        resultado.append(int(bits[i:i+8],2))
    return resultado

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

def Longitud(Prob,cod):
    sum=0
    for i in range(len(Prob)):
        sum+=Prob[i]*len(cod[i])
    return sum

def rendimientoRedundancia(C,P):
    n=H_priori(P)/Longitud(P,C)
    r=1-n
    return n,r

def shanonN(S,P,n):
    print(H_priori(P)," < ",Longitud(P,S)," < ",H_priori(P)+1)


alfabetoFuente,ProbabiliadesPriori=prob_priori(msj)
alfExt3,probExt3=extenderNrecur(alfabetoFuente,ProbabiliadesPriori,3)
codHuffmanExt3=huffman(probExt3)

codificacionHuffman=huffman(ProbabiliadesPriori)
codificacionShannon=shannonFano(ProbabiliadesPriori)
print(prob_priori(msj),"    H:",H_priori(ProbabiliadesPriori))
print("     TazaCompreison:",tasaCompresion(msj,codificarMensaje(alfabetoFuente,codificacionHuffman,msj)))
print("     TazaCompreison:",tasaCompresion(msj,codificarMensaje(alfabetoFuente,codificacionShannon,msj)))

print("     TazaCompreison:",tasaCompresion(msj,codificarMensaje(alfabetoFuente,codHuffmanExt3,msj)))


L=Longitud(ProbabiliadesPriori,codificacionHuffman)
rendimiento,redundancia=rendimientoRedundancia(codificacionHuffman,ProbabiliadesPriori)
print("L:",L,"Rendi:",rendimiento,"redund:",redundancia)

L=Longitud(probExt3,codHuffmanExt3)
rendimiento,redundancia=rendimientoRedundancia(codHuffmanExt3,probExt3)
print("L:",L,"Rendi:",rendimiento,"redund:",redundancia)

shanonN(codificacionHuffman,ProbabiliadesPriori,2)
shanonN(codHuffmanExt3,probExt3,3)




"""
obetener las probabilidades a priori y la matriz del canal

"""



entrada="10000111100110111010101010110100"
salida="CBBBBBBCDBBDCABDBBAADBBACAAABBBA"

def probabilidades_salida(P,M):
    salida=[]

    for j in range(len(M[0])):
        prob=0
        for i in range(len(P)):
            prob += P[i] *M[i][j]
        salida.append(prob)
    return salida

def probabilidades_posteriori(P,M):
    salida=probabilidades_salida(P,M)
    posteriori = []

    for i in range(len(P)):
        fila =[]
        for j in range(len(salida)):
            if salida[j] != 0:
                fila.append(P[i]*M[i][j]/ salida[j])
            else:
                fila.append(0)
        posteriori.append(fila)
    return posteriori

def matriz_canal (entrada,salida):      #me devuelve de a filas
    simbolos_entrada= sorted(set(entrada))
    simbolos_salida=sorted(set(salida))
    matriz=[]

    for x in simbolos_entrada:
        fila=[]

        for y in simbolos_salida:
            cantidad=0
            total=0
            for i in range(len(entrada)):
                if entrada[i]==x:
                    total+=1
                    if salida[i]==y:
                        cantidad +=1
            if total >0:
                fila.append(cantidad/total)
            else:
                fila.append(0)
        
        matriz.append(fila)
    
    return matriz

AlfFuente,Ppriori=prob_priori(entrada)
mat1=matriz_canal(entrada,salida)
Pposteriori=probabilidades_posteriori(Ppriori,mat1)
print("\n---------------------------------------------------------------------------------------------\n Ppriori:",Ppriori,"   MatrizCanal:",mat1)



def analizar_canal(M):
    determinante = True
    sin_ruido = True

    # Verificar si es determinante (filas)
    for fila in M:
        salidas = 0

        for p in fila:
            if p > 0:
                salidas += 1

        if salidas > 1:
            determinante = False

    # Verificar si no tiene ruido (columnas)
    for j in range(len(M[0])):
        entradas = 0

        for i in range(len(M)):
            if M[i][j] > 0:
                entradas += 1

        if entradas > 1:
            sin_ruido = False

    if determinante and sin_ruido:
        print("Ambos")
    elif determinante:
        print("Determinante")
    elif sin_ruido:
        print("Sin ruido")
    else:
        print("Ninguno")






analizar_canal(mat1)

def equivocacion(M, P):
    conjunta = []

    for i in range(len(M)):
        fila = []

        for j in range(len(M[i])):
            fila.append(P[i] * M[i][j])

        conjunta.extend(fila)

    py = probabilidades_salida(M, P)

    return entropia(conjunta) - entropia(py)


def informacion_mutua(M, P):
    Hx = entropia(P)
    He = equivocacion(M, P)

    return Hx - He

print(equivocacion(mat1,Ppriori),"  ",informacion_mutua(mat1,Ppriori))
