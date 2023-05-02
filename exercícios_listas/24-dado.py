import random

def lanca_dado():
    return random.randint(1, 6)

jogadas = {}

for i in range (100):
    dado = lanca_dado()
    if dado in jogadas:
        jogadas[dado] += 1
    else:
        jogadas[dado] = 1

print("Valor do daoo mais lançado: ", max(jogadas, key=jogadas.get), " vezes")

print("Lançamentos: ")
for i in jogadas:
    print("Número: ", i, "Jogadas: ", jogadas[i])
