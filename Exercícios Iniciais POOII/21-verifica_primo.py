def verifica_primo (x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False

            return True

n = int(input("Digite um número: "))
print(verifica_primo(n))