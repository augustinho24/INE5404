import sys
import random
import traceback
import Cards
#SAdadasdsa
gLogEnabled = False 
gNumPlayers = 0
gPlayers = []
gBoard = []

def Log(someLog):
    if gLogEnabled:
        print(someLog)

def GetPlayingPlayersFromUser():
    global gNumPlayers
    global gPlayers

    i = 1
    while True:
        pName = input("Por favor, digite o nome do jogador (deixe vazio para continuar): ")
        if not pName:
            break
        gPlayers.append(Cards.Player(i, pName, GetNumRandomCardFromCurrentDeck(2)))
        i += 1

    if len(gPlayers) < 2:
        print("Pelo menos 2 jogadores são necessários.")
        gPlayers = []  
        GetPlayingPlayersFromUser() 

    gNumPlayers = i

def GetNumRandomCardFromCurrentDeck(num):
    cards = []
    for i in range(1,num+1):
        cards.append(GetOneCardFromCurrentDeck())
    return cards

def GetOneCardFromCurrentDeck():
    cardsLeft = len(gCurrentDeck)

    idx = random.randint(0,cardsLeft)
    try:
        card = gCurrentDeck[idx]
    except IndexError as e:
        print("Tamanho do baralho: " + str(len(gCurrentDeck)))
        sys.exit(0)

    del gCurrentDeck[idx]
    return card

def Init():
    global gCurrentDeck

    gCurrentDeck = Cards.GetNewDeck()
    GetPlayingPlayersFromUser()
    PrintPlayersWithCards()

def PrintPlayersWithCards():
    for eachPlayer in gPlayers:
        print("{0} tem {1}{2} {3}{4}".format(eachPlayer.name,
            Cards.GetCardNameString(eachPlayer.cards[0].value), eachPlayer.cards[0].suite,
            Cards.GetCardNameString(eachPlayer.cards[1].value), eachPlayer.cards[1].suite)
            )

def GetListOfJustCards(someList):
    newList = []
    for eachItem in someList:
        newList.append("{0}{1}".format(Cards.GetCardNameString(eachItem.value), eachItem.suite))
    return newList

def DealFlop():
    global gBoard
    gBoard = GetNumRandomCardFromCurrentDeck(3)

def DealTurn():
    gBoard.append(GetOneCardFromCurrentDeck())

def DealRiver():
    gBoard.append(GetOneCardFromCurrentDeck())

def Play():
    DealFlop()
    DealTurn()
    DealRiver()

    print("\nCartas da mesa: " + " ".join(GetListOfJustCards(gBoard)))

    print("\nMelhores mãos:")

    for eachPlayer in gPlayers:
        Cards.PrintBestHandOfPlayer(eachPlayer, gBoard)

def Rank():
    print("----------------------------")
    print("-----------RANKING----------")
    print("----------------------------")

    gPlayers.sort(key=lambda x: x.points, reverse=True)
    i = 1
    for eachPlayer in gPlayers:
        print("{0}. {1}".format(i, eachPlayer.name))
        i+=1

def main():
    Init()
    Play()
    Rank()

if __name__ == '__main__':
    try:
        main()
    except:
        print(traceback.print_exc())
