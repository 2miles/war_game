from deck import Deck
import random

turn_count = 0
war_count = 0
game_over = False


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
            print(card, end="")
        print()

    def remove_top_card(self):
        return self.cards.pop()

    def add_card_to_bottom(self, card):
        self.cards.insert(0, card)
        pass

    def add_cards_to_bottom(cardList):
        pass


def dealCards(p1, p2, deck):
    deck.shuffle()
    while len(deck.cards) > 0:
        p1.hand.append(deck.remove_top_card())
        if len(deck.cards) > 0:
            p2.hand.append(deck.remove_top_card())


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

    print(f"Battle Cards:\n{p1.battle_card} vs  {p2.battle_card}")
    print("Cards on table: ")
    for c in table_cards:
        print(c, end="")
    print()
    p1.showHand()
    p2.showHand()

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
        shuffle_card_list(table_cards)
        for c in table_cards:
            p2.hand.insert(0, c)
        table_cards.clear()
    else:
        shuffle_card_list(table_cards)
        for c in table_cards:
            p1.hand.insert(0, c)
        table_cards.clear()


def shuffle_card_list(list):
    for i in range(len(list) - 1, 0, -1):
        r = random.randint(0, i)
        list[i], list[r] = list[r], list[i]


def play_game(p1, p2):
    table_cards = []
    dealCards(p1, p2, deck)
    while game_over != True:
        print(f"\n***** turn {turn_count} *****")
        gameTurn(p1, p2, table_cards)
    print(f"War count: {war_count}")


p1 = Player("Player 1")
p2 = Player("Player 2")
deck = Deck()
play_game(p1, p2)
