from game_model import *

from players import *

for player in players:
    print(f"{player}")
    player.clear_history()


player1.battle_vs_more(player2, player3, player4, player5)

print('End of programm')
