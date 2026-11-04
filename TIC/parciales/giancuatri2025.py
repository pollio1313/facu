"""1. Para cada uno de los siguientes mensajes, emitidos por fuentes de información:
a. Determinar el alfabeto y las probabilidades de sus símbolos
b. Obtener la matriz de transición de la fuente 
c. Estimar si se trata de una fuente de memoria nula o no nula 
d. Calcular la entropía de la fuente 
e. Si es una fuente de memoria nula, generar la extensión de orden 2 y 
calcular su entropía a partir de sus probabilidades 
f. Si es una fuente con memoria, obtener el vector estacionario"""
import math

msj1=")[))[([()))()[[]](([[)))])))][))(][)[[[)()]))[)[])"
#a)
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

alf,prob=alfabeto(msj1)
print("a) ",alf,"   ",prob)

#b
def MatrizTransicion(alf,msj):                          
    """tener ne cuenta q muestra por columna 
    m= n1
       n2
       n3                            
       """
    Mat=[[0 for _ in range(len(alf))] for _ in range(len(alf))] #lleno la matriz de 0

    #acumula 
    for i in range(len(msj)-1):
        actual = alf.index(msj[i])
        siguiente= alf.index(msj[i+1])
        Mat[actual][siguiente]+=1 

    for i in range(len(alf)):
        total= sum(Mat[i])
        if total!=0:
            for j in range(len(alf)):
                Mat[i][j]=round(Mat[i][j]/total,2)
    return Mat

MatTrans=MatrizTransicion(alf,msj1)
print("b) Matriz",MatTrans)

#c
def tieneMem(M):
    igual=True
    for i in range(len(M)):
        for j in range(len(M)-1):
            if not M[j][i]==M[j+1][i]:
                igual=False
    
    return not igual

if tieneMem(MatTrans):
    print("c) TIENE MEMORIA")
else:
    print("c) NO TIENE MEMORIA")

#d
def entropia(l):                #espera una lista de probabilidades
    acum=0
    for i in l:
        entro = i * math.log2(1/i)
        acum= acum+entro
    return acum

print("d) ",round(entropia(prob),2))

#e
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
                NuevoP.append(round(Probant[x]*ListaP[y],4))
    return NuevoAlfabeto,NuevoP

alfExt,Pext=extenderNrecur(alf,prob,2)
print("e) ",alfExt," \n ",Pext)
print("entro:",round(entropia(Pext),3))

mensaje2="-+-+*//++///*/-////+---////-+/+--+-+/-/+-+/-+*++//"

#a
alf2,prob2=alfabeto(mensaje2)
print("a)",alfabeto(mensaje2))
#b
mat2=MatrizTransicion(alf2,mensaje2)
print("b)",mat2)
#c
if tieneMem(mat2):
    print("c) TIENE MEMORIA")
else:
    print("c) NO TIENE MEMORIA")
#d
print("d) ",round(entropia(prob2),2))
#e
def MultVectMat(V,Matriz):
    
    resultado=[]

    for j in range(len(Matriz)):
        suma=0

        for i in range(len(V)):
            suma+= V[i]* Matriz[i][j]
        resultado.append(suma)

    return resultado

def estacionario(Matriz):
    V=[1/len(Matriz)] * len(Matriz) #lleno el vector con equiprobable
    
    nuevo = MultVectMat(V,Matriz)
    iguales = False
    while not iguales:
        V=nuevo
        nuevo=MultVectMat(V,Matriz)
        iguales=True
        for i in range(len(V)):
            if abs(V[i]-nuevo[i])>=0.01:
                iguales=False
    return nuevo

print("e) ",estacionario(mat2))

def entropiaVe(Ve,Ma):
    suma=0
    for j in range(len(Ma)):
        sant=suma
        for i in range(len(Ve)):
            if Ma[j][i]!=0:
                suma+= Ve[j]*Ma[j][i]*math.log2(1/Ma[j][i])
    return suma

print("entropiav2: ",entropiaVe(estacionario(mat2),mat2))



#ejercicio 2

probCodigo1=[0.15,0.25,0.05,0.45,0.10]
Codigo1=[';.',',','.:',':',',;']
Codigo1conj={';.',',','.:',':',',;'}

print("\n--------------------EJE 2-----------------\n")
def entropiaR(l,r):             #espera la lista de probabilidades y a r que es la base
    acum=0
    
    for i in l:
        entro = i * math.log((1/i),r)
        acum= acum+entro
    return acum

print("a) Hr(cod1)=",entropiaR(probCodigo1,4))

def Longitud(Prob,cod):
    sum=0
    for i in range(len(Prob)):
        sum+=Prob[i]*len(cod[i])
    return sum


print("b) L=",Longitud(probCodigo1,Codigo1))

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

print("c) ",SumatoriaKraft(Codigo1))

#calcula si es UD, espera el codigo, no revisa lo anterior
#para saber si es UD, uso el algoritmo de sarinas patterson
def Univocamente(C):
    C=set(C)
    anteriores=[]
    S=set()
    for x in C:
        for y in C:
            if x.startswith(y):
                sufijo= x[len(y):]
            if y.startswith(x):
                sufijo=y[len(x):]
            if sufijo != '':
                S.add(sufijo)
    fin=False
    UD=True
    while (not fin) and S:
        #print("S=",S)
        
        #caso de S interseccion C
        if S & C:
            UD=False
            fin=True
        #caso que un sufijo este en otro S
        elif any(S & anterior for anterior in anteriores):
            UD=True
            fin=True
        else:
            anteriores.append(S)
            nuevo=set()
            for x in S:
                for y in C:
                    #print("x: ",x,"  y: ",y)
                    if x.startswith(y):
                        sufijo= x[len(y):]
                    if y.startswith(x):
                        sufijo=y[len(x):]
                        #print("sufijo:",sufijo)
                    if sufijo !='':
                        nuevo.add(sufijo)
            S=nuevo
    return UD

#revisa si es Insta, hay q verificar los otro por separado
#pasa saber si es instantaneo reviso q ninguna palabra sea prefijo de la otra
def instantaneo (C):
    insta=True
    for x in C:
        for y in C:
            if x.startswith(y) and x!=y:
                insta=False
    return insta
#mismo revisa si es no singular, lo hace viendo si el largo de la lista es igual al largo de la list con un set.
def NoSingular(C):
    if len(C)==len(set(C)):
        nosing=True
    else:
        nosing=False
    return nosing

print("NoSingular: ",NoSingular(Codigo1),"  UD: ",Univocamente(Codigo1conj),"    Instantaneo: ",instantaneo(Codigo1))

probCodigo2=[0.15,0.25,0.05,0.45,0.10]
Codigo2=['(]',']','[)',')','([']
Codigo2conj={'(]',']','[)',')','(['}

print("a) Hr(cod1)=",entropiaR(probCodigo2,4))

print("b) L=",Longitud(probCodigo2,Codigo2))

print("c) ",SumatoriaKraft(Codigo2))

print("NoSingular: ",NoSingular(Codigo2),"  UD: ",Univocamente(Codigo2conj),"    Instantaneo: ",instantaneo(Codigo2))

def compacto(C,prob):
    EsCompacto=True

    for i in range(len(prob)):
        if not(math.ceil(Informacion(prob[i]))>=len(C[i])):
            EsCompacto=False
    return EsCompacto

def Informacion(probabilidad):
    info = math.log2(1/probabilidad)
    return info

print("d) ",compacto(Codigo2,probCodigo2))

"""
Como 
"""