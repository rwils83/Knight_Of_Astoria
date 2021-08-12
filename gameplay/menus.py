import json
from gameplay import gameactions as g
from gameplay.player import Player, get_player_name, get_player_class

class Menu():
    def __init__(self, text):
        self.text = text

    def create_menu(self):
        return self.text

    def get_menu_selection(self):
        selection = input("")
        return selection


class ArmoryMenu(Menu):
    """
    Sells Weapons and Armor
    """
    def __init__(self):
        self.text = """
This is the Armory
"""
        super().__init__(self.text)

    def return_menu(self):
        selection = self.get_menu_selection()
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

class GeneralShopMenu(Menu):
    """
    Sells food (Regenerate Health) and potions for Health
    """
    def __init__(self):
        self.type = "General Shop"
        self.text = """
This is the General Store
        """
        super().__init__(self.text)

    def return_menu(self):
        selection = self.get_menu_selection()
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

class ApothecaryMenu(Menu):
    """
    Sells Spells, ingredients for spells, potions for regenerating and increasing magic
    """
    def __init__(self):
        self.text = """
This is the Apothecary
        """

        super().__init__(self.text)

    def return_menu(self):
        selection = self.get_menu_selection()
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

    def return_menu(self):
        selection = self.get_menu_selection()
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