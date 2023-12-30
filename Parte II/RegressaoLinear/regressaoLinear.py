# Universidade Estadual de Santa Cruz
# Discnte: Flávia Alessandra Santos de Jesus
# Disciplina: Análise Numérica pelo Profº Gesil Sampaio

# Implementação do método de Regressão Linear

import math

# Lê a entrada e armazena os vetores x e y
def ler_entrada():
  x = []
  y = []

  with open("RegressaoLinear/entrada.txt", "r", encoding="utf-8") as arquivo:
    x = list(map(float, arquivo.readline().strip().split()))
    y = list(map(float, arquivo.readline().strip().split()))

  return x, y

x, y = ler_entrada()

def regressao_linear(x, y):

  xsom, ysom, xy, x2, i = 0, 0, 0, 0, 0
  tamX = len(x)

  for i in range(tamX):
    xsom = xsom + x[i]
    ysom = ysom + y[i]
    xy = xy + x[i] * y[i]
    x2 = x2 + x[i]**2

  a1 = (tamX * xy - (xsom * ysom)) / ((tamX * x2) - xsom**2)
  a0 = (ysom/tamX) - (a1 * (xsom/tamX))
    
  return a0, a1

a0, a1 = regressao_linear(x, y)

def coeficiente_correlacao(x, y):

  xsom, ysom, xy, x2, i, y2 = 0, 0, 0, 0, 0, 0
  tamX = len(x)

  for i in range(tamX):
    xsom = xsom + x[i]
    ysom = ysom + y[i]
    xy = xy + x[i] * y[i]
    x2 = x2 + x[i]**2
    y2 = y2 + y[i]**2

  r = (tamX * xy - (xsom * ysom)) / (math.sqrt(((tamX * x2) - xsom**2)) * math.sqrt(((tamX * y2) - ysom**2)))

  return r

r = coeficiente_correlacao(x, y)

# Salvar o resultado no arquivo "resultado.txt"
def salvar_resultado(a1, a0, r):
  with open("RegressaoLinear/resultado.txt", "w", encoding="utf-8") as arquivo:
      arquivo.write(f"y =~ {a0} + {a1}x\n")
      arquivo.write(f"r: {r}")
    
salvar_resultado(a1, a0, r)