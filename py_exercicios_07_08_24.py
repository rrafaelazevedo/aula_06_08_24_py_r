# exercicio: adicione um novo par chave-valor 'profissão': 'engenheiro'
# ao dicionário {"nome": "Ana", "idade": "25", "cidade": "São Paulo"}
dic = {"nome": "Ana", "idade": "25", "cidade": "São Paulo"}
dic['profissão'] = 'engenheira'
print(dic)

# exercicio: remova a chave 'cidade' do dicionário
#{"nome": "Ana", "idade": "25", "cidade": "São Paulo"}
dic = {"nome": "Ana", "idade": "25", "cidade": "São Paulo"}
del dic['cidade']
print(dic)

# exercicio: crie um dicionário aninhado para armazenar informações
# de varias pessoas, onde cada pessoa tem nome, idade e cidade
dic_pessoal = {
              'pessoa1': {'nome': 'Rafael', 'idade': 25, 'cidade': 'São Paulo'},
              'pessoa2': {'nome': 'Gustavo','idade': 19, 'cidade': 'Santo André'},
              'pessoa3': {'nome': 'Igor', 'idade': 19, 'cidade': 'Santo André'}
              }
print(dic_pessoal)

# exercicio: percoca um dicionario aninhado e imprima as 
# informações de cada pessoa no formato 'Nome: Ana, Idade: 25, Cidade: São Paulo'.

for pessoa, dados in dic_pessoal.items():
  print(f'Nome: {dados["nome"]}, Idade: {dados["idade"]}, Cidade: {dados["cidade"]}')
  
  
  
# exercicio: soma de números
soma_n = 7 + 7
print(soma_n)

# exercicio: subtraçao de numeros
subtrai_n = 7 - 7
print(subtrai_n)

# exercicio: multiplicacao de numeros
mult_n = 7 * 7
print(mult_n)


# exercicio : divisão de numeros
div_n = 7/7
print(div_n)

# exercicio: exponenciacao de numeros
exp_n = 7 ** 7
print(exp_n)

# exercicio: resto da divisao entre dois numeros (funcao_mod)
mod_n = 8 % 7
print(mod_n)

#lógicos
#exercicio: verificação se um numero n1 é maior que o n2
n1 = 1
n2 = 2
print(n1 > n2)

#lógicos
#exercicio: verificação se um numero n1 é menor que o n2
n1 <- 1
n2 <- 2
print(n1 < n2)

# exercicio: verifique se o numero n1 é maior que n2 e menor que n3
n1 = 7
n2 = 5
n3 = 10
result = n2 < n1 < n3
print(result)

# exercicio: verique se o numero n é par e se esta entre 10 e 15
n = 12
result == (n % 2 == 0) and (n > 10 and n < 15)
#if n % 2 == 0 and n >= 10 and n <= 15:
 # True
#else:
  #False

# exercicio: verifique se um numero n é multiplo de 3 ou de 5
# e se está entre 20 e 30
n = 25
multiple_3_or_5 = (n % 3 == 0) or (n % 5 == 0) and (20 <= n <= 30)
print(multiple_3_or_5)  


  




    
