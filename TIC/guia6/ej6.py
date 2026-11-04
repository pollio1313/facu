"""5. Volver a realizar los cálculos del ejercicio anterior, 
pero considerando las probabilidades a priori P(0) = 0.2 y P(1) = 0.8. 
Comparar los resultados obtenidos."""


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

def probabilidades_conjuntas(P,M):
    conjunta=[]
    for i in range(len(P)):
        fila = []
        for j in range(len(M[i])):
            fila.append(P[i]*M[i][j])
        conjunta.append(fila)
    return conjunta


matrizCanal=[[0.4,0.4,0.2],[0.3,0.2,0.5],[0.3,0.4,0.3]]
prob=[0.3,0.3,0.4]


print(probabilidades_salida(prob,matrizCanal),"\n",probabilidades_posteriori(prob,matrizCanal),"\n",probabilidades_conjuntas(prob,matrizCanal))