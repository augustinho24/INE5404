usuario = input()
senha = input()

while usuario == senha:
    senha = input("Inválido, a senha não pode ser igual ao seu nome de usuário, seu mentecapto: ")

print("ok, você não é um mentecapto.")