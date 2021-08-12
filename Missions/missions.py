import json


class Mission():
    def __init__(self, level):
        self.level = level

    def _get_story(self):
        with open(f"missions/{self.level}.txt", "r") as f:
            for line in f.readlines():
                print(line.strip())
        cont = input("Continue? y or n \r\n")
        if cont.lower() == "y":
                print("You successfully continued")
        elif cont.lower() == "n":
            import gameplay.menus as g
            g.MainMenu().create_menu()
            g.MainMenu().get_menu_selection()
