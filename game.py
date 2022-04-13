from deck import Deck
from player import Player
import random

DEBUG = False

turn_count = 0
war_count = 0
game_over = False


def dealCards(p1, p2, deck):
    deck.shuffle_deck()
    while len(deck.cards) > 0:
        p1.draw(deck)
        if len(deck.cards) > 0:
            p2.draw(deck)


def shuffle(list):
    for i in range(len(list) - 1, 0, -1):
        r = random.randint(0, i)
        list[i], list[r] = list[r], list[i]


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

    card1 = p1.battle_card.value
    card2 = p2.battle_card.value
    if DEBUG == True:
        display_turn(p1, p2, table_cards)

    # go to war
    if card1 == card2:
        war_count += 1
        if len(p1.hand) < 3 or len(p2.hand) < 3:
            game_over = True
            return
        p1.give_cards(table_cards, 3)
        p2.give_cards(table_cards, 3)

    elif card1 < card2:
        p2.win_cards(table_cards)
    else:
        p1.win_cards(table_cards)


def display_turn(p1, p2, table_cards):
    print(f"\n**************** turn {turn_count:<4} ****************")
    print("*******************************************")
    print("BATTLE CARDS (p1 vs p2):")
    print("------------------------------------------")
    print(f"{p1.battle_card} vs  {p2.battle_card}\n")

    print("CARDS ON TABLE: ")
    print("------------------------------------------")
    for c in table_cards:
        print(c, end="")
    print()
    print()
    p1.showHand()
    p2.showHand()
    print()
    # print(f"Turn count: {turn_count}")
    # print(f"War count: {war_count}")


def play_game(turns, wars):
    global turn_count
    global war_count
    global game_over
    global DEBUG

    p1 = Player("Player 1")
    p2 = Player("Player 2")
    deck = Deck()
    table_cards = []
    dealCards(p1, p2, deck)
    while game_over != True:
        gameTurn(p1, p2, table_cards)

    turns.append(turn_count)
    wars.append(war_count)

    turn_count = 0
    war_count = 0
    game_over = False


def results(turns_list, war_list, GAMES_PLAYED):

    longest = max(turns_list)
    shortest = min(turns_list)
    most = max(war_list)
    least = min(war_list)
    avg_turns = int(sum(turns_list) / len(turns_list))
    avg_wars = int(sum(war_list) / len(war_list))

    print("\n\n\n\n")
    print(f"Out of {GAMES_PLAYED} games played:")
    print("--------------------------------------------------")
    print(f"- Average game: {avg_turns} turns")
    print(f"- Longest game: {longest} turns")
    print(f"- Shortest game: {shortest} turns")
    print(f"- Average wars in a game: {avg_wars} wars")
    print(f"- Most wars in a game: {most} wars")
    print(f"- Least wars in a game: {least} wars")
    # print(f"- Highest war to turn ratio: {} turns per war")
    # print(f"- Lowest war to turn ratio: {} turns per war")
    # print(f"- Player 1 win ratio: ")
    # print(f"- Player 2 win ratio: ")
    print("\n\n\n\n")
