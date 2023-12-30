# Universidade Estadual de Santa Cruz
# Discente: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

import sympy as sp

def read_file(path):
    """
    Lê um arquivo e retorna uma lista com as linhas do arquivo.
    """
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]

def write_file(res):
    # Abrir o arquivo de saída
    with open('Ralston/resultado.txt', 'w', encoding="utf-8") as f:
        # Imprime os resultados	
        i = 0
        for x, y in res.items():
            f.write(f"x[{i}] = {x:.1f},  y = {y:.6f}\n")
            i = i + 1
            #

def f(x, y):
    
    return eval(func)

def ralston_method(x0, y0, h, n):
    """
    Resolve uma EDO de primeira ordem pelo método de Ralston.
    Retorna um dicionário com os valores de x e y.
    """

    dots = {x0: round(y0, 6)}

    for _ in range(n):
        k1 = f(x0, y0)
        k2 = f(x0 + (3/4)*h, y0 + (3/4)*h*k1)

        y0 += h * ((1/3)*k1 + (2/3)*k2)
        x0 += h
        dots[x0] = round(y0, 6)

    return dots

def main():
    global func

    # Lê a entrada do arquivo
    lines = read_file('Ralston/entrada.txt')
    func = lines[0]
    n = int(lines[1])
    x0 = float(lines[2])
    y0 = float(lines[3])
    h = float(lines[4])

    # Chamada da função do método de Ralston
    res = ralston_method(x0, y0, h, n)

    # Escrever os resultados no arquivo de saída
    write_file(res)

main()
