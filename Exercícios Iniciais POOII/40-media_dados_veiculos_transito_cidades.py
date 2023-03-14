cidades = {}
cidade_maior_indice_acidente = ''
cidade_menor_indice_acidente = ''

for i in range(5):
    cod_cidade = int(input('Digite o código da cidade: '))
    num_veiculos_de_passeio = int(input('Digite o número de veículos de passeio: '))
    num_acidentes_de_transito_com_vitima = int(input('Digite o número de acidentes de trânsito com vítimas: '))
    indice_acidente = num_acidentes_de_transito_com_vitima/num_veiculos_de_passeio
    cidades[cod_cidade] = [indice_acidente,num_veiculos_de_passeio,num_acidentes_de_transito_com_vitima]

    if cidade_maior_indice_acidente == '':
        cidade_maior_indice_acidente = cod_cidade
    elif cidades[cidade_maior_indice_acidente][0] < indice_acidente:
        cidade_maior_indice_acidente = cod_cidade

    if cidade_menor_indice_acidente == '':
        cidade_menor_indice_acidente = cod_cidade
    elif cidades[cidade_menor_indice_acidente][0] > indice_acidente:
        cidade_menor_indice_acidente = cod_cidade


print(f"A cidade com o menor indice de acidentes é a {cidade_menor_indice_acidente} com : {(cidades[cidade_menor_indice_acidente][0]):.2f}")
print(f"A cidade com o maior indice de acidentes é a {cidade_maior_indice_acidente} com : {(cidades[cidade_maior_indice_acidente][0]):.2f}")
print(f"A média de veículos nas cinco cidades é de {sum([cidades[i][1] for i in cidades])/len(cidades)}")
print(f"A média de acidentes nas cinco cidades é de {sum([cidades[i][2] for i in cidades])/len(cidades)}")
print(f"A média de acidente nas cidades com menos de 2000 veículos é de {sum([cidades[i][2] for i in cidades if cidades[i][1] < 2000])/len([cidades[i][2] for i in cidades if cidades[i][1] < 2000])}")