#temperaturas, mais alta, mais baixa e média de todas as temperaturas.
while True:
    i = 0
    temperaturas = []
    maior_temperatura = 0
    pos_maior = 0
    menor_temperatura = 0
    pos_menor = 0 

    while True:
        permission_adc = "S"
        i+=1
        temperaturas.append(float(input(f"{i}ª Temperatura: ")))
        permission_adc = input("Registrar mais uma temperatura (S:(Sim) / N:(Não)?: ").upper()
        if permission_adc == "N": break
               
    menor_temperatura = min(temperaturas)
    pos_menor = temperaturas.index(menor_temperatura)
    maior_temperatura = max(temperaturas)
    pos_maior = temperaturas.index(maior_temperatura)
        
    print(f"- Menor temperatura: {menor_temperatura}ºC, na {pos_menor}ª posição.")
    print(f"- Maior temperatura: {maior_temperatura}ºC, na {pos_maior}ª posição.")
    print(f"- Temperatura média: {sum(temperaturas)/len(temperaturas):.1f}")
    permission_process = input("Realizar o processo novamente (S:(Sim) / N:(Não)?: ").upper()
    if permission_process ==  'N': break



    




    


    

    




