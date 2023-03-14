#Calcular juros de cada parcela

valor_inicial_divida = float(input())
porcentagem_juros = 0


print("VALOR DA DÍVIDA /// VALOR DOS JUROS /// QUANTIDADE DE PARCELAS /// VALOR DA PARCELA")
for i in range(12):
    porcentagem_juros += 5
    valor_juros = valor_inicial_divida * (porcentagem_juros/100)
    valor_parcela = ((valor_inicial_divida + valor_juros)/(i+1))
    if i == 0:
        print(f"R$ {valor_inicial_divida} /// 0.00 /// {i+1}x /// {valor_inicial_divida}")
    else:
        print(f"R$ {valor_inicial_divida} /// {valor_juros} /// {i+1}x /// {valor_parcela:.2f}")




    
