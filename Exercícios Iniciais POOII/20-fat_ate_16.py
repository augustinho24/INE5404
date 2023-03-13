def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)

n = int(input("Digite um número: ")) 

while n > 16:
    print("Erro")
    n = int(input("Insira novamente: "))

print(fat(n))
