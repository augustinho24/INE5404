votos_enquete = {}

while True:
    voto = int(input('Qual o melhor Sistema Operacional para uso em servidores?\n As possíveis respostas são:\n\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n\nDigite sua resposta: '))
    if voto == 0: break

    while voto < 0 or voto > 6:
        voto = int(input('Informe um valor entre 1 e 6 ou 0 para sair!'))

        if voto in votos_enquete.keys():
            votos_enquete[voto] += 1
        else:
            votos_enquete[voto] = 1


total_votos = sum(votos_enquete.values())
if total_votos == 0:
    total_votos = 1


print('Total                    ', total_votos)

#ARRUMAR DEPOIS

# print('O Sistema Operacional mais votado foi o', max(votos_enquete, key=lambda key: votos_enquete[key]), 'com', max(votos_enquete.values()), 'votos, correspondendo a', round((max(votos_enquete.values())/total_votos)*100,2), '% do total de votos.')