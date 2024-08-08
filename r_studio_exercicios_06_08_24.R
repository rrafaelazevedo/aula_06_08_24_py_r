# Fatores em R
# Exercício facil: crue um vetor de categorias (fatores) com as cores
# "vermelho", "azul" e "verde"
cores <- factor(c("vermelho", "azul", "verde"))
print(cores)

# Exercício fácil: Crie um vetor de fatores os dias da semana e imprima-os.
semana <- factor(c("segunda", "terça", "quarta", "quinta", "sexta"))
print(semana)

#Exercício Médio: Crie um vetor de fatores com as
#Categorias "baixo", "medio" e "alto" e ordene-os
niveis <- factor(c("Baixo", "Alto", "Medio"), levels = c("Baixo", "Medio", "Alto"), ordered = TRUE)
print(niveis)

#Exercício Médio: Converta um vetor de fatores em um vetor numérico
categorias <- factor(c("Baixo", "Alto", "Medio"), levels = c("Baixo", "Medio", "Alto"), ordered = TRUE)
numeros <- as.numeric(categorias)
print(numeros)

#Exercício Dificil: Crie um vetor de fatores com as categorias
# "pequeno", "medio" e "grande", e substitua "pequeno" por "extra pequeno"
tamanhos <- factor(c("pequeno", "medio", "grande"), levels = c("pequeno", "medio", "grande"), ordered = TRUE)
levels(tamanhos)[levels(tamanhos) == "pequeno"] <- "extra pequeno"
print(tamanhos)

#Exercício Dificil: Crie um vetor de fatores com 100 elementos aleatorios entre 
# "baixo", "medio" e "alto", e calcule a frequência de cada categoria
set.seed(123)
categorias <- c("baixo", "medio", "alto")
vetor <- sample(categorias, 100, replace = TRUE)
fatores <- factor(vetor, levels = categorias, ordered = TRUE)
frequencias <- table(fatores)
print(frequencias)

# Listas em R
# Exercício Fácil: Crie uma lista contando os números de 1 a 5.
lista <- list(1,2,3,4,5)
print(lista)

# Exercício Fácil: Adicione um elemento "6" ao final da lista [1,2,3,4,5].
lista[[6]] <- 6
print(lista)

#Exercicio Medio: Remova o terceiro elemento da lista [1,2,3,4,5].
lista <- lista[-3]
print(lista)

# Exercicio Dificil: Inverta a ordem dos elementos da lista [1,2,3,4,5]
lista_invertida <- rev(lista)
print(lista_invertida)

# Exercicio Dificil: Crie uma lista de listas (Matriz)
# de tamanho 3x3 e calcule a soma de cada linha
matriz <- list(c(1,2,3),c(4,5,6),c(7,8,9))
soma_linhas <- sapply(matriz, sum)
print(soma_linhas)

#Tupla em R
# Exercicio facil: Crie uma tupla contendo os números de 1 a 5 e imprima-a
tupla <- list(1,2,3,4,5)
print(tupla)

# Exercicio facil: Acesse o terceiro elemento da tupla (1,2,3,4,5) e imprima-o
tupla <- list(1,2,3,4,5)
print(tupla[[3]])

# Exercicio Médio: Crie uma tupla contendo três tuplas internas
# cada uma com dois elementos, imprima-a
tupla <- list(list(1,2), list(3,4), list(5,6))
print(tupla)

# Exercicio Médio: Concatene duas tuplas (1,2,3) e (4,5,6) e imprima o resultado
lista1 <- list(1,2,3)
lista2 <- list(4,5,6)
lista_concatenada <- c(lista1, lista2)
print(lista_concatenada)

# Exercício Dificil: Crie uma tupla com os elementos (1,2,3,4,5)
# e verifique se o número 3 está na tupla
lista <- list(1,2,3,4,5)
existe <- 3 %in% lista
print(existe)

# Exercício Dificil: Crie uma tupla com os elementos (1,2,3,4,5)
# e encontre o indice do numero 4
lista <- list(1,2,3,4,5)
indice <- which(unlist(lista) == 4)
print(indice)

# Dicionarios em R
# Exercicio facil: Crie um dicionario com as chaves 'nome', 'idade', e 'cidade'
# e valores 'Ana', 25 e 'São Paulo' respectivamente.
dicionario1 <- list(nome = "Ana", idade = 25, cidade="São Paulo")
print(dicionario1)

# Acesse o valor associado a chave "idade" no dicionario
# {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
dicionario <- list(nome="Ana", idade=25, cidade="São Paulo")
idade <- dicionario$idade
print(idade)

# Exercicio Medio: adicione um novo par chave-valor "profissão": "Engenheira"
# ao dicionario ["nome": "Ana", "idade": 25, "cidade": "São Paulo"]
dicionario <- list(nome="Ana", idade=25, cidade="São Paulo")
dicionario$profissão <- "engenheira"
print(dicionario)

#