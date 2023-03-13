# preço por pão = 0.18*q | q(1 -> 50)
print('Preço por unidade de pão: R$ 0.18')
print('Padaria Pão de Ontem - Tabela de Preços:')
for q in range(50): print(f'{q+1} - R$ {(0.18*(q+1)):.2f}')

