# exercicio: remova a chave 'cidade' do dicionário
#{"nome": "Ana", "idade": "25", "cidade": "São Paulo"}
dic <- list(nome='Ana', idade=25, cidade='São Paulo')
dic$cidade <- NULL
print(dic)

# exercicio: crie um dicionário aninhado para armazenar
# informaçõpoes de várias pesssoas, onde caa uma tem nome, idade e cidade
dic <- list(
  pessoa1 = list(nome='Rafael', idade=26, cidade='São Paulo'),
  pessoa2 = list(nome='Leib', idade=55, cidade='Sao Caetano'),
  pessoa3 = list(nome='New', idade=45, cidade='Santo André')
)
print(dic)


# exercicio: percorra um dicionario aninhado e imprima as
# informações de cada pessoa no formato "Nome": Ana, Idade: 25, Cidade: "São Paulo".
dicionario <- list(
  pessoa1 <- list(nome = "Ana", idade=25 , cidade="São Paulo"),
  pessoa2 <- list(nome = "Carolina", idade= 95 , cidade="Araraquara"),
  pessoa3 <- list(nome = "Anabela", idade= 45 , cidade="Toque-Toque Grande"),
  pessoa4 <- list(nome = "Anafeia", idade= 10 , cidade="Toque-Toque Pequeno")
)

for (pessoa in dicionario){
  print(paste("Nome:", pessoa$nome, ", Idade:", pessoa$idade, ", Cidade:", pessoa$cidade))
}


# operadores aritméticos em R
# exercicio: soma de números
soma_n <- 7 + 7
print(soma_n)

# exercicio: subtraçao de numeros
subtrai_n <- 7 - 7
print(subtrai_n)

# exercicio: multiplicacao de numeros
mult_n <- 7 * 7
print(mult_n)


# exercicio : divisão de numeros
div_n <- 7/7
print(div_n)

# exercicio: exponenciacao de numeros
exp_n <- 7 ^ 7
print(exp_n)

# exercicio: resto da divisao entre dois numeros (funcao_mod)
mod_n <- 8 %% 7
print(mod_n)

#lógicos
#exercicio: verificação se um numero n1 é maior que o n2
n1 <- 1
n2 <- 2
print(n1 > n2)

#lógicos
#exercicio: verificação se um numero n1 é menor que o n2
n1 <- 1
n2 <- 2
print(n1 < n2)

# exercicio: verifique se o numero n1 é maior que n2 e menor que n3
n1 <- 7
n2 <- 5
n3 <- 10
result <- n1 > n2 & n1 < n3
print(result)


# exercicio: verique se o numero 12 é par e se esta entre 10 e 15
result <- (12 %% 2 == 0) & (12 > 10 & 12 < 15)
print(result)

# exercicio: verifique se um numero n é multiplo de 3 ou de 5
# e se está entre 20 e 30
n <- 25
multiple_3_or_5 <- (n %% 3 == 0) | (n %% 5 == 0) & (20 > n < 30)
print(multiple_3_or_5)  




