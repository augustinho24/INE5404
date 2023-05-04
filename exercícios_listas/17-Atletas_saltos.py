def media(x):
    media_saltos = sum(x)/len(x)
    media_saltos = round(media_saltos,2)
    return media_saltos

atletas = {}

while True:
    nome = input()
    if nome == "": break
    saltos = [float(x) for x in input('Saltos: ').split()]
    while len(saltos) != 5:
        saltos = [float(x) for x in input('Saltos (insira novamente): ').split()]
    atletas[nome] = saltos


for u,v in atletas.items():

    print(f'Atleta: {u}')
    print(f'Primeiro salto: {v[0]} m\nSegundo salto: {v[1]} m\nTerceiro salto: {v[2]} m\nQuarto salto: {v[3]} m\nQuinto salto: {v[4]} m')

    print('\nResultado final:')
    print(f'Atleta: {u}')
    print(f'Saltos: {v[0]} - {v[1]} - {v[2]} - {v[3]} - {v[4]}')
    print(f'Média dos saltos: {media(v)} m\n')

#melhor_atleta = max(atletas, key=lambda key: atletas[key])
#print('\nResultado final:')






