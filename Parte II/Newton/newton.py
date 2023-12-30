# Universidade Estadual de Santa Cruz
# Discente: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

# Implementação do método das Diferenças Divididas de Newton

from sympy import *
from math import *

fx = {}
pontos = []
x = symbols('x')

arquivoLer = open('Newton/entrada.txt', "r")
arquivoResultado = open("Newton/resultado.txt", "w")

def lerArquivo():
	global arquivoLer, fx, pontos

	aux = arquivoLer.readline()
	while(aux != '\n'):
		aux = float(aux)
		pontos.append(aux)
		aux = arquivoLer.readline()
  
	aux = arquivoLer.readline()
 
	i = 0
 
	while(aux != '' and aux != '\n'):		
		aux = float(aux)
		fx[pontos[i]] = aux		
		aux = arquivoLer.readline()
		i += 1
	
def calculaFdosPontos(fx, pontos):
	n = len(pontos)
	if(n == 1):
		return fx[pontos[0]]
	elif(n == 2):
		return(fx[pontos[0]] - fx[pontos[1]]) / (pontos[0] - pontos[1])
	else:		
		return(calculaFdosPontos(fx, pontos[0 : n-1]) - calculaFdosPontos(fx, pontos[1 : n])) / (pontos[0] - pontos[n-1])

def newton(fx, pontos):
	termos = 1
	n = len(pontos)
	P = 0
	aux = []

	for i in range(n):
		aux.append(pontos[i])
		P += termos * round(calculaFdosPontos(fx, aux), 2)
		termos = termos * Poly(x - pontos[i])

	return str(P.args[0])


def main():
	global arquivoResultado, fx, pontos

	lerArquivo()

	arquivoResultado.write("P(x) = " + newton(fx, pontos))

	arquivoLer.close()	
	arquivoResultado.close()

main()