import json


class Item:
    def __init__(self, weight, cost, quality, equipped, name):
        self.weight = weight
        self.cost = cost
        self.quality = quality
        self.equipped = equipped
        self.name = name

    def return_item_stats(self):
        return f'You found: {self.name} with the following stats: Quality: {self.quality} Weight:{self.weight} Cost:{self.cost} Equipped:{self.equipped}'


class Spells(Item):
    def __init__(self, magic_cost, healing, damage, weight, cost, quality, equipped):
        super().__init__(weight, cost, quality, equipped)
        self.magic_cost = magic_cost
        self.healing = healing
        self.damage = damage
        self.type = "Spells"


class Armor(Item):
    def __init__(self, protection, weight, cost, quality, equipped, name):
        self.protection = protection
        super().__init__(weight, cost, quality, equipped, name)
        self.type = "Armor"

    def return_stats(self):
        return f'{self.return_inventory_stats()} Protection:{self.protection}'


class Weapon(Item):
    def __init__(self, damage, weight, cost, quality, equipped, name):
        self.damage = damage
        self.type = "Weapon"
        super().__init__(weight, cost, quality, equipped, name)


class Book(Item):
    def __init__(self, topic):
        self.topic = topic
        self.topics = {}
        with open("Enemy\enemies_info.json", "r") as f:
            self.topics = json.load(f)

    def learn_info(self):
        if self.topic in self.topics:
            print(f'You learned about {self.topic}. '
                  f'You now know that {self.topic} are resistant to '
                  f'{self.topics[self.topic]["Resistance"]} '
                  f'and their weakness is {self.topics[self.topic]["Weakness"]}')