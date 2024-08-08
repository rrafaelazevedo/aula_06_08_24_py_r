print('Hello World')
nome = 'Rafael'
idade = 25
altura = 1.74
altura > 1.70
idade < 25


print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura )
print(type(nome))
print(type(idade))
print(type(altura))

PI = 3.14159265
mensagem = 'texto arbitrário'
print(mensagem)
print(type(mensagem))

# inteiro
numero = 100

#data e hora
from datetime import datetime
data_atual = datetime.now()
print(data_atual)


#enumerar
from enum import Enum

class DiasDaSemana(Enum):
  Segunda = 1
  Terca = 2
  Quarta = 3
  Quinta = 4
  Sexta = 5
  Sabado = 6

print(DiasDaSemana.Quarta.value)
print(DiasDaSemana.Quarta.name)
  
  
