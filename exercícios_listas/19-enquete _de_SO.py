votos_enquete = {}

while True:
    voto = int(input('Qual o melhor Sistema Operacional para uso em servidores?\n As possíveis respostas são:\n\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n\nDigite sua resposta: '))
    if voto == 0: break

    while voto < 0 or voto > 6:
        voto = int(input('Informe um valor entre 1 e 6 ou 0 para sair!'))

        if voto in votos_enquete:
            votos_enquete[voto] += 1
        else:
            votos_enquete[voto] = 1


'''print('Resultado da votação:\n')
print('Foram computados', len(jogadores), 'votos\n')
print('Jogador\tVotos\t%')
for u,v in jogadores.items():
    print(f'{u}\t{v}\t{round((v/len(jogadores))*100,2)}%')

print('\nO melhor jogador foi o número', max(jogadores, key=lambda key: jogadores[key]), 'com', max(jogadores.values()), 'votos, correspondendo a', round((max(jogadores.values())/len(jogadores))*100,2), '% do total de votos.')

'''

print('Sistema Operacional\tVotos\t%')
print('Windows Server\t\t', votos_enquete.get(1, 0), '\t', round((votos_enquete.get(1, 0)/sum(votos_enquete.values()))*100,2), '%')
print('Unix\t', votos_enquete.get(2, 0), '\t', round((votos_enquete.get(2, 0)/sum(votos_enquete.values()))*100,2), '%')   
print('Linux\t', votos_enquete.get(3, 0), '\t', round((votos_enquete.get(3, 0)/sum(votos_enquete.values()))*100,2), '%')   
print('Netware\t', votos_enquete.get(4, 0), '\t', round((votos_enquete.get(4, 0)/sum(votos_enquete.values()))*100,2), '%')   
print('Mac OS\t', votos_enquete.get(5, 0), '\t', round((votos_enquete.get(5, 0)/sum(votos_enquete.values()))*100,2), '%')   
print('Outra\t', votos_enquete.get(6, 0), '\t', round((votos_enquete.get(6, 0)/sum(votos_enquete.values()))*100,2), '%')  