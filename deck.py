import random


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def __str__(self):
        result = ""
        for card in self.cards:
            result += card
        return result

    def build(self):
        # In this deck an Ace is worh more than the other cards
        # so it will take the value 15. There is no card with value 1.
        for suit in ["s", "c", "d", "h"]:
            for value in range(2, 15):
                self.cards.append(Card(suit, value))

    def shuffle_deck(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def remove_top_card(self):
        return self.cards.pop()


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __str__(self):
        return "{}{}, ".format(self.value, self.suit)
