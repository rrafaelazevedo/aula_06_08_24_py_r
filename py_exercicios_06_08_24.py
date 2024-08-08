#Fatores em Python
# Exercício facil: crue um vetor de categorias (fatores) com as cores
# "vermelho", "azul" e "verde"

import pandas as pd
cores = pd.Categorical(['vermelho', 'azul', 'verde'])
print(cores)

# Exercício fácil: Crie um vetor de fatores os dias da semana e imprima-os.
import pandas as pd
semana = pd.Categorical(['segunda', 'terca', 'quarta', 'quinta', 'sexta'])
print(semana)

#Exercício Médio: Crie um vetor de fatores com as
#Categorias "baixo", "medio" e "alto" e ordene-os
import pandas as pd
niveis = pd.Categorical(["Baixo", "Alto", "Medio"], categories=["Baixo", "Medio", "Alto"], ordered=True)
print(niveis)

#Exercício Médio: Converta um vetor de fatores em um vetor numérico
import pandas as pd
categorias = pd.Categorical(["Baixo", "Alto", "Medio"], categories=["Baixo", "Medio", "Alto"], ordered=True)
numeros = categorias.codes
print(numeros)

#Exercício Dificil
#Crie um vetor de fatores com as categorias pequeno medio e grande e substitua pequeno por extra pequeno
import pandas as pd
tamanhos = pd.Categorical(['pequeno','medio','grande'], categories=['pequeno','medio','grande'], ordered = True)
tamanhos2 = tamanhos.rename_categories({'pequeno': 'extra pequendo'})
print(tamanhos)
print(tamanhos2)

#Exercício Dificil: Crie um vetor de fatores com 100 elementos aleatorios entre 
# "baixo", "medio" e "alto", e calcule a frequência de cada categoria
import pandas as pd
import random
categorias = ['baixo','medio','alto']
vetor = [random.choice(categorias) for _ in range(100)]
fatores = pd.Categorical(vetor, categories=categorias, ordered = True)
frequencias = pd.value_counts(fatores)
print(frequencias)

# Listas em Python
# Exercício Fácil: Crie uma lista contando os números de 1 a 5.
numeros1 = [1, 2, 3, 4, 5]
print(numeros1)

# Exercício Fácil: Adicione um elemento "6" ao final da lista [1,2,3,4,5].
numeros1.append(6)
print(numeros1)

# Exercicio Medio: Remova o terceiro elemento da lista [1,2,3,4,5].
numeros1.pop(2)
print(numeros1)

# Exercicio Dificil: Inverta a ordem dos elementos da lista [1,2,3,4,5]
numeros1.reverse()
print(numeros1)

# Exercicio Dificil: Crie uma lista de listas (Matriz)
# de tamanho 3x3 e calcule a soma de cada linha
matriz = [[1,2,3],[4,5,6],[7,8,9]]
soma_linhas = [sum(linha) for linha in matriz]
print(soma_linhas)

# Tuplas Python
# Exercicio facil: Crie uma tupla contendo os números de 1 a 5 e imprima-a
tupla = (1,2,3,4,5)
print(tupla)

# Exercicio facil: Acesse o terceiro elemento da tupla (1,2,3,4,5) e imprima-o
tupla = (1,2,3,4,5)
print(tupla[2])

# Exercicio Médio: Crie uma tupla contendo três tuplas internas
# cada uma com dois elementos, imprima-a
tupla = ((1,2),(3,4),(5,6))
print(tupla)

# Exercicio Médio: Concatene duas tuplas (1,2,3) e (4,5,6) e imprima o resultado
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)

# Exercício Dificil: Crie uma tupla com os elementos (1,2,3,4,5)
# e verifique se o número 3 está na tupla
tupla = (1,2,3,4,5)
existe = 3 in tupla
print(existe)

# Exercício Dificil: Crie uma tupla com os elementos (1,2,3,4,5)
# e encontre o indice do numero 4
tupla = (1,2,3,4,5)
indice = tupla.index(4)
print(indice)

# Dicionarios em Python
# Exercicio facil: Crie um dicionario com as chaves 'nome', 'idade', e 'cidade'
# e valores 'Ana', 25 e 'São Paulo' respectivamente.
dicionario = {"nome": "ana", "idade" : "25" , "cidade" : "São Paulo"}
print(dicionario)

# Acesse o valor associado a chave "idade" no dicionario
# {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
dicionario = {"nome": "ana", "idade" : "25" , "cidade" : "São Paulo"}
idade = dicionario['Idade']
print(idade)

# Exercicio Medio: adicione um novo par chave-valor "profissão": "Engenheira"
# ao dicionario ["nome": "Ana", "idade": 25, "cidade": "São Paulo"]
dicionario = {"nome": "ana", "idade" : "25" , "cidade" : "São Paulo"}
dicionario["profissão"] = "engenheira"
print(dicionario)
