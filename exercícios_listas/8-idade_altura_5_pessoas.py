pessoas = {}

for i in range(5):
    nome = input()
    idade = int(input())
    altura = float(input())
    pessoas[nome] = [idade,altura]

#percorrer o dicionário na ordem inversa
pessoas = dict(reversed(list(pessoas.items())))
for u,v in pessoas.items():
    print(u,v[0],v[1])



    