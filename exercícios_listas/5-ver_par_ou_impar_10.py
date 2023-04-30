numeros = [int(x) for x in input().split()]
PARES = []
IMPARES = []

while not len(numeros) == 20:
    numeros = [int(x) for x in input().split()]

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        PARES.append(numeros[i])
    else:
        IMPARES.append(numeros[i])

print("Números:", *numeros)
print("PARES:", *PARES)
print("ÍMPARES:", *IMPARES)
