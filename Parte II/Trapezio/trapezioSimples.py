# Universidade Estadual de Santa Cruz
# Discente: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

# Implementação do método de Integração por Trapézio Simples

from sympy import *

x = symbols('x')

arquivoLer = open('Trapezio/entrada.txt', 'r')
arquivoResultado = open('Trapezio/resultado.txt', 'w')

def lerArquivo():
	
    global arquivoLer, funcao, a, b
	
    funcao = eval(arquivoLer.readline())

    a = float(arquivoLer.readline())
    b = float(arquivoLer.readline())

def trapezio_simples(a, b, funcao):
    
    I = (b - a)*((funcao.subs(x, a) + funcao.subs(x, b))/2)
    return I

def main():
	global arquivoResultado, funcao, a, b

	lerArquivo()

	arquivoResultado.write("I(f(x)) ~= " + str(trapezio_simples(a, b, funcao)))
 
	arquivoLer.close()	
	arquivoResultado.close()

main()