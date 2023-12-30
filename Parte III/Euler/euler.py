# Universidade Estadual de Santa Cruz
# Discente: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio 

import math

def euler(f, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]
    
    for _ in range(n):
        x = x_values[-1]
        y = y_values[-1]
        
        y_new = y + h * f(x, y)
        x_new = x + h
        
        x_values.append(x_new)
        y_values.append(y_new)
    
    return x_values, y_values

def main():
    # Lê a entrada do arquivo
    with open('Euler/entrada.txt', 'r', encoding="utf-8") as file:
        equation = file.readline().strip()
        n = int(file.readline())
        x0 = float(file.readline())
        y0 = float(file.readline())
        h = float(file.readline())
        

    # Define a função a partir da string lida do arquivo
    f = lambda x, y: eval(equation)

    n = int(n)

    # Chamada da função do método de Euler
    x_values, y_values = euler(f, x0, y0, h, n)

    # Abrir o arquivo de saída
    with open('Euler/resultado.txt', 'w', encoding="utf-8") as f:
        # Imprime os resultados
        i = 0
        for x, y in zip(x_values, y_values):
            f.write(f"x[{i}] = {x:.1f},  y = {y:.6f}\n")
            i = i + 1
            #
        
main()

#x[{i}] = {x:.1f},  y = {y:.6f}