import numpy as np

# Lendo os dados de entrada
with open('EliminacaoGauss/entrada.txt', 'r', encoding='utf-8') as arquivo:
    n = int(arquivo.readline().strip())  # Lê o tamanho da matriz
    A = []
    for i in range(n):
        linha = list(map(float, arquivo.readline().strip().split()))
        A.append(linha)
    b = list(map(float, arquivo.readline().strip().split()))
  
# Etapa de eliminação
for i in range(n):
    # Pivoteamento parcial: troca de linha se necessário
    max_row = i
    for k in range(i+1, n):
        if abs(A[k][i]) > abs(A[max_row][i]):
            max_row = k
    A[i], A[max_row] = A[max_row], A[i]
    b[i], b[max_row] = b[max_row], b[i]
        
    # Eliminação dos elementos abaixo do pivô
    for k in range(i+1, n):
        fator = A[k][i] / A[i][i]
        b[k] -= fator * b[i]
        for j in range(i, n):
            A[k][j] -= fator * A[i][j]

# Etapa de substituição
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = b[i] / A[i][i]
    for j in range(i + 1, n):
        x[i] -= A[i][j] * x[j] / A[i][i]

# Salvando o resultado no txt
with open('EliminacaoGauss/resultado.txt', 'w', encoding='utf-8') as arquivo:  
    for resultado in x:
        arquivo.write(f'x{i}: {resultado}\n')
        i+=1


