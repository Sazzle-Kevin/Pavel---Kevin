################################################################################
#                                     SHOP                                     #
################################################################################

import random
import items
import time
from text import slow_print, clear_screen

################################################################################
#                                KLASSE: SHOP                                  #
################################################################################


class Shop:

    def __init__(self):
        self.items = {"Kleiner Heiltrank": items.small_potion}

    def new_items(self):
        self.itmes = [random.choice(items.shop_items) for _ in range(3)]

    def kaufen(self, inventory):
        while True:
            clear_screen()
            slow_print(
                "Verkäufer", "Was hätten Sie gerne? V zum verlassen.\n", resume=""
            )

            for item in self.items.keys():
                print(item)

            inp = input().title()
            clear_screen()

            if inp == "V":
                slow_print("Verkäufer", random.choice(random_faces), resume="")
                time.sleep(1)
                return inventory

            if inp in self.items:
                slow_print("Verkäufer", f"1x {inp}? Sehr gerne!")
                inventory.add_item(self.items.pop(inp, None))
            else:
                slow_print(
                    "Verkäufer",
                    f"Leider habe ich gerade das letzte {inp} verkauft.",
                    resume="",
                )

    def verkaufen(self, inventory):
        while True:
            clear_screen()
            slow_print(
                "Verkäufer", "Was möchten Sie verkaufen? V zum Verlassen\n", resume=""
            )

            for item, quantity in inventory.inventory.items():
                print(f"{item.name} x{quantity}")

            inp = input().title()
            clear_screen()
            if inp == "V":
                slow_print("Verkäufer", random.choice(random_faces), resume="")
                time.sleep(1)
                return inventory

            if items.item_dict[inp] and items.item_dict[inp] in inventory.inventory:
                inventory.remove_item()

    def fragen(self):
        slow_print(
            "Verkäufer",
            f"Ich beantworte keine Fragen mehr{random.choice(random_antworten)}",
        )


random_antworten = [
    " seitdem meine Frau laktoseintolerant ist.",
    " seitdem ich hungig bin.",
    " seit Mitte August.",
    " seitdem ich weiß, dass es keine Drachen gibt...",
    " seitdem... seit... Guten Tag junger Abenteurer!\n Wie kann ich behilflich sein?",
    " seitdem Herbert meine Jackpot Bingo Karte gegessen hat.",
    " seitdem Döner mehr als 5 Gold kostet.",
    " seit es gestern regnete.",
    " seit die Antwortsteuer erhöht wurde.",
    ". Aber ich mag Pudding.",
]

random_faces = ["O_O", "-_-", ":)", ":O", "😎", ":(", "Ich mag Brot."]
