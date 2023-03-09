def media(x):
    return sum(x)/len(x)

numeros = []

for _ in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

print(f"Média: {media(numeros)}")
print(f"Soma: {sum(numeros)}")
