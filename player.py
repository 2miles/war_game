import game


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.battle_card = None

    def draw(self, deck):
        self.hand.append(deck.remove_top_card())
        return self

    def give_cards(self, cards, num):
        # takes num cards from player into cards[]
        for i in range(num):
            cards.append(self.hand.pop())

    def win_cards(self, cards):
        game.shuffle(cards)
        for c in cards:
            self.hand.insert(0, c)
        cards.clear()

    def showHand(self):
        # print(f"{self.name} has {len(self.hand)} cards: ")
        print(f"{self.name.upper()} DECK ({len(self.hand)} cards): ")
        print("------------------------------------------")
        i = 0
        for card in self.hand:
            i += 1
            if i % 10 == 0:
                print()
            print(card, end="")
        print()
        print()
