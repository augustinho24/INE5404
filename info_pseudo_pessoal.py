nome = input()
while len(nome) <= 3:
    nome = input("Quantidade da caracteres inválidos, digite novamente: ")

idade = int(input())
while idade < 0 or idade > 150:
    idade = int(input("Inválido, digite novamente: "))

sexo = input(str()).lower()
while sexo != 'f' and sexo != 'm':
    sexo = input("Inválido, digite novamente: ")

estd_civil = input().lower()
while not (estd_civil == 's') or (estd_civil == 'c') or (estd_civil == 'v') or (estd_civil == 'd'):
    estd_civil = input("Inválido, digite novamente: ")


 


