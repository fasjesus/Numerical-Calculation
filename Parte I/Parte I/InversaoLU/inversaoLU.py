import numpy as np

# Leitura dos dados de entrada
with open('InversaoLU/entrada.txt', 'r', encoding='utf-8') as arquivo:
    n = int(arquivo.readline().strip())
    A = []
    for i in range(n):
        linha = list(map(float, arquivo.readline().strip().split()))
        A.append(linha)

# Cálculo da fatoração LU
matriz = np.array(A)
n = len(matriz)
L = np.zeros((n, n))
U = np.zeros((n, n))

for i in range(n):
    L[i][i] = 1

    for j in range(i, n):
        U[i][j] = matriz[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        
    for j in range(i+1, n):
        L[j][i] = (matriz[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

# Calculando a matriz inversa
identidade = np.identity(n)
inversa = np.zeros((n, n))

for i in range(n):
    b = identidade[:, i]
    
    # Resolve o sistema linear LU
    n = len(b)
    y = np.zeros(n)
    x = np.zeros(n)

    # Resolva Ly = b
    for k in range(n):
        y[k] = b[k] - sum(L[k][p] * y[p] for p in range(k))

    # Resolva Ux = y
    for k in range(n - 1, -1, -1):
        x[k] = (y[k] - sum(U[k][p] * x[p] for p in range(k+1, n))) / U[k][k]

    inversa[:, i] = x

# Salvando a matriz inversa no arquivo "resultado.txt"
with open('inversaoLU/resultado.txt', 'w', encoding='utf-8') as arquivo:
    for linha in inversa:
        arquivo.write(' '.join([f'{valor:.3f}' for valor in linha]) + '\n')
