# Universidade Estadual de Santa Cruz
# Discnte: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

# Implementação do método de Lagrange

from sympy import *

fx = []
pontos = []
x = symbols('x')

arquivoLer = open('Lagrange/entrada.txt', "r")
arquivoResultado = open("Lagrange/resultado.txt", "w")

def pegarValores():
	
	global arquivoLer, fx, pontos

	aux = arquivoLer.readline()
	while(aux != '\n'):
		aux = float(aux)
		fx.append(aux)
		aux = arquivoLer.readline()
  
	aux = arquivoLer.readline()
	while(aux != '' and aux != '\n'):
		aux = float(aux)
		pontos.append(aux)
		aux = arquivoLer.readline()
	
def Polinomios(k, pontos, n):
	
    L = 1
    for i in range(n):
        if i != k:
            L *= Poly((x - pontos[i]) / (pontos[k] - pontos[i]))
    return L

def lagrange(fx, pontos):
	
	P = 0.0
	Poli = 0
 
	for k in range(len(pontos)):
		Poli = Polinomios(k, pontos, len(pontos))
		P = P + fx[k] * Poli

	return str(P.args[0])

def main():
	
	global arquivoResultado, fx, pontos

	pegarValores()

	arquivoResultado.write("P(x) = " + lagrange(fx, pontos))
	arquivoLer.close()	
	arquivoResultado.close()

main()