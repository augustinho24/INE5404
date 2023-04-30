alunos = {}
alunos_media_7= []

for i in range (10):
    nome = input()
    notas  = [float(x) for x in input().split()]
    alunos[nome] = sum(notas)/4

for u,v in alunos.items():
    if v >= 7:
        alunos_media_7.append(u)
    
print("Alunos com média maior ou igual 7: ",*alunos_media_7)






