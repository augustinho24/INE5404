perguntas = ["Telefonou para a vítima?","Esteve no local do crime?", "Mora perto da vítima?" , "Devia para a vítima?", "Já trabalhou com a vítima?"]
respostas = 0

print("Responda as perguntas abaixo com S(sim) ou N(não):")

for u in range(len(perguntas)):
    print(perguntas[u])
    resposta = input().upper()
    while resposta != "S" and resposta != "N":
        resposta = input("Inválido, digite 'S'(sim) ou 'N'(não): ").upper()
    if resposta == "S": respostas += 1
    
if respostas == 2: print("Condição: Suspeita(o)")
elif 3 == respostas <= 4: print("Condição: Cúmplice")
elif respostas == 5: print("Condição: Assassina(o)")
else: print("Condição: Inocente")




           