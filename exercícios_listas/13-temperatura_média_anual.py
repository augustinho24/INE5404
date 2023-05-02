meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho','Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

temperaturas = [float(x) for x in input().split()]
while len(temperaturas) != 12:
    print("Insira novamente: ")
    temperaturas = [float(x) for x in input().split()]

matriz_temp_meses = []
for i in range(12):
    matriz_temp_meses.append([meses[i], temperaturas[i]])

media_anual = sum(temperaturas)/len(temperaturas)

for i in range(12):
    print(f"{matriz_temp_meses[i][0]} - {(matriz_temp_meses[i][1]):.2f}")
print()
print(f"Média anual: {media_anual:.2f}")

