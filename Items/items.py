class Item:
    def __init__(self, weight, cost, quality, equipped, name):
        self.weight = weight
        self.cost = cost
        self.quality = quality
        self.equipped = equipped
        self.name = name

    def add(self):
        pass

    def remove(self):
        pass

    def degrade(self):
        pass

    def return_inventory_stats(self):
        return f'{self.name} Stats: Quality: {self.quality} Weight:{self.weight} Cost:{self.cost} Equipped:{self.equipped}'


class Spells(Item):
    def __init__(self, magic_cost, healing, damage, weight, cost, quality, equipped):
        super().__init__(weight, cost, quality, equipped)
        self.magic_cost = magic_cost
        self.healing = healing
        self.damage = damage
        self.type = "Spells"


class Armor(Item):
    def __init__(self, protection, weight, cost, quality, equipped):
        self.protection = protection
        super().__init__(weight, cost, quality, equipped)
        self.type = "Armor"

    def return_stats(self):
        return f'{self.return_inventory_stats()} Protection:{self.protection}'


class Weapon(Item):
    def __init__(self, damage, weight, cost, quality, equipped, name):
        self.damage = damage
        self.type = "Weapon"
        super().__init__(weight, cost, quality, equipped, name)
