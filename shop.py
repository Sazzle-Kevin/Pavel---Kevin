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
        self.items = {"Kleiner Heiltrank": 1}

    def new_items(self):
        for _ in range(3):
            chosen = random.choice(items.shop_items)
            self.items[chosen.name] = self.items.get(chosen.name, 0) + 1

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
                inventory.add_item(inp)
                if self.items[inp] > 1:
                    self.items[inp] -= 1
                else:
                    self.items.pop(inp)
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
                print(inventory)

            inp = input().title()
            clear_screen()
            if inp == "V":
                slow_print("Verkäufer", random.choice(random_faces), resume="")
                time.sleep(1)
                return inventory

            if inp in inventory.inventory:
                slow_print(
                    "Verkäufer",
                    "Hier sind ihre 0 Dino Nuggets (Wir haben noch kein Geld^^)",
                )
                inventory.remove_item(inp)

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
