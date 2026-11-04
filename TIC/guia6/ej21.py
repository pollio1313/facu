import math

def H(P):
    return -sum(p * math.log2(p) for p in P if p > 0)


def I(M, P):
    py = [sum(P[i] * M[i][j] for i in range(len(M)))
          for j in range(len(M[0]))]

    conjunta = [P[i] * M[i][j]
                for i in range(len(M))
                for j in range(len(M[0]))]

    return H(P) + H(py) - H(conjunta)


def reducir(M, P):
    while len(M[0]) > 1:
        original = I(M, P)
        mejor = None

        for j in range(len(M[0])):
            for k in range(j + 1, len(M[0])):
                nueva = []

                for fila in M:
                    nueva.append([
                        fila[j] + fila[k]
                    ] + [fila[x] for x in range(len(fila))
                         if x != j and x != k])

                if abs(I(nueva, P) - original) < 1e-9:
                    mejor = nueva
                    break

            if mejor is not None:
                break

        if mejor is None:
            break

        M = mejor

    for fila in M:
        print(fila)
    print("\n")
    return M



M1=[[0.4,0.6,0.0,0.0],[0.0,0.0,0.5,0.5],[0.0,0.0,0.7,0.3]]
P1=[1/3,1/3,1/3]
M2=[[0.2,0.3,0.5],[0.0,0.0,1.0],[0.0,0.0,1.0]]
P4=[1/4,1/4,1/4,1/4]
M3=[[0.4,0.0,0.2,0.4],[0.4,0.3,0.2,0.1],[0.0,0.3,0.0,0.7]]
M4=[[0.0,0.5,0.0,0.5],[0.8,0.0,0.2,0.0],[0.0,0.5,0.0,0.5],[0.8,0.0,0.2,0.0]]
reducir(M1,P1)
reducir(M2,P1)
reducir(M3,P1)
reducir(M4,P4)