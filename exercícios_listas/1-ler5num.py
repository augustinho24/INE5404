numeros = [int(x) for x in input().split()]

while len(numeros) < 5 or len(numeros) > 5:
    numeros = [int(x) for x in input("CU").split()]
else:
    print(*numeros)

