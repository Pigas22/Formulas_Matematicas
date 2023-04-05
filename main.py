import math


def fatorial(numero):
  
  total = numero
  for x in range(numero-1, 0, -1):
    st = total * x
    total =+ st

  return total


def arranjo(n, k):

  fatn = fatorial(n)
  fatnk = fatorial(n - k)
  formulafac = fatn / fatnk

  return formulafac


def comb(n, k):

  combn = fatorial(n)
  combk = fatorial(k)
  combnk = fatorial(n - k)
  formulacomb = combn / (combk * combnk)

  return formulacomb


def delta(a, b, c):
  
  delta = (b ** 2) - (4 * a * c)

  return delta
  

def verifydelt(delta):

  if delta < 0:
    return False

  elif delta >= 0:
    return True
    

def bhaskara(a, b, c):

  global delta
  
  delta = delta(a, b, c)
  valor1 = (-b + math.sqrt(delta)) / (2 * a)
  valor2 = (-b - math.sqrt(delta)) / (2 * a)  
  
  return delta, valor1, valor2


def anagrama(str):
  
  quantidade = len(str)
  quantidade = fatorial(quantidade)  

  return quantidade


def potencia(num, num2):

  conta = num ** num2

  return conta
"""
def permutrepit(str):
  semspace = str.strip()
  frase = len(semspace)
  multi = fatorial(frase)
  divi = 1
  
  for i in range(0, frase):
    iguais = frase.count(frase(i))
    if iguais > 1:
      divi *= iguais
      str = semspace.replace(frase(i), ' ')
"""


def bacterias(inicial, minutos):
  tempo = int(input('\nO tempo está em horas ou em segundos? O tempo tem de ser convertido para Minutos. \n[0] - Horas \n[1] - Minutos \n[2] - Segundos \nQual a sua escolha? '))
  min = minutos
  if tempo == 0:
    min *= 60

  elif tempo == 1:
    if min >= 20:
      min = min

    else:
      print('\nNão ouve diferença no número de bactérias. Pois o processo de divisão bacteriana demora 20 minutos.')
  
  elif tempo == 2:
    if min >= 1200:
      min /= 60

    else:
      print('\nNão ouve diferença no número de bactérias. Pois o processo de divisão bacteriana demora 20 minutos.')
      exit()
      
  else:
    exit()

  min /= 20
  num_bacterias = inicial * (2 ** min)
  if tempo == 0:
    print(f'\nO números de bactérias geradas num período de {minutos} horas, foi de: {num_bacterias} bactérias.')

  elif tempo == 1:
    print(f'\nO número de bactérias geradas num período de {minutos} minutos, foi de: {num_bacterias} bactérias.')
    
  elif tempo == 2:
    print(f'\nO número de bactérias geradas em um período de {minutos} segundos, foi de: {num_bacterias} bactérias.')


def linha():
  print(50 * '=')


while True:
  print('[0] - Sair \n[1] - Fatorial \n[2] - Arranjo e Combinação \n[3] - Bhaskara \n[4] - Anagrama Simples(sem rpetição) \n[5] - Potência \n[6] - Cálculo de Bactérias')
  escolha = int(input('\n-> O que você quer fazer? '))
  linha()
  
  if escolha == 0:
    print('Saindo...')
    break
    
  elif escolha == 1:
    pergunta1 = int(input('Qual Número você quer fatorar? '))
    result = fatorial(pergunta1)
    print(f'\nO resultado da fatoração é: {result}')

  elif escolha == 2:
    ordem = int(input('A ordem é importante no problema? \n[1] - Sim \n[2] - Não \nR: '))
    linha()
    if ordem == 1:
      pergunta1 = int(input('\n1º Número para fazer Arranjo? '))
      pergunta2 = int(input('2º número? '))
      result = arranjo(pergunta1, pergunta2)
      print(f'\nResultado: {result}')

    elif escolha == 2:
      pergunta1 = int(input('\n1º Número para fazer combinação? '))
      pergunta2 = int(input('2º número? '))
      result = comb(pergunta1, pergunta2)
      print(f'\nResultado: {result}')

    else:
      print('\nDesculpe não consegui entender, Tente Novamente!')

  elif escolha == 3:
    pergunta1 = int(input('Qual o valor de A: '))
    pergunta2 = int(input('Qual o valor de B: '))
    pergunta3 = int(input('Qual o valor de C: '))
    
    result = delta(pergunta1, pergunta2, pergunta3)
    
    verify = verifydelt(result)
    if not verify:
      print('\nNão é possível realizar conta com Delta negativo.')

    if verify:
      resposta = bhaskara(pergunta1, pergunta2, pergunta3)
      print('\nValor de Delta, Valor1 e Valor2. Respectivamente nessa ordem:', resposta)

  elif escolha == 4:
    pergunta1 = str(input('Quantos anagramas são possíveis formar com: '))
    result = anagrama(pergunta1)
    print(f'\nÉ possível fazer {result} anagramas com {pergunta1}')

  elif escolha == 5:
    pergunta1 = int(input('Número da base: '))
    pergunta2 = int(input('Número elevado: '))
    result = potencia(pergunta1, pergunta2)
    print(f'\nO resultado da potência do número {pergunta1} elevado ao número {pergunta2}, é igual à: {result}')

  elif escolha == 6:
    pergunta1 = int(input('Número de bactérias iniciais: '))
    pergunta2 = int(input('Tempo decorrido em minutos (o código possui convertor de horas e segundos para minutos.): '))
    bacterias(pergunta1, pergunta2)

  else:
    print('Desculpe :( não conseguir entender.\nTente novamente!')

  linha()
  