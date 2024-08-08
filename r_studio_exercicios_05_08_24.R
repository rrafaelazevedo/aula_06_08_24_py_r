# vetores

# exercicio 1: crie um vetor com os números de 1 a 10 e imprima-o

vec <- 1:10
print(vec)

# exercicio 2: crie um vetor com os números pares de 2 a 20 e imprima-o

vec <- seq(2, 20, by=2)
print(vec)

# exercicio 3: calcule a soma dos elementos de um vetor com numeros de 1 a 100
vec <- 1:100
soma_vec <- sum(vec)
print(soma_vec)

# exercicio 4: encontre o maior e o menor valor em um vetor de numeros
# aleatorios entre 1 e 1000, de tamanho 50
vec <- sample(1:1000, 50, replace=TRUE)
vec_max <- max(vec)
vec_min <- min(vec)
print(paste('Maior: ', vec_max, 'Menor: ', vec_min))

# exercicio 5: criar um vetor com os 10 primeiros numeros primos
eh_primo <- function(n){
  if(n<= 1){
    return(FALSE)
  }
  for (i in  2:sqrt(n)){
    if(n %% i == 0 ){
      return(FALSE)
      
    }
  }
  return(TRUE)
}


primos <- c()
num <- 2 
while (length(primos)< 10){
  if(eh_primo(num)){
    primos <- c(primos, num)
  }
  num <- num + 1
}

print(primos)


# exercicio 6: inverta a ordem dos elementos de um vetor aleatoio de tamanho 20
vec_aleatorio <- sample(1: 100, 20, replace = TRUE)
print(vec_aleatorio)
vec_invertido <- rev(vec_aleatorio)
print(vec_invertido)

# matrizes em python
# exercicio 7: criar uma matriz 3x3 com numeros de 1 a 9
matriz <- matrix(1:9, nrow=3, ncol=3)
print(matriz)

# exercicio 8: crie uma matriz identidade 4x4
matrix_i <- diag(4)
print(matrix_i)         

# exercicio 9: soma de duas matrizes A e B, em que A e B são do tipo (2x2)

matriz_A <- t(matrix(c(1, 2, 3, 4), nrow = 2, ncol = 2))
matriz_B <- t(matrix(c(5, 6, 7, 8), nrow = 2, ncol = 2))
sum_matriz_A_B <- matriz_A + matriz_B
print(sum_matriz_A_B)


# exercicio 10: multiplicação de duas matrizes A e B, em que A e B são do tipo (2x2)
matriz_A <- t(matrix(c(1, 2, 3, 4), nrow = 2, ncol = 2))
matriz_B <- t(matrix(c(5, 6, 7, 8), nrow = 2, ncol = 2))
dot_matriz_A_B <- matriz_A %*% matriz_B
print(dot_matriz_A_B)

# exercicio 11: calcule a transposta de uma matriz 3x3
matriz_transp <- t(matrix(1:9, nrow = 3, ncol = 3))
print(matriz_transp)
            

# exercicio 12: calcule o determinante da matriz A (3x3)
matriz <- matrix(1:9, nrow = 3, ncol=3)
determinante <- det(matriz)
print(determinante)
            
            
