# Universidade Estadual de Santa Cruz
# Discente: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

import numpy as np

def sistema_manual(y, t, a, b):
    j, k = y
    djdt = a * j - b * k
    dkdt = b * j - a * k
    return np.array([djdt, dkdt])

def metodo_euler(sistema, y0, t, a, b):
    sol = [y0]
    for i in range(1, len(t)):
        h = t[i] - t[i-1]
        y_atual = sol[-1]
        y_proximo = y_atual + h * sistema(y_atual, t[i], a, b)
        sol.append(y_proximo)
    return np.array(sol)

# Leitura dos parâmetros do arquivo
with open('EDOs/entrada.txt', 'r') as file:
    linhas = file.readlines()
    y0 = np.array([float(val) for val in linhas[0].split()])
    t_inicio, t_fim = [float(val) for val in linhas[1].split()]
    totalPontos = int(linhas[2])

# Geração dos pontos de tempo
t = np.linspace(t_inicio, t_fim, totalPontos)

# Parâmetros do sistema
a = 1.0
b = 0.5

# Resolução manual das EDOs usando o método de Euler
sol_manual = metodo_euler(sistema_manual, y0, t, a, b)

# Escrita dos resultados em um arquivo
with open('EDOs/resultado.txt', 'w') as f:
    for i in range(len(t)):
        f.write(f"t = {t[i]:.4f}, j = {sol_manual[i, 0]:.4f}, k = {sol_manual[i, 1]:.4f}\n")
