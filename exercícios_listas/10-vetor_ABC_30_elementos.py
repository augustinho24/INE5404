vet_A = []
vet_B = []
vet_C = []
vet_ABC = []

elementos_A = input().split()
while len(elementos_A) != 10:
    print("Insira novamente: ")
    elementos_A = [input().split()]

elementos_B = input().split()
while len(elementos_B) != 10:
    print("Insira novamente: ")
    elementos_B = [input().split()]

elementos_C = input().split()
while len(elementos_C) != 10:
    print("Insira novamente: ")
    elementos_C = [input().split()]

for i in range(10):
    vet_ABC.append(elementos_A[i])
    vet_ABC.append(elementos_B[i])
    vet_ABC.append(elementos_C[i])

print("Vetor ABC:", *vet_ABC, sep=" ")
