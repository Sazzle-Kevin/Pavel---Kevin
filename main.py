################################################################################
#                                    MAIN                                      #
################################################################################

import time
import random
import strings
import location
import combat
import items
import enemy
from shop import Shop
from inventory import Inventory
from player import Player
from text import slow_print, clear, clear_screen

################################################################################
#                                     UI                                       #
################################################################################


class UserInterface:

    def __init__(self):
        self.current = "Neutral"

    # # # # # # # # # # # # # # # # Inventory # # # # # # # # # # # # # # # #
    def tasche(self):
        self.tasche_benutzen(player, inventory)

    def tasche_benutzen(self, char, inventory):
        while True:
            clear_screen()
            slow_print(
                "Erzähler", "Welchen Gegenstand willst du benutzen?\n\n", resume=""
            )

            print(inventory, "\n\n")
            print("-- V zum Verlassen --\n\n\n")

            inp = input().title()

            if inp == "V":
                self.current = "Neutral"
                return

            if inp in inventory.inventory:
                items.item_dict[inp].use(char, inventory)
                slow_print("Erzähler", f"{char.name} benutzt {inp}!")
            else:
                print(f"{inp} kann nicht benutzt werden.")

    # # # # # # # # # # # # # # # # Look around # # # # # # # # # # # # # # # #
    def umschauen(self):
        if player.location == location.unlock_cities.head.city:
            slow_print(
                "Erzähler",
                "Der Verkäufer sieht aus, als würde er sich auf einen Kampf vorbereiten...",
            )
        else:
            slow_print("Erzähler", player.location.description)

    # # # # # # # # # # # # # # # # Shop # # # # # # # # # # # # # # # #
    def laden(self):
        self.current = "Laden"

    def kaufen(self):
        global inventory
        inventory = town_shop.kaufen(inventory)

    def verkaufen(self):
        global inventory
        inventory = town_shop.verkaufen(inventory)

    def fragen(self):
        if player.location == location.unlock_cities.head.city:
            slow_print("Verkäufer", "Zeig mir, was du drauf hast!")
            self.kampf(location.spawn_shopkeeper)
            if player.is_alive():
                slow_print(
                    "Verkäufer",
                    f"Ok, ok.. Du hast einiges drauf. Also, die nächste Stadt.. (Er erzählt dir von {location.unlock_cities.head.next.city.name})",
                )
                worldmap.add_city(player.location)
                location.unlock_cities.head = location.unlock_cities.head.next
        else:
            town_shop.fragen()

    def verlassen(self):
        self.current = "Neutral"

    # # # # # # # # # # # # # # # # World Map # # # # # # # # # # # # # # # #
    def karte(self):
        while True:
            slow_print("Erzähler", "Wohin möchtest du reisen?\n", resume="")
            print("Stadt  |  Route\n")
            worldmap.print(player.location)
            inp = input().title()

            if inp == "V":
                self.current = "Neutral"
                return

            for city in worldmap.locations[player.location]:
                if inp == city.name:
                    self.ziel(city)
                    return

    def ziel(self, city):
        self.current = worldmap.locations[player.location][city]
        self.reisen(city)
        self.current = "Neutral"

    # # # # # # # # # # # # # # # # Reisen # # # # # # # # # # # # # # # #

    def reisen(self, city):
        clear_screen()
        route = self.current
        town_shop.new_items()
        slow_print(
            "Erzähler",
            f"{player.name} macht sich auf die Reise. Route: {route.name}.",
        )
        slow_print("Erzähler", f"{route.description}")

        ## Erste Kampfmöglichkeit ##
        slow_print("Erzähler", "Hier ist etwas...")
        clear_screen()
        time.sleep(1)
        if random.randint(1, 10) >= 8:
            slow_print("Erzähler", random.choice(strings.reise_battle), delay=0.03)
            self.kampf(random.choice(route.enemies))
        else:
            slow_print("Erzähler", random.choice(strings.reise_no_battle))

        clear_screen()
        time.sleep(1)
        slow_print("Erzähler", "Weiter gehts!")
        clear_screen()
        time.sleep(1)

        ## Mitte der Reise - Event ##
        slow_print("Erzähler", random.choice(route.events))
        while True:
            print("Möchtest du nachschauen? - ja/j oder nein/n\n\n\n")
            inp = input().lower()
            clear_screen()
            if inp in ["ja", "j"]:
                time.sleep(1)
                slow_print("Erzähler", "Du sammelst deinen Mut...")
                chance = random.randint(1, 10)
                clear_screen()
                time.sleep(1)
                if chance >= 7:
                    loot = random.choice(items.event_items)
                    slow_print("Erzähler", f"Nice! 1x {loot.name} gefunden!")
                    inventory.add_item(loot.name)
                else:
                    slow_print("Erzähler", "Oh nein, ein Überfall!")
                    self.kampf(random.choice(route.enemies))
                break
            elif inp in ["nein", "n"]:
                slow_print("Erzähler", "Du gehst weiter. Eiskalt.")
                break
            else:
                slow_print("Erzähler", f"Falscher Input: {inp}")

        clear_screen()
        time.sleep(1)
        slow_print("Erzähler", "Weiter gehts!")
        time.sleep(1)

        ### Letzte Kampfmöglichkeit ###
        slow_print("Erzähler", "Du spürst etwas...")
        clear_screen()
        time.sleep(1)
        if random.randint(1, 10) >= 8:
            slow_print("Erzähler", random.choice(strings.reise_battle))
            self.kampf(random.choice(route.enemies))
        else:
            slow_print("Erzähler", random.choice(strings.reise_no_battle))
        clear_screen()
        time.sleep(1)

        player.location = city
        if city != location.castle:
            slow_print("Erzähler", "Du hast dein Ziel erreicht!")
            slow_print("", city.name.upper().center(40))
        else:
            slow_print("Erzähler", "Du erreichst das Schloss.")
            slow_print("", city.name.upper().center(40), delay=0.1)
            strings.boss()
            self.kampf(location.spawn_vampire_lord)

            if player.is_alive():
                strings.outro(player)

    # # # # # # # # # # # # # # # # Kampf # # # # # # # # # # # # # # # #

    def kampf(self, enemy):
        enemy = enemy()
        battle = combat.Combat(player, enemy, inventory)

        battle.fight()


################################################################################
#                          START - INTRO + NAMESWAHL                           #
################################################################################

# player = strings.intro()

# strings.game_start()
player = Player("Bob", 100, 10, location=location.village)  ### Intro überspringen
clear_screen()


################################################################################
#                                     GAME                                     #
################################################################################
inventory = Inventory()
town_shop = Shop()

worldmap = location.WorldMap()
ui = UserInterface()
options = {
    "Neutral": {
        "Umschauen": ui.umschauen,
        "Tasche": ui.tasche,
        "Laden": ui.laden,
        "Karte": ui.karte,
    },
    "Tasche": {},
    "Laden": {
        "Kaufen": ui.kaufen,
        "Verkaufen": ui.verkaufen,
        "Fragen": ui.fragen,
        "Verlassen": ui.verlassen,
    },
    "Karte": {},
}

################################################################################
#                                   RUN GAME                                   #
################################################################################


def run_game():
    clear_screen()
    print(" - ".join(options[ui.current]), "\n\n\n")

    player_input = input().title()
    if player_input == "V":
        ui.current = "Neutral"
    elif player_input in options[ui.current]:
        options[ui.current][player_input]()
    else:
        print(f"{player_input} konnte nicht ausgeführt werden.")


if __name__ == "__main__":
    while True:
        if ui.current not in options:
            ui.current = "Neutral"
        run_game()
