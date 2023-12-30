# Universidade Estadual de Santa Cruz
# Discente: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

from sympy import *
from math import *
import numpy as np

h = None
pontos = None
ultimo_x = None
a = None
b = None
Ta = None

arquivoLer = open('DiferencasFinitas/entrada.txt', 'r', encoding = 'utf8')
arquivoResultado = open('DiferencasFinitas/resultado.txt', 'w', encoding = 'utf8')


def lerArquivo():
    global arquivoLer, h, pontos, ultimo_x, a, b, Ta

    h = float(arquivoLer.readline())
    ultimo_x = float(arquivoLer.readline())
    pontos = int(arquivoLer.readline())
    a = float(arquivoLer.readline())
    b = float(arquivoLer.readline())
    Ta = float(arquivoLer.readline())

def eliminacao_gauss(A, b):
    n = len(A)
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
    return x



def diferencasFinitas(h, pontos, Dx, a, b, Ta):
    vetor_b = []
    matriz_linear = []
    aux = 0
    
    for i in range(pontos-1):
        vetor_aux = []
        for j in range(pontos-1):
            vetor_aux.append(0)
        
        if aux == 0:
            vetor_aux[aux] = (2 + h * Dx**2)
            vetor_aux[aux+1] = -1
        elif aux == pontos-2:
            vetor_aux[aux] = (2 + h * Dx**2)
            vetor_aux[aux-1] = -1
        else:
            vetor_aux[aux] = (2 + h * Dx**2)
            vetor_aux[aux+1] = -1
            vetor_aux[aux-1] = -1
        matriz_linear.append(vetor_aux)
        aux+=1
        
    vetor_b.append(h * (Dx**2) * Ta + a)

    for j in range(pontos-3):
        vetor_b.append(h * (Dx**2) * Ta)

    vetor_b.append(h * (Dx**2) * Ta + b)
            
    R = eliminacao_gauss(matriz_linear, vetor_b)

    count = 1
    
    if a%2 == 0:
        arquivoResultado.write("Iteração " + str(count) + ": ")
        arquivoResultado.write(str(int(a)) + "\n")
    else:
        arquivoResultado.write("Iteração " + str(count) + ": ")
        arquivoResultado.write(str(round(a, 5)) + "\n")

    for resultado in R:
        count += 1
        if resultado%2 == 0:
            arquivoResultado.write("Iteração " + str(count) + ": ")
            arquivoResultado.write(str(int(resultado)) + "\n")
        else:
            arquivoResultado.write("Iteração " + str(count) + ": ")
            arquivoResultado.write(str(round(resultado,5)) + "\n")

        
    if b%2 == 0:
        arquivoResultado.write("Iteração " + str(count+1) + ": ")
        arquivoResultado.write(str(int(b)) + "\n")
    else:
        arquivoResultado.write("Iteração " + str(count+1) + ": ")
        arquivoResultado.write(str(round(b,5)) + "\n")


def main():
    global h, pontos, ultimo_x, a, b, Ta

    lerArquivo()

    Dx = ultimo_x/pontos

    diferencasFinitas(h, pontos, Dx, a, b, Ta)


main()