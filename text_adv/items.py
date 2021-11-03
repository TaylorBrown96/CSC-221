

class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist sized rock, might be good against an enemy."
        self.damage = 5
        self.value = 1


class Dagger(Weapon):
    def __init__(self):
        self.name = "Used Dagger"
        self.description = "A small dagger with some rust. " \
                           "it's Somewhat more dangerous than a rock."
        self.damage = 10
        self.value = 15


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing its age," \
                           " but it still has some fight in it. "
        self.damage = 20
        self.value = 50


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class MoldyBread(Consumable):
    def __init__(self):
        self.name = "Moldy Bread"
        self.healing_value = 10
        self.value = 20


class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60


class PuzzlePiece:
    def __init__(self):
        raise NotImplementedError("Do not create raw Puzzle Piece objects.")

    def __str__(self):
        return "{}".format(self.name)


class Key(PuzzlePiece):
    def __init__(self):
        self.name = "Key"
        self.value = 10
