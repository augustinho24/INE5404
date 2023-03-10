n1,n2 = [int(x) for x in input().split()]
soma = 0
if n1 > n2:
    n1,n2 = n2,n1

for i in range(n1+1, n2):
    print(i, end=' ')
    soma += i
print()
print(f"Soma: {soma}")
