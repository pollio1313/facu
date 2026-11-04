import math
import random

#calcular un alfabeto a partir de una mensaje
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

#calcular probabilidad simple, espera la probabilidad sola, no una lista

def Informacion(probabilidad):
    info = math.log2(1/probabilidad)
    return info

#entropia simple de un caso sin memoria, espera una Lista[]
#entropia de fuentes sin memoria
def entropia(l):
    acum=0
    for i in l:
        entro = i * math.log2(1/i)
        acum= acum+entro
    return acum

#simula un mensaje espera el largo del mensaje,n y la lista alfabeto y la probabilidad
def simulacion(n,listaA,listaP):
    mensaje = random.choices(listaA,weights=listaP,k=n)
    mensaje = ''.join(mensaje)
    return mensaje

#espera una lista[] de probabilidades y devuelve una lista
def InformacionAlfabeto(prob):    #espera una lista de probabilidades
    info=[]
    for i in prob:
        info.append(math.log2(1/i))
    return info


#espera una lista de caracteres, otra de probabilidades, y n de cuanto extiendo
#devuelve una lista con alfabeto nuevo y sus probabilidades. Si no calculara las neuvas p, podria ahcer la entropia anterior y multiplicarla por n
#tener en cuenta q si calculo la entropia de la extension, esta va a ser n*H de la fuente original es decir,si antes de la extension tenia H=1,5 y la extiendo en n=2 la entropia nueva seria 3
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

#funcion q utiliza el estacionario, deberia usarla yo
def MultVectMat(V,Matriz):
    
    resultado=[]

    for j in range(len(Matriz)):
        suma=0

        for i in range(len(V)):
            suma+= V[i]* Matriz[i][j]
        resultado.append(suma)

    return resultado

#est funcion espera la matriz de prob, y te devuelve el vectorEstacionario
# primero asigna que todo es equiprobable, despues M*Ve=Ve, empiezo a hacer M*ve y me fijo si el ve es igual al nuevo, repito esa ceunta hasta q la diferencia me de practicamente igual

def estacionario(Matriz):
    V=[1/len(Matriz)] * len(Matriz) #lleno el vector con equiprobable
    
    nuevo = MultVectMat(V,Matriz)
    iguales = False
    while not iguales:
        V=nuevo
        nuevo=MultVectMat(V,Matriz)
        iguales=True
        for i in range(len(V)):
            if abs(V[i]-nuevo[i])>=0.001:
                iguales=False
        print("   V:",nuevo,"\n")
    return nuevo

#calcula la entropia del Ve, espera el Vector y la Mat de probabilidades
#Entropia fuentes de memoria no nula, Markov

def entropiaVe(Ve,Ma):
    suma=0
    for j in range(len(Ma)):
        sant=suma
        for i in range(len(Ve)):
            suma+= Ve[j]*Ma[j][i]*math.log2(1/Ma[j][i])
        print("   ",suma-sant)
    return suma

#Calcular la amtriz de transicion, es decir la probabilidad de un signo dependiendo del anterior, espera el alfabeto y los mensajes
"""tener ne cuenta q muestra por columna 
    m= n1
       n2
       n3                            
       """
def MatrizTransicion(alf,msj):
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
                Mat[i][j]/=total
    return Mat

#genera un mensaje, espera el largo del mensaje, el alfabeto y la mtriz de transicion o de probabilidaes
def generarMsj(N,alf,M):
    mensaje=""

    #simbolo inicial
    estado=random.randint(0,len(alf)-1)
    mensaje+=alf[estado]

    for i in range(N-1):
        r= random.random()
        acumulada=0
        nuevo_estado=0
        for j in range(len(alf)):
            acumulada+=M[estado][j]
            if r>=acumulada:
                nuevo_estado+=1
        estado=nuevo_estado
        mensaje+=alf[estado]
    return mensaje

#devuelve si tiene memoria o no, para esto se fija si en las filas son iguales, osea la probabilidad del simbolo no depende del simbolo anterior
"""
if tieneMem(Matriz):
    print("TIENE MEMORIA")
else:
    print("NO")
"""

def tieneMem(M):
    igual=True
    for i in range(len(M)):
        for j in range(len(M)-1):
            if not M[j][i]==M[j+1][i]:
                igual=False
            print(M[j][i],"==",M[j+1][i])
    
    return not igual

# espera un conjunto {}
#usa el algoritmo de sardinas patterson se obtienen sucesivamente los conjuntos de subfijos, revisando si alguno de ellos pertenece al conjunto C (conjunto de palabras codigo)(este caso seria NO UD) o algun otro conjunto de subfijos anterior(en escaso SI UD)
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

#calcula el alfabeto del codigo, espera el mensaje hecho a aprtir del codigo
def alfabetocod(cad):
    listaA=[]
    for i in cad:
        if not (i in listaA):
            listaA.append(i)
    return listaA

#calcula la Longitud media L, espera la probabilidad y el alfabeto codigo
#esta funcion hace la sumaoria de la probabilidad de la palabra * su longitud
def Longitud(Prob,cod):
    sum=0
    for i in range(len(Prob)):
        sum+=Prob[i]*len(cod[i])
    return sum

#calcula la longitud l
def LongitudesChicas(cod):
    listaLi=[]
    for i in cod:
        listaLi.append(len(i))
    return listaLi

#la sumatoria de craft se calcula con la sumatoria de r^(-l), para cumplirse tiene q ser menos o igual q uno, tambien puede obsevarse
#que mientras mas larga sea la palabra mas chiquita te va a dar la sumatoria, entonces siendo que kraft te dice si puede ser instantaneo. Esto tiene sentido ya que mientras mas larga la palabra menos chances hay de q sea prefijo de la otra.

def SumatoriaKraft(cod):
    r=len(alfabetocod(cod))
    l=LongitudesChicas(cod)
    sum=0
    for i in l:
        sum+= r**(-i)
    return sum
#r seria la cantidad de simbolos que tiene el alfabeto codigo
#para calcularla uso la formula de Sumatoria de p*logr(1/p)
def entropiaR(l,r):             #espera la lista de probabilidades y a r que es la base 
    acum=0
    
    for i in l:
        entro = i * math.log((1/i),r)
        acum= acum+entro
    return acum

#espera el el codigo, y sus probabilidades
#revisa que el largo de la palabra codigo, sea menor o igual que la informacion redondeada hacia arriba del simbolo que representa.Si cumple para todos el alfabeto devuelve true
#si resulta que la Hr(s)=L(C) es un compacto perfecto, sino deberia ser h<L, y si da al revez algo esta mal
def compacto(C,prob):
    EsCompacto=True

    for i in range(len(prob)):
        if not(round(Informacion(prob[i]))>=len(C[i])):
            EsCompacto=False
    return EsCompacto
