import sympy as sp

cont, resultado = 0, 0
# Lendo os dados do arquivo
with open('Secante/entrada.txt', 'r', encoding='utf-8') as arquivo:
    x0 = arquivo.readline().strip()  # Lê a primeira linha
    x1 = arquivo.readline().strip() # Lê a segunda linha
    erro = arquivo.readline().strip()  # Lê a terceira linha
    funcao = arquivo.readline().strip()  # Lê a quarta linha

# casting ...
x0 = float(x0)
x1 = float(x1)
erro = float(erro)

# salvando os intervalos...
inf = x0
sup = x1

# Transformando a string da função em uma expressão simbólica
x = sp.symbols('x')
f = sp.sympify(funcao)

fx0 = f.subs(x, x0)
fx1 = f.subs(x, x1)

# Calculando a raíz
while abs(fx1) > erro or abs(x2 - x1) < erro:

    if abs(fx1) < erro:
        cont+=1
        resultado = x1
        break
        
    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
    cont+=1
    if abs(x2 - x1) < erro:
        cont+=1
        resultado = x2
        break

    x0, x1 = x1, x2

fx = f.subs(x, resultado)

# Salvando o resultado no txt "resultado":
with open('Secante/resultado.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.8 ====================\n\n')
    arquivo.write(f'Intervalo: [{inf}, {sup}]\n')
    arquivo.write(f'A raiz encontrada é: {resultado}\n')
    arquivo.write(f'Valor da função aplicada à raíz é: {fx}\n')
    arquivo.write(f'Número de iterações necessário: {cont}\n')