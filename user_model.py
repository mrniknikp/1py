#TODO: Сделать систему учетных записей с возможностью привязки различных объектов (player) к одной учетной записи
from game_model import *
from players import *

class User:

    def __init__(self, id, name, players: list[Player] = None):
        """
            Creating User with ID autoincrement (check parser.py)
            Name from username field
            And army list of objects

            
        """
        self.id = id
        self.name = name
        self.player = {}
        i = 0
        for player in players:
            self.player[i] = player
            i=+1

    def __str__(self):
        info_text = ''
        for i in self.player:
            info_text = f"{info_text} {self.player[i].id},"
        return f"| {self.id} | {self.name} | {info_text} |"
    
    def add_player(self, player):
        self.player[len(self.player)] = player

    def player_info(self, id):
        try:
            return f"Юнит с id {id}: {self.player[id]}"
        except:
            return f"Юнит с id {id} не найден"
        
    def all_players(self):
        for p in self.player:
            print(self.player[p])

User1 = User(1, "User One", [player1, player2])

User2 = User(2, "User Two", [player4, player5])

print(User1)

User1.add_player(player3)

print(User1)

print(User2)

print(User2.player_info(0))

print(User2.player_info(4))

User1.all_players()