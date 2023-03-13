#Pseudo Caixa Registradora:

while True:
    produtos = []
    dinheiro_fornecido_cliente = 0
    total_compra = 0
    troco = 0
    i = 0
    print('='*60)
    print("Lojas Tabajara")
    print('='*40)
    
    while True:
        i+=1
        prod_preco = float(input(f"Produto {i}: R$ "))
        if prod_preco == 0: break
        produtos.append(prod_preco)

    while (len(produtos)) > 0:
        total_compra += sum(produtos)
        print(f"Total: R$ {total_compra:.2f}")
        dinheiro_fornecido_cliente += float(input("Dinheiro: R$ "))
        print(f"Troco: R$ {(dinheiro_fornecido_cliente-total_compra):.2f}")
        produtos.clear()
    pergunta = input("Efetuar outra compra (S:(Sim) / N:(Não))?: ").upper()
    if pergunta == 'N': break 











