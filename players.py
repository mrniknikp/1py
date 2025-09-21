from game_model import *

#GLOBAL CONST
HP = 100
ARMOR = 1
ID = 0
ATTACK = 13

player1 = Player(1, "name1", HP+10, 1.3, ATTACK+10)
player2 = Player(2, "name2", HP, ARMOR+0.4, ATTACK)
player3 = Player(3, "name3", HP, 0.7, ATTACK + 12)
player4 = Player(4, "name4", HP, 1.1, 20)
player5 = Player(5)

players = {player1, player2, player3, player4, player5}