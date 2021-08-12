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
    def __init__(self, mission,level, items_for_sale):
        super().__init__(mission, level)
        self.items = items_for_sale

    def sell_items(self):
        print("I have the following Items for sale")
        for i in self.items:
            print(i)

    def buy_items(self):
        pass


class Instructor:
    pass


class StoryTeller:
    pass


class Random:
    pass
