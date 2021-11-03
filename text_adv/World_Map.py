import random
import enemies
import Characters
import items


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch
        on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """


class BoringTile(MapTile):
    def intro_text(self):
        return """
        This is very boring part of the cave
        """


class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You see a bright light...
        it seems to grow as you get closer! It's sunlight!
        
        
        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True


class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return"""
            Another unremarkable part of the cave.
            You must forge onward.
            """
        else:
            return"""
            Someone dropped some gold. You pick it up.
            """


class TraderTile(MapTile):
    def intro_text(self):
        return """
        A Frail not-quite-human, not-quite-creature squats in
        the corner
        clinking his gold coins together. He looks willing to 
        trade.
        """

    def __init__(self,x,y):
        self.trader = Characters.Trader()
        super().__init__(x, y)

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid Choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade Complete!")

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['q', 'Q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer = player, seller = self.trader)
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")


"""
class LockedRoom(MapTile):
    def __init__(self, x, y):
        self.Unlocked = False
        super().__init__(x, y)


    def modify_player(self, player):
        if not self.Unlocked:
            if items.Key() in player.inventory:
                self.Unlocked = True
            else:
                self.x - 1


    def intro_text(self):
        if self.Unlocked == True:
            return"
            The old rusty cave door opens and you see a glimer of light ahead.
            "
        else:
            return"
            You dont have access to this way yet! 
            You will need to find a key first.
            
            You have been sent back a room.
            "
                   
"""     


"""
    dsl = (D)oc (S)tring (L)iteral
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("Doc String Literal is invalid")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None


world_dsl = """
|EN|  |VT|FG|FG|
|FG|EN|  |  |FG|
|EN|FG|EN|EN|TT|
|TT|FG|ST|FG|FG|
|FG|  |EN|  |FG|
"""

world_map = []

tile_type_dict = {"VT": VictoryTile,
                  #"EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  #"LR": LockedRoom,
                  "  ": None}