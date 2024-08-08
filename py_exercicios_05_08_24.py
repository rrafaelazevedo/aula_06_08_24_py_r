# vetores
# exercicio 1: crie um vetor com os números de 1 a 10 e imprima-o

vec = list(range(1, 11))
print(vec)

# exercicio 2: crie um vetor com os números pares de 2 a 20 e imprima-o
vec = list(range(2, 21, 2))
print(vec)

# exercicio 3: calcule a soma dos elementos de um vetor com numeros de 1 a 100
vec = list(range(1, 101))
soma_vec = sum(vec)
print(soma_vec)


# exercicio 4: encontre o maior e o menor valor em um vetor de numeros
# aleatorios entre 1 e 1000, de tamanho 50
import numpy as np
vec_aleatorio = np.random.randint(1, 1001, size=50)
print(vec_aleatorio)
vec_max = max(vec_aleatorio)
print(vec_max)
vec_min = min(vec_aleatorio)
print(vec_min)

# exercicio 5: criar um vetor com os 10 primeiros numeros primos
def n_primo(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
    return True
  
primos = []
num = 2
while len(primos) < 10:
  if n_primo(num):
    primos.append(num)
  num += 1
print(primos)

# exercicio 6: inverta a ordem dos elementos de um vetor aleatoio de tamanho 20
vec_aleatorio = np.random.randint(1, 100, size=20)
print(vec_aleatorio)
vec_invertido = (vec_aleatorio[::-1])
print(vec_invertido)

# exercicio 7: matrizes em python
# criar uma matriz 3x3 com numeros de 1 a 9
matriz = np.arange(1, 10).reshape(3, 3)
print(matriz)

# exercicio 8: crie uma matriz identidade 4x4
matrix_i = np.identity(4)
print(matrix_i)

# exercicio 9: soma de duas matrizes A e B, em que A e B são do tipo (2x2)
matrix_A = np.array([[1, 2],[3, 4]])
matrix_B = np.array([[5, 6],[7, 8]])
sum_matrix_A_B = matrix_A + matrix_B
print(sum_matrix_A_B)

# exercicio 10: multiplicacao de duas matrizes A e B, em que A e B são do tipo (2x2)
matrix_A = np.array([[1, 2],[3, 4]])
matrix_B = np.array([[5, 6],[7, 8]])
dot_matrix_A_B = np.dot(matrix_A, matrix_B)
print(dot_matrix_A_B)

# exercicio 11: calcule a transposta de uma matriz 3x3
matrix = np.array([[1, 2,3], [4, 5, 6], [7, 8, 9]])
matrix_transp = np.transpose(matrix)
print(matrix_transp)

# exercicio 12: calcule o determinante da matriz A (3x3)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
detA = np.linalg.det(A)
print('O determinante da matriz A é: ', detA)
