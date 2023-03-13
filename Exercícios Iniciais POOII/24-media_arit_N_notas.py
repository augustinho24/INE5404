n = int(input('Quantidade de notas: '))
notas = []

for cu in range(n):
    notas.append(float(input(f"Insira o valor da {cu+1}ª nota: ")))

media = sum(notas)/n
print(f"{media:.1f}")

