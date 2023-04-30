vet_C = []

elementos_A = input().split()
while len(elementos_A) != 10:
    print("Digite 10 elementos!")
    elementos_A = input().split()

elementos_B = input().split()
while len(elementos_B) != 10:
    print("Digite 10 elementos!")
    elementos_B = input().split()

for i in range(10):
    vet_C.append(elementos_A[i])
    vet_C.append(elementos_B[i])

print("Vetor C:",*vet_C, sep = " ")



