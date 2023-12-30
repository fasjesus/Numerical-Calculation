import sympy as sp

# Lendo os dados do arquivo
with open('PosicaoFalsa/entrada.txt', 'r', encoding='utf-8') as arquivo:
    a = arquivo.readline().strip()  # Lê a primeira linha
    b = arquivo.readline().strip()  # Lê a segunda linha
    erro = arquivo.readline().strip()  # Lê a terceira linha
    funcao = arquivo.readline().strip()  # Lê a quarta linha

# salvando os intervalos...
inf = a
sup = b

# casting ...
a = float(a)
b = float(b)
erro = float(erro)

# Transformando a string da função em uma expressão simbólica
x = sp.symbols('x')
f = sp.sympify(funcao)

cont = 0
resultado = 0

fa = f.subs(x, a)
fb = f.subs(x, b)
  
while fa > erro or fb > erro:   
    if abs(fa) < erro:
        cont+=1
        resultado = a
        break  
    if abs(fb) < erro:
        cont+=1
        resultado = a
        break        
    c = (((a * fb) - (b * fa)) / (fb - fa))
    fc = f.subs(x, c)
        
    if abs(fc) < erro:
        fa = fc # condicao de parada
        cont+=1
        resultado = a
        break
    if fa * fc < 0:
        b = c
        cont+=1
    else:
        a = c
        cont+=1

fx = f.subs(x, resultado)

# Salvando o resultado no txt "resultado":
with open('PosicaoFalsa/resultado.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(f'================ PROBLEMA 3.6 ====================\n\n')
    arquivo.write(f'Intervalo: [{inf}, {sup}]\n')
    arquivo.write(f'A raiz encontrada é: {resultado}\n')
    arquivo.write(f'Valor da função aplicada à raíz é: {fx}\n')
    arquivo.write(f'Número de iterações necessário: {cont}\n')

