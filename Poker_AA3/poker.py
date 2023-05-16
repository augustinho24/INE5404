

#naipes = ['Espadas', 'Copas', 'Ouros', 'Paus']
#cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

naipes = ['E', 'C', 'O', 'P']
cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'D', 'J', 'Q', 'K']

rank = {'Straight Flush': 9, 'Quadra': 8, 'Full House': 7, 'Flush': 6, 'Sequencia': 5, 'Trinca': 4, 'Dois Pares': 3, 'Um Par': 2, 'Carta Alta': 1}

class Carta:
    def __init__(self, naipe, carta):
        self.naipe = naipe
        self.carta = carta

class Jogador:
    def __init__(self, nome, mao, pontos):
        self.nome = nome
        self.mao = mao
        self.pontos = pontos


            



def GetNovoBaralho():
    baralho = [Carta(valor, naipe) for valor in cartas for naipe in naipes]
    


