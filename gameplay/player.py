class Player():
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.missions_passed = ["0"]
        self.inventory = {"Armor": {}, "Weapon": {}, "Spells": {}, "Coins": 0}

    def add_to_inventory(self, item_to_add, type, stats):
        if self.inventory[type] == None:
            self.inventory[type] = {item_to_add:stats}
        else:
            self.inventory[type].update({item_to_add:stats})
    def __remove_from_inventory(self, item_to_remove, type):
        self.inventory[type].pop(item_to_remove)

    def sell_item(self, item_to_remove, type):
        print(f"You are selling {item_to_remove}")
        self.inventory["Coins"] = self.inventory["Coins"]+self.inventory[type][item_to_remove]["Cost"]
        self.__remove_from_inventory(item_to_remove, type)

    def buy_item(self, item_to_add, type, stats):
        print(f"You are buying {item_to_add}")
        self.add_to_inventory(item_to_add, type, stats)
        self.inventory["Coins"] = self.inventory["Coins"] - self.inventory[type][item_to_add]["Cost"]

    def _mission_passed(self, mission):
        self.missions_passed.append(mission)

    def get_inventory(self):
        for items in self.inventory.keys():
            print(f"{items}: {self.inventory[items]}")

    def equip_item(self, type, item_to_equip):
        for i in self.inventory[type].keys():
            if self.inventory[type][i]['Equipped'] == True and self.inventory[type][i] != item_to_equip:
                self.inventory[type][i]['Equipped'] = False
        self.inventory[type][item_to_equip]['Equipped'] = True
def get_player_name():
    name = input("Please tell me your name\r\n")
    return name


def get_player_class():
    player_class = input("Which class you wanna be\r\n") #Figure out a better way to ask this
    return player_class