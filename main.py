from time import *
import os
import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

"""
class PlayerDatabase:
    def __init__(self, db_name = "players.db"):
        self.db_name = db_name
        self.init_db()
    
    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS players (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    hp REAL NOT NULL,
                    armor REAL NOT NULL,
                    attack REAL NOT NULL
                )
            ''')
            cursor.commit()
"""

#==========================CLASS PLAYER========================#


class Player:
    default_hp = 100
    default_armor = 1
    default_attack = 10
    default_name = f"player"
    def __init__(self, id, name = None, hp = None, armor = None, attack = None):
        """Creating player: ID, HP, Armor (from 0 to 2), Attak (from 0 to infinity)"""
        self.id = id
        self.name = name if name is not None else f"{Player.default_name}{id}"
        self.hp = hp if hp is not None else Player.default_hp
        self.armor = armor if hp is not None else Player.default_armor
        self.attack = attack if hp is not None else Player.default_attack

    def is_alive(self):
        return self.hp > 0
    
    def info(self):
        name = f"Name: {self.name}"
        hp = f"HP: {self.hp:.1f}"
        armor = f"Armor: {self.armor:.2f}"
        attack = f"Attack: {self.attack:.2f}"
        return f"\n{name} {hp} {armor} {attack}\n"
    
    def __str__(self):
         return self.info()

    def get_hit(self, damage):
        self.hp -= damage
        if not(self.is_alive()):
            return f"You died\n"
        return f"Your HP {self.hp:.1f}\n"
    
    def damage(self, other):
        return self.attack*(2-other.armor)

    def battle(self, other):
        s_dmg = self.damage(other)
        o_dmg = other.damage(self)
        s_hp = self.hp
        o_hp = other.hp
        self.hp -= o_dmg
        other.hp -= s_dmg
        
        if not self.is_alive() and not other.is_alive():
            if self.hp == other.hp:
                return "Both dead"
            elif self.hp > other.hp:
                self.hp = 1
            else:
                other.hp = 1
        if not self.is_alive():
            return f"Player {other.id} wins with {other.hp:.1f} HP!\nDamage dealed: {s_dmg:.1f}"
        elif not other.is_alive():
            return f"Player {self.id} wins with {self.hp:.1f} HP!\nDamage dealed: {o_dmg:.1f}" 
        else:
            return f"\n{self}\n\n{other}"

    def add_to_history(self, i, result):
        my_file = open(f'history_{self.id}.txt', 'a+')
        my_file.write(f"Result after {i} battles: {result}\n")
        my_file.close()
        return 0
    
    def clear_history(self):
        my_file = open(f'history_{self.id}.txt', 'w+')
        my_file.write(f"Here will be history of player #{self.id}:\n\n")
        my_file.close()
        return 0

    def battle_vs_more(self, *others):
        players = list(others)
        for i in range(len(players)):
            battle_inf(self, players[i])


def battle_inf(*objects):
    players = list(objects)
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            player1 = players[i]
            player2 = players[j]
            if player1 != player2:
                count = 0
                while player1.is_alive() and player2.is_alive():
                    count += 1
                    result = player1.battle(player2)
                    print(f"Result for battle №{count}: {result}")
                    player1.add_to_history(count, result)
                    player2.add_to_history(count, result)

    return 0

def new_player(players):
    id = len(players)
    name = Player(id)
    return name


#==========================GLOBAL CONST AND CREATION OBJECTS========================#


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

#==========================CLASS FIELD========================#


class Field:
    """TODO Сделать карту и пересещение по ней"""
    locations = {"castle", "forest", "wheat_field", "road"}

    def __init__(self):
        return Field.locations
    
    def move(self):
        """TODO Проверка на возможность перемещения и реализация этого перемещения выбором пункта номером из контекстного меню"""
        return 0
    

#==========================CLASS USER========================#


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

#==========================MAIN BODY========================#


User1 = User(1, "User One", [player1, player2])

User2 = User(2, "User Two", [player4, player5])

print(User1)

User1.add_player(player3)

print(User1)

print(User2)

print(User2.player_info(0))

print(User2.player_info(4))

User1.all_players()


#==========================TKINTER FUNCTIONS========================#


def close():
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        root.destroy()

root = tk.Tk()
root.title("Game window")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry(f"{width}x{height}")

frame = tk.Frame(root)
frame.pack(side="bottom")

button = tk.Button(frame, text="Btn1", command=close)
button.pack(side="right")

root.mainloop()
