# Universidade Estadual de Santa Cruz
# Discente: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

# Implementação do método de Simpson 1/3

from sympy import *
from math import *

x = symbols('x')

arquivoLer = open('Simpson/entrada.txt', 'r')
arquivoResultado = open('Simpson/resultado.txt', 'w')

def lerArquivo():
	
	global arquivoLer, funcao, a, b, subInter

	funcao = eval(arquivoLer.readline())

	a = float(arquivoLer.readline())
	b = float(arquivoLer.readline())

	subInter = int(arquivoLer.readline())

def intervalos(inicio, fim, h):
	
	xi = [inicio]
	aux = inicio + h
 
	while(True):
		if aux >= fim:
			break
		aux = round(aux, 2)
		xi.append(aux)
		aux += h
	xi.append(aux)
	
	return xi

def Simpson1_3(funcao, a, b, n):
	
	h = (b - a) / (2*n)
	xi = intervalos(a, b, h)
	I = funcao.subs(x, a) + funcao.subs(x, b)

	for i in range(1,len(xi)-1):
		aux = funcao.subs(x, xi[i])
		if(i % 2 == 0):
			I += 2*aux
		elif i % 2 != 0:
			I += 4*aux
	I *= h/3
	
	return round(I, 4)

def main():
	
	global arquivoResultado, funcao, a, b, subInter

	lerArquivo()

	arquivoResultado.write("I(f(x)) ~= " + str(Simpson1_3(funcao, a, b, subInter)))
	arquivoLer.close()	
	arquivoResultado.close()

main()
