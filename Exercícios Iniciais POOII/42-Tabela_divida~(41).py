
valor_inicial_divida = float(input())
porcentagem_juros = 0

print("VALOR DA DÍVIDA /// VALOR DOS JUROS /// QUANTIDADE DE PARCELAS /// VALOR DA PARCELA")
for i in range(0,15,3):

    try: 
        porcentagem_juros += 5
        valor_juros = valor_inicial_divida * (porcentagem_juros/100)
        valor_parcela = ((valor_inicial_divida + valor_juros)/(i))
    except ZeroDivisionError:
        valor_parcela = ((valor_inicial_divida + valor_juros)/(i+1))
    if i == 0:
        print(f"R$ {valor_inicial_divida:.2f} /// 0 /// 1x /// R$ {valor_inicial_divida:.2f}")
    else:
        print(f"R$ {(valor_inicial_divida + valor_juros):.2f} /// {valor_juros:.0f} /// {i}x /// R$ {valor_parcela:.2f}")




    
