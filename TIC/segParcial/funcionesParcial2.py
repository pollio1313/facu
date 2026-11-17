import math
import random


#extiende un alfabeo
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


#P(a)
#probabilidades y alfabeto del mensaje que salio de una fuente
#las probabilidades de los símbolos antes de que ingresen al canal
def prob_priori(entrada):
    alfabeto= sorted (set(entrada))
    total= len(entrada)
    probabilidades = []

    for simbolo in alfabeto:
        probabilidades.append(entrada.count(simbolo)/total)

    return alfabeto,probabilidades


#P(b)
#No sabemos qué se envió, solamente queremos saber qué probabilidades hay de recibir cada símbolo
def probabilidades_salida(P,M):
    salida=[]

    for j in range(len(M[0])):
        prob=0
        for i in range(len(P)):
            prob += P[i] *M[i][j]
        salida.append(prob)
    return salida

#P(a/b)
#Ahora estamos del lado del receptor: recibimos un símbolo y queremos averiguar qué se había enviado originalmente.
#Utilizamos el teorema de Baye
#Cada columna debe sumar 1, siempre que la probabilidad de esa salida sea mayor que cero
#devuevle la columna de 0 cuando P(B)=0, pero en realidad no se puede condicionar cuando un evento es imposible
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


#requiere el msj de entrada y el msj de salida del canal y te devuelve la amtriz
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

# La entropia a PRIORI
#nunca negativo, Si todos los simbolos son equiprobables, alcanza su maximo, si un simbolo tiene P()=1 entonces H da 0
def entropia(P):
    H=0
    for p in P:
        if p>0:
            H-=p*math.log2(p)
    return H


#espera un msj y el msj codificado
#me calcula la relacion de TamOriginal/tamComprimido, por 2.5 seria q se comprimio 2.5 veces
# TC > 1 hubo compresion, =1 no cambio elt amaño, <1 el tamaño se agrando, me da 0 cuando no hay codificacion
def tasaCompresion (mensaje,codificacion):
    tam_original = len(mensaje.encode("utf-8"))
    tam_comprimido = len(codificacion)

    if tam_comprimido ==0:
        return 0
    
    return tam_original/ tam_comprimido

#me devuelve el alafabeto codigo, hay q codificarlo despues, osea pasarlo por la otra funcion
#asigna simbolos cortos a los simbolos mas probables, y largos a los menos
#Garantiza una longitud media optima
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


#me devuelve el alafabeto codigo, hay q codificarlo despues, osea pasarlo por la otra funcion
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

#recibe el alfabeto, el alfabeto codigo, y el msj original q queres codificar, devuelve un bytearray
def codificarMensaje(alf,cod,mensaje):
    tabla = dict(zip(alf,cod))
    bits = "".join(tabla[c] for c in mensaje)
    bits += "0" * ((8- len(bits) % 8) % 8)

    resultado = bytearray()
    for i in range(0, len(bits), 8):
        resultado.append(int(bits[i:i+8],2))
    return resultado


#te devuelve la Longitud
def Longitud(Prob,cod):
    sum=0
    for i in range(len(Prob)):
        sum+=Prob[i]*len(cod[i])
    return sum

#devuelve rendimiento (n) y redundancia (R)
#rendimiento es la eficiencia de un codigo, es decirq ue proporcion de bits utilizados representa informacion de la fuente
#es la proporciond e bits adicionales q usa el codigo respecto del minimo necesario, mientras mas cercano a 0 menor reducnai y mayor eficiencia
def rendimientoRedundancia(C,P):
    n=entropia(P)/Longitud(P,C)
    r=1-n
    return n,r


#imprime el teorema de shannon
def shanonN(S,P,n):
    print(entropia(P)," < ",Longitud(P,S)," < ",entropia(P)+1)


#pide la amtriz y te analiza si es determinantes, tiene ruido, sin ruido, o ambas
#SIN RUIDO, solo un elemento distinto de 0 por columna. Cuando ves la salida sabes con certeza cual fue la entrada
#aunq una entrada puede producir varias salidas
#H(A/B)=0 <--equivocacion       I(A,B)=H(A)
#la cant info es igual a la incertidumbre total del alfabeto entrada

#DETERMINANTE, solo un elemento distinto de 0 por fila, sabiendo la entrada se con certeza la salida
#cada entrada produce una unica salida, pero una salida puede venir de varias entradas
#H(B/A)=0 <---ruido      I(A,B)=H(B)
#Toda la info se recoge a la salida

#si es ambas, significa q cada entrada produce una unica salida y cada salida se identifica con una unica entrada
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


# Mide cuanta incertidumbre me queda del mensaje original, despues de haber recibido al salida. Osea Recibi algo, y me dice cuanto sigo sin saber de lo q me habian enviado
#si me da 0 significa que puedo determinar la entrada original.
# mayor a 0 que tengo incertidumbre sobre la entrada
# igual H(A) la salida no me aporta informacion sobre la entrada
def equivocacion(M, P):
    conjunta = []

    for i in range(len(M)):
        fila = []

        for j in range(len(M[i])):
            fila.append(P[i] * M[i][j])

        conjunta.extend(fila)

    py = probabilidades_salida(P,M)

    return entropia(conjunta) - entropia(py)

#Mide cuánta información sobre el mensaje original obtenemos al recibir el mensaje de salida
# 0 la salida no me aporta ifno sobre la entrada
# mayor a 0 que conozco parcialmente al entrada
# =H(A) la salida me permite conocer perfectamente la entrada
def informacion_mutua(M, P):
    Hx = entropia(P)
    He = equivocacion(M, P)

    return Hx - He

def conjunta(P, M):
    J = []

    for i in range(len(P)):
        fila = []

        for j in range(len(M[0])):
            fila.append(P[i] * M[i][j])

        J.append(fila)

    return J

#Ruido: H(B|A) necesita la funcion llamda conjunta
def ruido(P, M):
    h = 0
    J = conjunta(P, M)

    for i in range(len(P)):
        for j in range(len(M[0])):
            if J[i][j] > 0:
                h -= J[i][j] * math.log2(M[i][j])

    return h



def columnasProporcionales(matriz, c1, c2):
    razon = None

    for fila in matriz:
        a = fila[c1]
        b = fila[c2]

        if abs(b) < 1e-9:
            if abs(a) > 1e-9:
                return False
        else:
            if razon is None:
                razon = a / b
            elif abs(a / b - razon) > 1e-9:
                return False

    return True

def matrizReduccion(matriz, c1, c2):
    columnas = len(matriz[0])

    if c1 > c2:
        c1, c2 = c2, c1
    R = []
    for i in range(columnas):
        fila = [0] * (columnas - 1)
        if i == c2:
            fila[c1] = 1
        elif i > c2:
            fila[i - 1] = 1
        else:
            fila[i] = 1
        R.append(fila)

    return R

def reducirCanal(matriz):
    reducida = [fila[:] for fila in matriz]

    while True:
        encontrada = False
        columnas = len(reducida[0])
        for c1 in range(columnas):    #recorre las columnas y busca proporcionales
            for c2 in range(c1 + 1, columnas):
                if columnasProporcionales(reducida, c1, c2):
                    R = matrizReduccion(reducida, c1, c2)  #genera matriz de reduccion
                    reducida = canalCompuesto(reducida, R)
                    encontrada = True
                    break
            if encontrada:
                break
        if not encontrada:
            break
    return reducida



def probabilidadError(apriori, matriz):
    error = 0

    for j in range(len(matriz[0])):
        probabilidades = []

        for i in range(len(matriz)):
            probabilidades.append(apriori[i] * matriz[i][j])

        error += sum(probabilidades) - max(probabilidades)

    return error


#en paso poner 0.001, esto devuelve la capacidad y tmb la probabilidad para cada simbolo
def capacidad_binaria(M, paso):
    capacidad = 0
    probabilidad_optima = None

    p = 0

    while p <= 1:
        P = [p, 1-p]

        # Probabilidades de salida
        PY = []

        for j in range(len(M[0])):
            prob = 0

            for i in range(2):
                prob += P[i] * M[i][j]

            PY.append(prob)

        # Entropía de salida
        HY = 0

        for prob in PY:
            if prob > 0:
                HY -= prob * math.log2(prob)

        # Entropía del ruido
        HYX = 0

        for i in range(2):
            H = 0

            for prob in M[i]:
                if prob > 0:
                    H -= prob * math.log2(prob)

            HYX += P[i] * H

        # Información mutua
        I = HY - HYX

        if I > capacidad:
            capacidad = I
            probabilidad_optima = P

        p += paso

    return capacidad, probabilidad_optima

def verificarMatriz(matriz):
    filasError = []
    columnasError = []

    for i in range(len(matriz)):  #  filas
        if matriz[i].count("1") % 2 != 0:
            filasError.append(i)

    for j in range(len(matriz[0])):  # columnas
        unos = 0

        for i in range(len(matriz)):
            if matriz[i][j] == "1":
                unos += 1

        if unos % 2 != 0:
            columnasError.append(j)

    return filasError, columnasError


#estas dos funciones de abajo corrigen el mensaje
def verificarMatriz(matriz):
    filasError = []
    columnasError = []

    for i in range(len(matriz)):  #  filas
        if matriz[i].count("1") % 2 != 0:
            filasError.append(i)

    for j in range(len(matriz[0])):  # columnas
        unos = 0

        for i in range(len(matriz)):
            if matriz[i][j] == "1":
                unos += 1

        if unos % 2 != 0:
            columnasError.append(j)

    return filasError, columnasError

def decodificarMensaje(matriz):
    filas, columnas = verificarMatriz(matriz)

    if len(filas) == 1 and len(columnas) == 1:
        i = filas[0]
        j = columnas[0]

        fila = list(matriz[i])

        if fila[j] == "0":
            fila[j] = "1"
        else:
            fila[j] = "0"

        matriz[i] = "".join(fila)

    elif len(filas) != 0 or len(columnas) != 0:
        return ""

    mensaje = ""

    for i in range(1, len(matriz)):
        binario = matriz[i][:7]
        mensaje += chr(int(binario, 2))


    return mensaje


#main q muestra donde esta el error
"""matrizBits = []

for i in range(0, len(entrada), 8):
    matrizBits.append(entrada[i:i+8])

filas, columnas = U2.verificarMatriz(matrizBits)

print("Filas con error:", filas)
print("Columnas con error:", columnas)

mensajeCorregido = U2.decodificarMensaje(matrizBits)

print("Mensaje corregido:", mensajeCorregido)"""



#funcion q con un codg y un mensaje codificado, te crea un alfabeto y p
def decodificar(codigo, mensaje):
    alfabeto = []

    for i in range(len(codigo)):
        alfabeto.append(chr(ord('A') + i))

    tabla = {}

    for i in range(len(codigo)):
        tabla[codigo[i]] = alfabeto[i]

    resultado = ""
    actual = ""

    for bit in mensaje:
        actual += bit

        if actual in tabla:
            resultado += tabla[actual]
            actual = ""

    if actual != "":
        print("Error: código incompleto")
        return None

    print("Mensaje decodificado:", resultado)
    print("\nProbabilidades:")

    probabilidades = []

    for simbolo in alfabeto:
        cantidad = resultado.count(simbolo)
        probabilidad = cantidad / len(resultado)
        probabilidades.append(probabilidad)

        print(simbolo, ":", probabilidad)

    return resultado, probabilidades


