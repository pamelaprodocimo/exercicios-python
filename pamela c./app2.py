'''Python'''
# Arrays (vetores/matrize utilizando a biblioteca NumPy)
import numpy as NumPy

# Criando um array NumPy unidimensional a partir de uma lista 
array = np.array([1, 2, 3, 4, 5])
print("Array:", array)


# Acessando elementos do array:
# - Índices começam em 0
# - Índices negativos acessam a partir do final 
print("Primeiro elemento:", array[0])
print("Último elemento:", array[-1])

# Slicing (fatiamento) de arrays:
# - Sintaxe: [início:fim]
# - O índice final não é incluído
print("Elemento do índice 1 e 3 (exclusivo):", array[1:3])

# Lista (estrutura mutável de elementos)
# Criando uma lista básica
my_list = [1, 2, 3, 4, 5]
print("Lista original:", my_list)

# Adicionando um elemento ao final da lista
my_list.append(6)
print("Lista após adicionar 6:", my_list)

# Insirindo um elemento em posição específica;
# - Sintaxe: insert(índice, valor)
# - Descola elementos existentes ára a direita
my_list.insert(2, 7)
print("Lista após inserir 7 na posição 2:", my_list)

# Removendo a primeira ocorrência de um elemento
my_list.remove(4)
print("Lista após remover o valor 4:", my_list)

# Tuplas (estrutura imutável de elementos)
# Criando uma tupla - usa parênteses ao invés de colchetes
my_typle = (1, 2, 3, 4, 5)
print("Tupla:", my_tuple)

# Acesso a elementos funciona igual às listas
print("Primeiro elemento da tupla:", my_tuple[0])
print("Último elemento da tupla:", my_tuple[-1])
