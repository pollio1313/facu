import math
def matriz_determinante(M, j, k):
    n = len(M[0])
    D = []

    nueva_columna = 0

    for i in range(n):
        fila = [0] * (n - 1)

        if i == j or i == k:
            fila[nueva_columna] = 1
        else:
            fila[nueva_columna] = 1
            nueva_columna += 1

        D.append(fila)

    return D

def combinacion_suficiente(M, j, k):
    for i in range(len(M)):
        for h in range(len(M)):
            if M[i][j] * M[h][k] != M[i][k] * M[h][j]:
                return False

    return True

def reducir_canal(M):
    while len(M[0]) > 1:
        reduccion = False

        for j in range(len(M[0])):
            for k in range(j + 1, len(M[0])):
                if combinacion_suficiente(M, j, k):
                    D = matriz_determinante(M, j, k)

                    print("Columnas combinadas:", j, k)
                    print("Matriz determinante:")
                    for fila in D:
                        print(fila)

                    nueva = []
                    for fila in M:
                        nueva.append([
                            sum(fila[i] * D[i][c] for i in range(len(fila)))
                            for c in range(len(D[0]))
                        ])

                    M = nueva
                    reduccion = True
                    break

            if reduccion:
                break

        if not reduccion:
            break

    print("Matriz final:")
    for fila in M:
        print(fila)

    return M

M4 = [
    [0.0, 0.5, 0.0, 0.5],
    [0.8, 0.0, 0.2, 0.0],
    [0.0, 0.5, 0.0, 0.5],
    [0.8, 0.0, 0.2, 0.0]
]

reducir_canal(M4)