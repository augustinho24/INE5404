import time

# Criando um conjunto com 10 milhões de elementos
conjunto = set(range(10000000))

# Criando uma lista com 10 milhões de elementos
lista = list(range(10000000))

# Valor a ser pesquisado
valor = 9999999

# Pesquisa no conjunto
inicio_conjunto = time.time()
encontrado_conjunto = valor in conjunto
fim_conjunto = time.time()
tempo_conjunto = fim_conjunto - inicio_conjunto

# Pesquisa na lista
inicio_lista = time.time()
encontrado_lista = valor in lista
fim_lista = time.time()
tempo_lista = fim_lista - inicio_lista

# Imprimindo os resultados
print("Tempo de pesquisa no conjunto:", tempo_conjunto)
print("Tempo de pesquisa na lista:", tempo_lista)