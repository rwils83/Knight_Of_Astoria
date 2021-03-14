class Item:
    def __init__(self, weight, cost, quality, equipped):
        self.weight = weight
        self.cost = cost
        self.quality = quality
        self.equipped = equipped

    def add(self):
        pass

    def remove(self):
        pass

    def degrade(self):
        pass

    def return_inventory_stats(self):
        return f'Quality: {self.quality} Weight:{self.weight} Cost:{self.cost} Equipped:{self.equipped}'


class Spells(Item):
    def __init__(self, magic_cost, healing, damage, weight, cost, quality, equipped):
        super().__init__(weight, cost, quality, equipped)
        self.magic_cost = magic_cost
        self.healing = healing
        self.damage = damage


class Armor(Item):
    def __init__(self, protection, weight, cost, quality, equipped):
        self.protection = protection
        super().__init__(weight, cost, quality, equipped)

    def return_stats(self):
        return f'{self.return_inventory_stats()} Protection:{self.protection}'


class Weapon(Item):
    def __init__(self, damage, weight, cost, quality, equipped):
        self.damage = damage
        super().__init__(weight, cost, quality, equipped)
