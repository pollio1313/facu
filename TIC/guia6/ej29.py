import math

def probabilidad_error(M, P):   #el B me dio mal
    aciertos = 0

    for j in range(len(M[0])):
        mayor = 0

        for i in range(len(M)):
            prob = P[i] * M[i][j]

            if prob > mayor:
                mayor = prob

        aciertos += mayor

    return 1 - aciertos


M = [
    [0.6, 0.3, 0.1],
    [0.1, 0.8, 0.1],
    [0.3, 0.3, 0.4]
]

P1 = [1/3, 1/3, 1/3]
P2 = [1/8, 3/8, 4/8]
P3 = [4/15, 3/15, 8/15]

print("a)", probabilidad_error(M, P1))
print("b)", probabilidad_error(M, P2))
print("c)", probabilidad_error(M, P3))