import war


def main():
    GAMES_PLAYED = 10000

    wars = []
    turns = []

    for i in range(GAMES_PLAYED):
        war.play_game(turns, wars)

    war.results(turns, wars, GAMES_PLAYED)


if __name__ == "__main__":
    main()
