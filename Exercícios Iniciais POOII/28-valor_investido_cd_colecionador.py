
qtd_cds = int(input())
valores_cds = []

for i in range(qtd_cds):
    valores_cds.append(float(input()))

print()
print(f"Quantidade de CD's: {qtd_cds}")
print(f"Valor médio para cada CD: {(sum(valores_cds)/qtd_cds):.2f}")






