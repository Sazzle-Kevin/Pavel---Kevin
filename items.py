################################################################################
#                                    ITEMS                                     #
################################################################################

import inventory

################################################################################
#                                 KLASSE: ITEMS                                #
################################################################################


class Items:

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value


class Potion(Items):

    def __init__(self, name: str, value: int, heal: int, use=True):
        super().__init__(name, value)
        self.heal = heal

        potions[self.name] = self

    def use(self, char, inventory):
        char.heal(self.heal)
        inventory.remove_item(self.name)


class Weapon(Items):

    def __init__(self, name: str, value: int, damage: int, use=True):
        super().__init__(name, value)
        self.damage = damage

        weapons[self.name] = self

    def use(self, char, inventory):
        char.use_weapon(self.damage)
        inventory.remove_item(self.name)


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


################################################################################
#                                  LOOTTABLES                                  #
################################################################################


event_items = [
    small_potion,
    small_potion,
    small_potion,
    small_potion,
    small_potion,
    big_potion,
    big_potion,
    big_potion,
    wood_axe,
    wood_sword,
]

shop_items = [
    small_potion,
    small_potion,
    small_potion,
    small_potion,
    small_potion,
    big_potion,
    big_potion,
    big_potion,
    wood_axe,
    wood_sword,
]

item_dict = {
    "Kleiner Heiltrank": small_potion,
    "Großer Heiltrank": big_potion,
    "Holzaxt": wood_axe,
    "Holzschwert": wood_sword,
}
