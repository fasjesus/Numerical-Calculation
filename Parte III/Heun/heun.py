# Universidade Estadual de Santa Cruz
# Discente: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

import math

def heun(f, x0, y0, h, interacao):
   
    x = x0
    y = y0
    solucao = [(x, y)]

    for _ in range(interacao):
        y_euler = y + h * f(x, y)
        y = y + (h / 2) * (f(x, y) + f(x + h, y_euler))
        x += h
        solucao.append((x, y))

    return solucao


with open('Heun/entrada.txt', 'r') as file:
    funcao = file.readline().strip()
    n = int(file.readline())
    x0 = float(file.readline())
    y0 = float(file.readline())
    h = float(file.readline())
    

f = lambda x, y: eval(funcao)

solucao = heun(f, x0, y0, h, n)


with open('Heun/resultado.txt', 'w') as f:
    i = 0
    for x, y in solucao:
        f.write(f"x[{i}] = {x:.2f},  y[{i}] = {y:.6f}\n")
        i = i+1
#x[{i}] = {x:.2f},  y[{i}] = {y:.4f}