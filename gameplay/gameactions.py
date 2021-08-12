import pickle
import os
from pathlib import Path
from gameplay import menus as m


class GameAction():
    def __init__(self, action):
        self.action = action
        self.save_games = ["Empty", "Empty", "Empty", "Empty", "Empty"]
        if Path("Save_1.pkl").exists():
            self.save_games[0] = "Save Game 1"
        if Path("Save_2.pkl").exists():
            self.save_games[1] = "Save Game 2"
        if Path("Save_3.pkl").exists():
            self.save_games[2] = "Save Game 3"
        if Path("Save_4.pkl").exists():
            self.save_games[3] = "Save Game 4"
        if Path("Save_5.pkl").exists():
            self.save_games[4] = "Save Game 5"

    def save_game(self, gamestate):
        print("Which Save Slot to Save Game?")
        selection = input("""
1.
2.
3.
4.
5.\r\n""")
        if selection == "1":
            with open('Save_1.pkl', 'wb') as f:
                pickle.dump(gamestate, f, pickle.HIGHEST_PROTOCOL)
            self.save_games[0] = "Save Game 1"
        elif selection == "2":
            with open('Save_2.pkl', 'wb') as f:
                pickle.dump(gamestate, f, pickle.HIGHEST_PROTOCOL)
            self.save_games[1] = "Save Game 2"
        elif selection == "3":
            with open('Save_3.pkl', 'wb') as f:
                pickle.dump(gamestate, f, pickle.HIGHEST_PROTOCOL)
            self.save_games[2] = "Save Game 3"
        elif selection == "4":
            with open('Save_4.pkl', 'wb') as f:
                pickle.dump(gamestate, f, pickle.HIGHEST_PROTOCOL)
            self.save_games[3] = "Save Game 4"
        elif selection == "5":
            with open('Save_5.pkl', 'wb') as f:
                pickle.dump(gamestate, f, pickle.HIGHEST_PROTOCOL)
            self.save_games[4] = "Save Game 5"
        else:
            return "No Save slot to load"

    def load_game(self):
        check = 0
        for i in self.save_games:
            while i == "Empty" and check < len(self.save_games):
                check += 1
                if check == 5:
                    selection = 0
                    print("No Saved Games")
                    m.MainMenu().create_menu()
                    return None
            else:
                print("Chose Game File to Load")
        # Will allow 5 saved Games
                selection = input(f"""
1. {self.save_games[0]} 
2. {self.save_games[1]}
3. {self.save_games[2]}
4. {self.save_games[3]}
5. {self.save_games[4]}\r\n""")
            if selection == "1":
                with open('Save_1.pkl', 'rb') as f:
                    gameState = pickle.load(f)
            if selection == "2":
                with open('Save_2.pkl', 'rb') as f:
                    gameState = pickle.load(f)
            if selection == "3":
                with open('Save_3.pkl', 'rb') as f:
                    gameState = pickle.load(f)
            if selection == "4":
                with open('Save_4.pkl', 'rb') as f:
                    gameState = pickle.load(f)
            if selection == "5":
                with open('Save_5.pkl', 'rb') as f:
                    gameState = pickle.load(f)
            return gameState

    def delete_saves(self):
        print("Delete which save? You will only be asked once")
        selection = input(f"""
1. {self.save_games[0]} 
2. {self.save_games[1]}
3. {self.save_games[2]}
4. {self.save_games[3]}
5. {self.save_games[4]}
6. Clear all\r\n""")
        if selection == "1":
            os.remove('Save_1.pkl')
        if selection == "2":
            os.remove('Save_2.pkl')
        if selection == "3":
            os.remove('Save_3.pkl')
        if selection == "4":
            os.remove('Save_4.pkl')
        if selection == "5":
            os.remove('Save_5.pkl')
        if selection == "6":
            for i in range(1,6):
                os.remove(f"Save_{i}.pkl")


class GameState():
    def __init__(self, player, inventory, missions_passed, current_location):
        self.player = player
        self.inventory = inventory
        self.missions_passed = missions_passed
        self.current_location = current_location


class NewGame():
    def __init__(self, player):
        self.player = player
