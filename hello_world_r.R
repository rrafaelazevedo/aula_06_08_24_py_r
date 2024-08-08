nome <- 'Rafael'
idade <- 25
altura = 1.74
altura > 1.70
idade < 20


print(nome)
print(idade)
print(altura)

print(typeof(nome))
print(typeof(idade))
print(typeof(altura))


PI <- 3.14159265
mensagem <- 'texto arbitrário'
print(mensagem)
print(typeof(mensagem))

#double
numero <- 100
print(typeof(numero))     

#data/hora
data_atual <- Sys.time()
d <- Sys.Date()
print(d)
print(data_atual)


#enumerar (factor)
DiasDaSemana <- factor(c('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'))
print(DiasDaSemana[3])
