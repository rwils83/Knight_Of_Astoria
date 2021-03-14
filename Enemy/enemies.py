class Enemy():
    def __init__(self, strength, level, health):
        self.strength = strength
        self.level = level
        self.health = health


class Werewolf(Enemy):
    def __init__(self, strength, level, health):
        super().__init__(strength, level, health)


class Ogre(Enemy):
    def __init__(self, strength, level, health):
        super().__init__(strength, level, health)


class Dragon(Enemy):
    def __init__(self, strength, level, health):
        super().__init__(strength, level, health)


class Troll(Enemy):
    def __init__(self, strength, level, health):
        super().__init__(strength, level, health)

