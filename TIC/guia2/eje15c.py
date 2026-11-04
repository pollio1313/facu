import math
import random

def tieneMem(M):
    igual=True
    for i in range(len(M)):
        for j in range(len(M)-1):
            if not M[j][i]==M[j+1][i]:
                igual=False
            print(M[j][i],"==",M[j+1][i])
    
    return not igual


Matriz=[[0.3,0.2,0.5],[0.2,0.3,0.5],[0.2,0.3,0.5]]

if tieneMem(Matriz):
    print("TIENE MEMORIA")
else:
    print("NO")
            