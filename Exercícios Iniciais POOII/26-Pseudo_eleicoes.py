n = int(input("Número de eleitores: "))

candidatos = {'kid_bengala': 0, 'mr_catra': 0,'ay_Caramba':0}

for i in range (n):
    print("="*30)
    print("NÚMEROS DOS RESPECTIVOS ELEITORES")
    print("Kid Bengala: 33 // Mr.Catra: 69 // Ay Caramba: 99")
    print("="*30)
    voto = int(input(f"Voto do {i+1}º eleitor: "))
    if voto == 33:
        candidatos["kid_bengala"] +=1
    elif voto == 69:
        candidatos['mr_catra'] += 1
    elif voto == 99:
        candidatos['ay_Caramba'] += 1
    else:
        print("Voto inválido")

print("="*30)
print("APURAÇÃO DOS VOTOS")
print(f"Kid Bengala: {candidatos['kid_bengala']}")
print(f"Mr.Catra: {candidatos['mr_catra']}")
print(f"Ay Caramba: {candidatos['ay_Caramba']}")
print("="*30)

if candidatos['kid_bengala'] > candidatos['mr_catra'] and candidatos['kid_bengala'] > candidatos['ay_Caramba']:
    print("Kid Bengala é o novo presidente do Brasil")
elif candidatos['mr_catra'] > candidatos['kid_bengala'] and candidatos['mr_catra'] > candidatos['ay_Caramba']:
    print("Mr.Catra é o novo presidente do Brasil")
elif candidatos['ay_Caramba'] > candidatos['kid_bengala'] and candidatos['ay_Caramba'] > candidatos['mr_catra']:
    print("Ay Caramba é o novo presidente do Brasil.")
else:
    print("Houve empate entre os candidatos. A votação será realizada novamente no Dia de São Nunca.")



