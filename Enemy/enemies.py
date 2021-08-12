class Enemy():
    def __init__(self, strength, level, health, weakness, resistance):
        self.strength = strength
        self.level = level
        self.health = health
        self.weakness = weakness
        self.resistance = resistance

    def take_damage(self, weapon, hit):
        if self.weakness in str(weapon):
            damage = hit + 5
        elif self.resistance in str(weapon):
            damage = hit - 5
        else:
            damage = hit
        self.health = self.health - damage
        if self.health > 0:
            print(f"You did {damage} damage. Your enemy is now at {self.health} health.")
        else:
            print(f"You have defeated the Enemy")


class Werewolf(Enemy):
    def __init__(self, strength, level, health):
        self.weakness = "Silver"
        self.resistance = "Iron"
        super().__init__(strength, level, health, self.weakness, self.resistance)


class Ogre(Enemy):
    def __init__(self, strength, level, health):
        self.weakness = "Iron"
        self.resistance = "Gold"
        super().__init__(strength, level, health, self.weakness, self.resistance)


class Dragon(Enemy):
    def __init__(self, strength, level, health):
        self.weakness = "Gold"
        self.resistance = "Silver"
        super().__init__(strength, level, health, self.weakness, self.resistance)


class Troll(Enemy):
    def __init__(self, strength, level, health):
        self.weakness = "Fire"
        self.resistance = "Water"
        super().__init__(strength, level, health, self.weakness, self.resistance)

