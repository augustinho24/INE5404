alunos = {}
idades = []
alturas = []
alunos_mais_13_anos_altura_inferior_media = []

for i in range(30):
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    altura = float(input("Altura do aluno: "))
    alunos[nome] = [idade, altura]
    idades.append(idade)
    alturas.append(altura)

media_alturas = sum(alturas)/len(alturas)

for aluno in alunos:
    if alunos[aluno][0] > 13 and alunos[aluno][1] < media_alturas:
        alunos_mais_13_anos_altura_inferior_media.append(aluno)
        
print("Média das idades:", media_alturas)

#imprimir os itens da lista "Alunos com altura abaixo da média", quebrando uma linha para cada item sem utlizar laço de "for".
print("Alunos com altura abaixo da média:") 
print(*alunos_mais_13_anos_altura_inferior_media, sep = "\n")




    
