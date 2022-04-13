## War (card game) Analyser
Simulates 10,000 games of war and collects data based on the games ran. The output of the program includes the average, longest, and shortest games. As well as the average, least, and most wars in a game.

## Example Output:
```console
Out of 100000 games played:
--------------------------------------------------
- Average game: 250 turns
- Longest game: 2238 turns
- Shortest game: 12 turns
- Average wars in a game: 14 wars
- Most wars in a game: 127 wars
- Least wars in a game: 0 wars
```

---
## Running the script
`python war.py [number-of-games]`
- If `number-of-games` is left blank the default is 10,000 games
- To display the result of each turn set `DEBUG = True` in `war.py`

---
## Example verbose display for an individual game turn
- If running in `DEBUG = True` mode run only a few games at most, as it will produce a lot of output for each game.
```console
**************** turn 91   ****************
*******************************************
BATTLE CARDS (p1 vs p2):
------------------------------------------
8c,  vs  7s, 

CARDS ON TABLE: 
------------------------------------------
4s, 4h, 12s, 11c, 7h, 4c, 6h, 12h, 8c, 7s, 

PLAYER 1 DECK (15 cards): 
------------------------------------------
2h, 5s, 14s, 11h, 8s, 9c, 6c, 11d, 13d, 
10c, 13c, 9d, 7c, 6d, 5d, 

PLAYER 2 DECK (27 cards): 
------------------------------------------
2d, 13h, 10h, 8h, 12c, 3c, 3h, 10d, 14c, 
12d, 4d, 2s, 14h, 2c, 11s, 3s, 5c, 9h, 5h, 
6s, 10s, 7d, 13s, 3d, 14d, 8d, 9s, 
```

## Notes
* If the players never shuffle the cards that they win before putting them at the bottom of their deck then there is a decent chance that the game will go on forever. 