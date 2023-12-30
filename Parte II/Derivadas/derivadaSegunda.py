# Universidade Estadual de Santa Cruz
# Discente: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

# Implementação do método da Derivada de Segunda Ordem

from math import *

arquivoLer = open('Derivadas/entrada.txt', 'r')
arquivoResultado = open('Derivadas/resultado.txt', 'w')

def lerArquivo():
    
	global arquivoLer, funcao, x

	funcao = arquivoLer.readline()
	x = float(arquivoLer.readline())
 
def func(x):

  global funcao
  
  return eval(funcao)


def derivadaSegunda(x):

  return str((func(x + 1) - func(x)) - (func(x) - func(x - 1)))


def main():

  global arquivoResultado, x

  lerArquivo()

  arquivoResultado.write("f''(x) = " + derivadaSegunda(x))
  arquivoLer.close()	
  arquivoResultado.close()

main()