notas = [float(x) for x in input().split()]

while not len(notas) >= 4:
    notas = [float(x) for x in input("CU: ").split()]

print(f'{(sum(notas)/4):.2f}')