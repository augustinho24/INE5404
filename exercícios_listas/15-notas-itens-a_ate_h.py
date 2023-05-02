valores = []
qtd_valores_acima_media = 0
qtd_valores_abaixo_7 = 0

while True:
    valor = float(input())
    if valor == -1: break
    valores.append(valor)

soma_valores = sum(valores)
media_valores = (soma_valores/len(valores))

for i in range(len(valores)):
    if valores[i] > media_valores: qtd_valores_acima_media += 1
    if valores[i] < 7: qtd_valores_abaixo_7 +=1

print("Quantidade de valores:", len(valores))
print()
print("Exibindo lado a lado:", *valores)
print()
print("Exibindo pela ordem inversa, um abaixo do outro: ")
for valor in valores[::-1]:
    print(valor)
print()
print("Soma dos valores:", soma_valores)
print()
print("Média dos valores:", round(media_valores,4))
print()
print("Quantidade de valores acima da média: ",qtd_valores_acima_media)
print()
print("Quantidade de valores abaixo que 7(sete):", qtd_valores_abaixo_7)
print()
print("Programa encerrado. DADINHO É O CARALHO, MEU NOME AGORA É ZÉ PEQUENO, PORRA.")




