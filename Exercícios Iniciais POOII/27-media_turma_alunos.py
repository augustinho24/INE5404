#Calculo médio, alunos/turma.

turmas = []
qtd_turmas = int(input("Quantidade de turmas: "))
qtd_alunos_por_turma = int(input('Quantidade máxima de alunos permitida: '))

while qtd_alunos_por_turma > 40:
    qtd_alunos_por_turma = int(input('Inválido, quantidade de alunos não pode exceder 40 indivíduos, insira novamente:  '))

for i in range(qtd_turmas):
    qtd_alunos = int(input(f'Quantidade de alunos para a {i+1}ª turma: '))
    while qtd_alunos < 0 or qtd_alunos > qtd_alunos_por_turma:
        qtd_alunos = int(input(f'Inválido, insira novamente a quantidade de alunos para a {i+1}ª turma: '))
    turmas.append(qtd_alunos)

media_turmas = round(sum(turmas)/qtd_turmas)

print(f"Média de alunos por turma: {media_turmas:.0f}")



