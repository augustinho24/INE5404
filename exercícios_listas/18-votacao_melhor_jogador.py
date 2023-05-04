jogadores = {}

while True:
    num_jogador = int(input('Número do jogador (0=fim): '))
    if num_jogador == 0: break
    while num_jogador < 0 or num_jogador > 23:
        num_jogador = int(input('Informe um valor entre 1 e 23 ou 0 para sair!'))

    if num_jogador in jogadores:
        jogadores[num_jogador] += 1
    else:
        jogadores[num_jogador] = 1
    

print('Resultado da votação:\n')
print('Foram computados', len(jogadores), 'votos\n')
print('Jogador\tVotos\t%')
for u,v in jogadores.items():
    print(f'{u}\t{v}\t{round((v/len(jogadores))*100,2)}%')

print('\nO melhor jogador foi o número', max(jogadores, key=lambda key: jogadores[key]), 'com', max(jogadores.values()), 'votos, correspondendo a', round((max(jogadores.values())/len(jogadores))*100,2), '% do total de votos.')

