alunos = {}
aluno_mais_alto = ''
aluno_mais_baixo = ''

for i in range(10):
    cod,altura = input("Digite o código e a altura do aluno: ").split()
    alunos[cod] = float(altura)

if aluno_mais_alto == '':
    aluno_mais_alto = cod
elif alunos[aluno_mais_alto] < altura:
    aluno_mais_alto = cod

if aluno_mais_baixo == '':
    aluno_mais_baixo = cod
elif alunos[aluno_mais_baixo] > altura:
    aluno_mais_baixo = cod

print(f"O aluno mais alto é {aluno_mais_alto} com {alunos[aluno_mais_alto]}m")
print(f"O aluno mais baixo é {aluno_mais_baixo} com {alunos[aluno_mais_baixo]}m")


