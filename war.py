import random


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "hearts"]:
            for v in range(1, 14):
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

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()


class WarGame:
    def __init__(self):
        self.p1 = Player("Player-1")
        self.p2 = Player("Player-2")
        self.deck = Deck()
        self.deck.shuffle()
        self.deal()

    def deal(self):
        while len(self.deck.cards) > 0:
            self.p1.hand.append(self.deck.cards.pop())
            if len(self.deck.cards) > 0:
                self.p2.hand.append(self.deck.cards.pop())

    def print_cards(self):
        print("Player-1 cards: ")
        self.p1.showHand()
        print("\n")
        print("Player-2 cards: ")
        self.p2.showHand()


game = WarGame()
game.print_cards()
