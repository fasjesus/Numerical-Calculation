# Universidade Estadual de Santa Cruz
# Discente: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

import math

def runge_kutta4(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]

    for _ in range(n):
        x = x_values[-1]
        y = y_values[-1]

        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x_next = x + h

        x_values.append(x_next)
        y_values.append(y_next)

    return x_values, y_values

def main():
    # Lê a entrada do arquivo
    with open('RungeKutta/entrada.txt', 'r') as file:
        equation = file.readline().strip()
        n = int(file.readline())
        x0 = float(file.readline())
        y0 = float(file.readline())
        h = float(file.readline())

    # Define a função a partir da string lida do arquivo
    f = lambda x, y: eval(equation)

    n = int(n)

    # Chamada da função do método de Euler
    x_values, y_values = runge_kutta4(f, x0, y0, h, n)

    # Abrir o arquivo de saída
    with open('RungeKutta/resultado.txt', 'w') as f:
        # Imprime os resultados
        i = 0
        for x, y in zip(x_values, y_values):
            f.write(f"x[{i}] = {x:.2f},  y =  {y:.6f}\n")
            # x[{i}] = {x:.2f},  y = 
            i = i + 1
        
main()

