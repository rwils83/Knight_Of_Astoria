import json
from gameplay import gameactions as g
from main import Player, get_player_name, get_player_class

class Menu():
    def __init__(self, text):
        self.text = text

    def create_menu(self):
        print(self.text)

    def get_menu_selection(self):
        selection = input("")

        if selection == "1":
            newgame = g.GameAction("load").load_game()
        if selection == "2":
            newgame = g.NewGame(Player(get_player_name(), get_player_class()))
        if selection == "3":
            GameInfo().create_menu()
            newgame = None
        if selection == "4":
            print(f"See you next time")
            exit()
        if selection == "5":
            MainMenu().create_menu()
            newgame = None
        if newgame is not None:
            return newgame
        else:
            return "loop"

class Armory(Menu):
    """
    Sells Weapson and Armor
    """
    def __init__(self):
        self.type = "Shop"
        super().__init__(self.type)


class GeneralShop(Menu):
    """
    Sells food (Regenerate Health) and potions for Health
    """
    def __init__(self):
        self.type = "General Shop"
        super().__init__(self.type)


class Apothecary(Menu):
    """
    Sells Spells, ingredients for spells, potions for regenerating and increasing magic
    """
    def __init__(self):

        super().__init__()


class GameMenu(Menu):
    """
    Game menu for save, load, exit during Game
    """
    def __init__(self):
        self.type = "In-Game Menu"
        super().__init__(self.type)


class MainMenu(Menu):
    """
    Main Game menu. Allows Exit from game, Load saved game, Start New Game
    """
    def __init__(self):
        self.text = """
    Game Menu
Would you like to:
1. Load a Game
2. Create a New Game
3. Get Game Information
4. Exit
        """
        super().__init__(self.text)

class GameInfo(Menu):
    """
    Defines Classes and how to play
    """
    def __init__(self):
        self.text = """
Different Player Classes:
Assassin: Enter Description for Assassin Class
Rogue: Enter Description for Rogue Class
Knight: Enter Description for Knight Class
Wizard: Enter Description for Wizard Class
Press 5 to exit        
"""
        super().__init__(self.text)