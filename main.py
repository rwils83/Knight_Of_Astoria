from Enemy import enemies as e
from Items import items as i
from NPC import npc as n
from Missions import missions as m
from gameplay import menus as menus
from gameplay import gameactions as g


class Player():
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.missions_passed = ["0"]
        self.inventory = {"Armor":{}, "Weapon":{}, "Spells":{}}

    def add_to_inventory(self, item_to_add, type, stats):
        self.inventory[type] = {item_to_add:stats}

    def remove_from_inventory(self, item_to_remove, type):
        pass

    def _mission_passed(self, mission):
        self.missions_passed.append(mission)

    def get_inventory(self):
        for items in self.inventory.keys():
            print(self.inventory[items])


def get_player_name():
    name = input("Please tell me your name\r\n")
    return name


def get_player_class():
    player_class = input("Which class you wanna be\r\n") #Figure out a better way to ask this
    return player_class


if __name__ == "__main__":
    intro_menu = menus.MainMenu()
    gamemenu = intro_menu.create_menu()
    gamestart = intro_menu.get_menu_selection()
    while gamestart == "loop":
        gamestart = intro_menu.get_menu_selection()
    player = Player(gamestart.player.name, gamestart.player.player_class)
    if player.name == "Jumpstart":
        player._mission_passed("Intro_Mission")
    if player.missions_passed[-1] == "0":
        current_mission = m.Mission("Intro_Mission")
        current_mission._get_story()
        player.missions_passed.append("Intro_Mission")
    else:
        current_mission = m.Mission("Main_Mission_1")
        current_mission._get_story()
