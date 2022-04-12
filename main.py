import war
import sys


def main():
    if len(sys.argv) == 2:
        GAMES_PLAYED = int(sys.argv[1])
    else:
        GAMES_PLAYED = 10000

    wars = []
    turns = []

    for i in range(GAMES_PLAYED):
        war.play_game(turns, wars)

    war.results(turns, wars, GAMES_PLAYED)


if __name__ == "__main__":
    main()
