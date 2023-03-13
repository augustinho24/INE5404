#Aluno mais baixo, mais alto, mais pesado e mais leve

pessoas = {}
mais_alto = ''
mais_baixo = ''
mais_pesado = ''
mais_leve = ''

nome = ''


while nome != 'exit':
    nome = input("Digite o nome: ")
    if nome == 'exit':
        break
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))
    pessoas[nome] = [altura,peso]

    if mais_alto == '':
        mais_alto = nome
    elif pessoas[mais_alto][0] < altura:
        mais_alto = nome
    
    if mais_baixo == '':
        mais_baixo = nome
    elif pessoas[mais_baixo][0] > altura:
        mais_baixo = nome

    if mais_pesado == '':
        mais_pesado = nome
    elif pessoas[mais_pesado][1] < peso:
        mais_pesado = nome

    if mais_leve == '':
        mais_leve = nome
    elif pessoas[mais_leve][1] > peso:
        mais_leve = nome

media_altura = sum([pessoas[i][0] for i in pessoas])/len(pessoas)
media_peso = sum([pessoas[i][1] for i in pessoas])/len(pessoas)

print(f"{'='*30} Dados {'='*30}")
print(f"- O cliente mais alto é {mais_alto} com {pessoas[mais_alto][0]}m")
print(f"- O cliente mais baixo é {mais_baixo} com {pessoas[mais_baixo][0]}m")
print(f"- O cliente mais pesado é {mais_pesado} com {pessoas[mais_pesado][1]}kg")
print(f"- O cliente mais leve é {mais_leve} com {pessoas[mais_leve][1]}kg")
print(f"- Média de altura dos clientes: {media_altura:.2f}m")
print(f"- Média de peso dos clientes: {media_peso:.2f}kg")
print(f"{'='*30} ///// {'='*30}")




