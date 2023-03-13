def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)

n = int(input())
resultado = fat(n)

print(f"{n}! = ", end="")
for i in range(n, 0, -1):
    print(i, end="")
    if i > 1: print(" . ", end="")
    else: print(" = ", end="")
print(f"{resultado}")
