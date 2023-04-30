consoantes = 0

vetor = input().replace(" ","").lower()
consoantes_vetor = []

while not len(vetor) == 10:
    vetor = input("CU: ").replace(" ","").lower()

for i in range(len(vetor)):
    if vetor[i] in ("bcdfgjklmnpqrstvwxz"):
        consoantes_vetor.append(vetor[i])

print("Quantidade de consoantes: ",len(consoantes_vetor))
print("Consoantes: ", *consoantes_vetor)


