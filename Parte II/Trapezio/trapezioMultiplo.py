# Universidade Estadual de Santa Cruz
# Discente: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

# Implementação do método de Integração por Trapézio Múltiplo

from sympy import *
from math import *

x = symbols('x')

arquivoLer = open('Trapezio/entrada.txt', 'r')
arquivoResultado = open('Trapezio/resultado.txt', 'w')

def lerArquivo():
	
    global arquivoLer, funcao, a, b, subInter
	
    funcao = eval(arquivoLer.readline())

    a = float(arquivoLer.readline())
    b = float(arquivoLer.readline())

    subInter = int(arquivoLer.readline())

def intervalos(inicio, fim, h):
	xi = [inicio]

	aux = inicio + h
	while(aux < fim):
		aux = round(aux, 2)
		xi.append(aux)
		aux += h
	xi.append(aux)
	return xi

def metodoTrapezio(funcao, a, b, n):
	h = (b - a) / n
	xi = intervalos(a, b, h)
	tam = len(xi)
	I = funcao.subs(x, a) + funcao.subs(x, b)

	for i in range(1,tam-1):
		I += 2*(funcao.subs(x, xi[i]))
	I *= h/2
	return round(I, 3)

def main():
	global arquivoResultado, funcao, a, b, subInter

	lerArquivo()

	arquivoResultado.write("I(f(x)) ~= " + str(metodoTrapezio(funcao, a, b, subInter)))
 
	arquivoLer.close()	
	arquivoResultado.close()

main()
