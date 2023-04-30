numeros = [int(x) for x in input().split()]

while not len(numeros) == 5:
    print("Digite 5 números!")
    numeros = [int(x) for x in input().split()]

#multiplicação
tot_mult = 0
for i in range(1,5):
    tot_mult += numeros[i-1]*numeros[i]

print("Multiplicação: ",tot_mult)
print("Soma: ",sum(numeros))

