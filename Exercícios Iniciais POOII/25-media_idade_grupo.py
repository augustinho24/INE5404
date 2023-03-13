qtd_pessoas = int(input("Quantidade de pessoas: "))
idades = []

for i in range(qtd_pessoas):
    idades.append(int(input(f"Idade da {i+1}ª pessoa: ")))

media = sum(idades)/qtd_pessoas
condicao = ""

if media >= 0 and media <=25: 
    condicao = "jovem"
elif media <= 60:
    condicao = "adulta"
elif media > 60:
    condicao = "idosa" 

print(f"A média etária do grupo de {qtd_pessoas} pessoas é de: {media:.0f} anos, no qual é considerada {condicao}.")


 
