import random

turn_count = 0
war_count = 0
game_over = False


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Sp", "Cl", "Di", "He"]:
            for v in range(2, 15):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        return self.cards.pop()


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        self.isBattleCard = False

    def __str__(self):
        return "{}-{}, ".format(self.value, self.suit)

    def show(self):
        print("{}-{}, ".format(self.value, self.suit), end="")


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.battle_card = None

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def showHand(self):
        print("{} has {} cards: ".format(self.name, len(self.hand)))
        i = 0
        for card in self.hand:
            i += 1
            if i % 10 == 0:
                print()
            card.show()
        print()


def dealCards(p1, p2, deck):
    deck.shuffle()
    while len(deck.cards) > 0:
        p1.hand.append(deck.draw_card())
        if len(deck.cards) > 0:
            p2.hand.append(deck.draw_card())


def gameTurn(p1, p2, table_cards):

    global turn_count
    global war_count
    global game_over
    turn_count += 1
    if len(p1.hand) < 1 or len(p2.hand) < 1:
        game_over = True
        return
    # take out of hand and call it a battle card
    p1.battle_card = p1.hand.pop()
    p2.battle_card = p2.hand.pop()
    # put battle card on the table
    table_cards.append(p1.battle_card)
    table_cards.append(p2.battle_card)
    print(f"{p1.battle_card} vs {p2.battle_card}")
    for c in table_cards:
        print(c)
    card1 = p1.battle_card.value
    card2 = p2.battle_card.value

    # go to war
    if card1 == card2:
        war_count += 1
        if len(p1.hand) < 4 or len(p2.hand) < 4:
            game_over = True
            return
        table_cards.append(p1.hand.pop())
        table_cards.append(p1.hand.pop())
        table_cards.append(p1.hand.pop())

        table_cards.append(p2.hand.pop())
        table_cards.append(p2.hand.pop())
        table_cards.append(p2.hand.pop())

    elif card1 < card2:
        for c in table_cards:
            p2.hand.insert(0, c)
        table_cards.clear()
    else:
        for c in table_cards:
            p1.hand.insert(0, c)
        table_cards.clear()


def play_game(p1, p2, table_cards):
    dealCards(p1, p2, deck)
    p1.showHand()
    p2.showHand()
    while game_over != True:
        print(f"\n***** turn {turn_count} *****")
        gameTurn(p1, p2, table_cards)
        p1.showHand()
        p2.showHand()
    print(f"War count: {war_count}")


table_cards = []
p1 = Player("Player 1")
p2 = Player("Player 2")
deck = Deck()
play_game(p1, p2, table_cards)
