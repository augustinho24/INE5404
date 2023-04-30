vetor = [int(x) for x in input().split()]
while len(vetor) != 10:
    print("Insira novamente: ")
    vetor = [int(x) for x in input().split()]

soma_quadrados = 0

for i in range(len(vetor)):
    soma_quadrados += vetor[i]**2

print("Soma dos quadrados:", soma_quadrados)



