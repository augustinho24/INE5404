#SUITES = ['Heart', 'Diamond', 'Spade', 'Club']
#CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

SUITES = ['H', 'D', 'S', 'C']
CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

RANKS = {
        'StraightFlush': 80,
        'Quads': 70,
        'FullHouse': 60,
        'Flush': 50,
        'Straight': 40,
        'Set': 30,
        'TwoPairs': 20,
        'Pair': 10,
        'High': 0
        }

class Card:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite

class Player:
    def __init__(self, id, name, cards, points = 0):
        self.id = id
        self.name = name
        self.cards = cards
        self.points = points

def GetNewDeck():
    deck = [Card(value, suite) for value in CARDS for suite in SUITES]
    return deck

def GetListOfCardValues(cards):
    cardValues = []
    for eachCard in cards:
        cardValues.append(int(eachCard.value))
    return cardValues

def GetHighestNumberFromListOfCards(cardValues):
    return max(cardValues)

def IsCardAce(cardValue):
    if cardValue == 14 or cardValue == 1:
        return True
    return False

def IsStraightFlushPossible(cards):
    if IsStraightPossible(cards)[0] and IsFlushPossible(cards)[0]:
        ls1 = []
        ls2 = []
        for eachCard in cards:
            ls1.append(str(eachCard.value) + eachCard.suite)

        for eachCard in ls1:
            if eachCard[-1] == 'H':
                uniqueNum = int(eachCard[:-1]) + 0
                ls2.append(uniqueNum)
                if IsCardAce(eachCard[:-1]):
                    ls2.append(1 + 0)
            elif eachCard[-1] == 'D':
                uniqueNum = int(eachCard[:-1]) + 13
                ls2.append(uniqueNum)
                if IsCardAce(eachCard[:-1]):
                    ls2.append(1 + 13)
            elif eachCard[-1] == 'S':
                uniqueNum = int(eachCard[:-1]) + 26
                ls2.append(uniqueNum)
                if IsCardAce(eachCard[:-1]):
                    ls2.append(1 + 26)
            else:
                uniqueNum = int(eachCard[:-1]) + 39
                ls2.append(uniqueNum)
                if IsCardAce(eachCard[:-1]):
                    ls2.append(1 + 39)

        ls2.sort(reverse=True)

        isPossible, val = IsStraightPossible(ls2, True)
        if isPossible:
            return True, val % 13

    return False, 0

def IsQuadsPossible(cards):
    cardValues = GetListOfCardValues(cards)

    found = False
    num = 1
    for i in range(4):
        sameCount = cardValues.count(cardValues[i])
        if sameCount == 4:
            found = True
            num = cardValues[i]

    if found:
        cardValues.remove(num)
        cardValues.remove(num)
        cardValues.remove(num)
        cardValues.remove(num)
        cardValues.sort(reverse=True)
        return True, [num, GetHighestNumberFromListOfCards(cardValues)]

    return False, 0

def IsFullHousePossible(cards):

    cardValues = GetListOfCardValues(cards)
    cardValues.sort(reverse=True)

    fullHouseCards = []                    

    for i in range(4):
        sameCount = cardValues.count(cardValues[i])
        if sameCount == 3:
            fullHouseCards.append(cardValues[i])
            break

    if len(fullHouseCards) == 1:
        cardValues.remove(fullHouseCards[0])
        cardValues.remove(fullHouseCards[0])
        cardValues.remove(fullHouseCards[0])

        for i in range(3):
            sameCount = cardValues.count(cardValues[i])
            if sameCount == 2:
                fullHouseCards.append(cardValues[i])
                break

    if len(fullHouseCards) == 2:
        return True, fullHouseCards

    return False, 0

def IsFlushPossible(cards):
    cardSuites = [0,0,0,0]                      # H,D,S,C
    HCards = []
    DCards = []
    SCards = []
    CCards = []
    for eachCard in cards:
        if eachCard.suite == 'H':
            cardSuites[0] += 1
            HCards.append(eachCard.value)

        if eachCard.suite == 'D':
            cardSuites[1] += 1
            DCards.append(eachCard.value)

        if eachCard.suite == 'S':
            cardSuites[2] += 1
            SCards.append(eachCard.value)

        if eachCard.suite == 'C':
            cardSuites[3] += 1
            CCards.append(eachCard.value)

    if any(i >= 5 for i in cardSuites):
        if (cardSuites[0] >= 5):
            return True, GetHighestNumberFromListOfCards(HCards)
        elif (cardSuites[1] >= 5):
            return True, GetHighestNumberFromListOfCards(DCards)
        elif (cardSuites[2] >= 5):
            return True, GetHighestNumberFromListOfCards(SCards)
        else:
            return True, GetHighestNumberFromListOfCards(CCards)
    else:
        return False,0

def IsStraightPossible(cards, fromStraightFlush = False):
    cardValues = []
    if not fromStraightFlush:
        cardValues = GetListOfCardValues(cards)
    else:
        cardValues = cards

    if 14 in cardValues:
        cardValues.append(1)
    cardValues = list(set(cardValues))                
    cardValues.sort(reverse=True)

    numCardsLeft = len(cardValues)
    numToIterate = numCardsLeft - 4

    if numCardsLeft > 4:
        for i in range(numToIterate):
            if cardValues[i] - 1 == cardValues[i+1]:
                if cardValues[i+1] - 1 == cardValues[i+2]:
                    if cardValues[i+2] - 1 == cardValues[i+3]:
                        if cardValues[i+3] - 1 == cardValues[i+4]:
                            return True, cardValues[i]

    return False, 0

def IsSetPossible(cards):
    cardValues = GetListOfCardValues(cards)
    cardValues.sort(reverse=True)

    found = False
    num = 1
    for i in range(5):
        sameCount = cardValues.count(cardValues[i])
        if sameCount == 3:
            found = True
            num = cardValues[i]

    if found:
        cardValues.remove(num)
        cardValues.remove(num)
        cardValues.remove(num)

        return True, [num, cardValues[0], cardValues[1]]

    return False, []

def IsPairPossible(cards):
    cardValues = GetListOfCardValues(cards)
    cardValues.sort(reverse=True)

    found = False
    num = 1
    for i in range(6):
        sameCount = cardValues.count(cardValues[i])
        if sameCount == 2:
            found = True
            num = cardValues[i]

    if found:
        cardValues.remove(num)
        cardValues.remove(num)
        return True, [num, cardValues[0], cardValues[1], cardValues[2]]

    return False, []

def IsTwoPairPossible(cards):
    cardValues = GetListOfCardValues(cards)
    cardValues.sort(reverse=True)

    best5Cards = []

    for i in range(6):
        sameCount = cardValues.count(cardValues[i])
        if sameCount == 2:
            best5Cards.append(cardValues[i])
            break

    if len(best5Cards) == 1:
        cardValues.remove(best5Cards[0])
        cardValues.remove(best5Cards[0])
        for i in range(5):
            sameCount = cardValues.count(cardValues[i])
            if sameCount == 2:
                best5Cards.append(cardValues[i])
                break


    if len(best5Cards) == 2:
        cardValues.remove(best5Cards[1])
        cardValues.remove(best5Cards[1])
        best5Cards.append(cardValues[0])

        return True, best5Cards

    return False, 0

def GetHighest5Cards(cards):
    cardValues = GetListOfCardValues(cards)
    cardValues.sort(reverse=True)

    return cardValues[:5]

def GetCardNameString(val):
    if val == 1 or val == 14:
        return "A"
    elif val == 11:
        return "J"
    elif val == 12:
        return "Q"
    elif val == 13:
        return "K"
    else:
        return str(val)

def PrintBestHandOfPlayer(player, boardCards):

    isTrue,val = IsStraightFlushPossible(player.cards + boardCards)
    if isTrue:
        player.points = RANKS["StraightFlush"] + val
        print("{0} tem {1} Straight Flush. Pontos: {2}".format(player.name, GetCardNameString(val), player.points))
        return

    isTrue,val = IsQuadsPossible(player.cards + boardCards)
    if isTrue:
        player.points = RANKS["Quads"] + val[0] + val[1]
        print("{0} tem {1} uma Quadra com Kicker {2}. Pontos: {3}".format(player.name,
            GetCardNameString(val[0]), GetCardNameString(val[1]),
            player.points))
        return

    isTrue,val = IsFullHousePossible(player.cards + boardCards)
    if isTrue:
        player.points = RANKS["FullHouse"] + val[0]*3 + val[1]*2
        print("{0} tem {1} de {2}. Pontos: {3}".format(player.name, GetCardNameString(val[0]), GetCardNameString(val[1]), player.points))
        return

    isTrue,val = IsFlushPossible(player.cards + boardCards)
    if isTrue:
        player.points = RANKS["Flush"] + val
        print("{0} has {1} Flush. Pontos: {2}".format(player.name, GetCardNameString(val), player.points))
        return

    isTrue,val = IsStraightPossible(player.cards + boardCards)
    if isTrue:
        player.points = RANKS["Straight"] + val
        print("{0} tem {1} Sequencia. Pontos: {2}".format(player.name, GetCardNameString(val), player.points))
        return

    isTrue,val = IsSetPossible(player.cards + boardCards)
    if isTrue:
        player.points = RANKS["Set"] + val[0]*3 + val[1] + val[2]
        print("{0} tem uma Trinca de {1} com Kickers {2},{3}. Pontos: {4}".format(player.name,
            GetCardNameString(val[0]), GetCardNameString(val[1]), GetCardNameString(val[2]), 
            player.points))
        return

    isTrue,val = IsTwoPairPossible(player.cards + boardCards)
    if isTrue:
        player.points = RANKS["TwoPairs"] + val[0] + val[1] + val[2]
        print("{0} tem Dois Pares de {1} e {2} com kicker {3}. Pontos: {4}".format(player.name,
            GetCardNameString(val[0]), GetCardNameString(val[1]), GetCardNameString(val[2]),
            player.points))
        return

    isTrue,val = IsPairPossible(player.cards + boardCards)
    if isTrue:
        player.points = RANKS["Pair"] + val[0]*2 + val[1] + val[2] + val[3]
        print("{0} tem um Par de {1}. Pontos: {2}".format(player.name, GetCardNameString(val[0]), player.points))
        return

    val = GetHighest5Cards(player.cards + boardCards)
    player.points = RANKS["High"] + val[0] + val[1] + val[2] + val[3] + val[4]
    print("{0} tem {1} carta alta. Pontos: {2}".format(player.name, GetCardNameString(val[0]), player.points))

