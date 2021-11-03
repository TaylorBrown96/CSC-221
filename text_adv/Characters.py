import items


class NPC():
    def __init__(self):
        raise NotImplementedError("Do not create raw Non Playable Character objects.")

    def __str__(self):
        return self.name


class Trader(NPC):
    def __init__(self):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [items.MoldyBread(),
                          items.MoldyBread(),
                          items.MoldyBread(),
                          items.HealingPotion(),
                          items.HealingPotion()]