################################################################################
#                                    ITEMS                                     #
################################################################################


class Items:

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value


class Potion(Items):

    def __init__(self, name: str, value: int, heal: int):
        super().__init__(name, value)
        self.heal = heal

        potions[self.name] = self


class Weapon(Items):

    def __init__(self, name: str, value: int, damage: int):
        super().__init__(name, value)
        self.damage = damage

        weapons[self.name] = self


################################################################################
#                                   USABLES                                    #
################################################################################

potions = {}
weapons = {}


# # # # # # # # # # # # # # # # Potions # # # # # # # # # # # # # # # #
small_potion = Potion("Kleiner Heiltrank", 5, 30)
big_potion = Potion("Großer Heiltrank", 10, 60)


# # # # # # # # # # # # # # # # Weapons # # # # # # # # # # # # # # # #
wood_axe = Weapon("Holzaxt", 20, 7)
wood_sword = Weapon("Holzschwert", 20, 7)
super_boom = Weapon("Superboom", 1001, float("inf"))
