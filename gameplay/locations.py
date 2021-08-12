from gameplay import menus as m
from NPC import npc as n
from Items import items as i

class Store():
    def __init__(self,type):
        self.menu = ""
        self.npc = ""
        pass


class GeneralStore(Store):
    def __init__(self):
        self.type = "General Store"
        super().__init__(self.type)

    def print_menu(self):
        menu = m.GeneralShopMenu().create_menu()
        print(menu)


class Armory(Store):
    def __init__(self):
        self.type = "Armory"
        self.clerk = self._generate_clerk()
        super().__init__(self.type)

    def print_menu(self):
        menu = m.ArmoryMenu().create_menu()
        print(menu)

    def _generate_clerk(self):
        items = {"Silver Sword":i.Weapon(10, 4, 10, 2, True, "Silver Sword"),"Leather Armor":i.Armor(10, 4, 10, 2, True, 'Leather Armor')}
        clerk = n.Merchant(False, 1, items)
        return clerk


class Apothecary(Store):
    def __init__(self):
        self.type = "Apothecary"
        super().__init__(self.type)

    def print_menu(self):
        menu = m.ApothecaryMenu().create_menu()
        print(menu)


class Town():
    def __init__(self):
        self.general = GeneralStore()
        self.apothecary = Apothecary()
        self.armory = Armory()