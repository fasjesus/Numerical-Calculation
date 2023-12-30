import sympy as sp

# Lendo os dados do arquivo
with open('Bisseccao/entrada.txt', 'r', encoding='utf-8') as arquivo:
    a = arquivo.readline().strip() # primeira linha 
    b = arquivo.readline().strip() # segunda linha
    erro = arquivo.readline().strip() # terceira linha
    funcao = arquivo.readline().strip() # quarta linha

# salvando os intervalos...
inf = a
sup = b

# casting ...
a = float(a)
b = float(b)
erro = float(erro)

#cria variavel para a equacao
x = sp.symbols('x')

#transformar f em funcao algebrica
f = sp.sympify(funcao)

# contador para monitorar as iteracoes
cont = 0

if f.subs(x, a) * f.subs(x, b) >= 0:
    print("A função deve ter sinais opostos em (a) e (b).")
    SystemExit()

while (b - a) / 2.0 > erro:
    c = (a + b) / 2.0
    cont+=1
    if f.subs(x, c) <= erro:
        break
    elif f.subs(x, c) * f.subs(x, a) < 0:
        b = c
    else:
        a = c
    
resultado = (a + b) / 2.0
fx = f.subs(x, resultado)

# Salvando o resultado no txt "resultado":
with open('Bisseccao/resultado.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.6 ====================\n\n')
    arquivo.write(f'Intervalo: [{inf}, {sup}]\n')
    arquivo.write(f'A raiz encontrada é: {resultado}\n')
    arquivo.write(f'Valor da função aplicada à raíz é: {fx}\n')
    arquivo.write(f'Número de iterações necessário: {cont}\n')