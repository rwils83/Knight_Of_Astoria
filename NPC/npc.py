class NPC:
    def __init__(self, mission, level):
        self.mission = mission
        self.level = level

    def _has_mission(self):
        if self.mission == True:
            return self.level
        else:
            return False

class Merchant(NPC):
    def __init__(self, mission, level):
        super().__init__(mission, level)

    def sell_items(self):
        pass

    def buy_items(self):
        pass


class Instructor:
    pass


class StoryTeller:
    pass


class Random:
    pass
