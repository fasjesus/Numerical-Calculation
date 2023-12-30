# Universidade Estadual de Santa Cruz
# Discnte: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

# Implementação do método da Quadratura de Gauss

from sympy import *

x = symbols('x')

arquivoLer = open('QuadraturaDeGauss/entrada.txt', 'r')
arquivoResultado = open('QuadraturaDeGauss/resultado.txt', 'w')

def lerArquivo():
	
    global arquivoLer, funcao, a, b
	
    funcao = eval(arquivoLer.readline())

    a = float(arquivoLer.readline())
    b = float(arquivoLer.readline())

def quadratura_gauss(a, b, funcao):
    
    I = ((b - a)/2)*funcao.subs(x, a) + ((b - a)/2)*funcao.subs(x, b)
    return I

def main():
	global arquivoResultado, funcao, a, b, subInter

	lerArquivo()

	arquivoResultado.write("I(f(x)) ~= " + str(quadratura_gauss(a, b, funcao)))
 
	arquivoLer.close()	
	arquivoResultado.close()

main()