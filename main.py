################################################################################
#                                    MAIN                                      #
################################################################################

import time
import random
import strings
import world_map
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
            print("Welchen Gegenstand willst du benutzen? V zum zurückkehren\n")

            print(inventory)

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
        if player.location == location.unlock_cities.head.city:
            slow_print("Verkäufer", "Ich habe schon auf dich gewartet!!")
            self.kampf(location.spawn_shopkeeper)
            if self.current == "Laden":
                worldmap.add_city(player.location)
                location.unlock_cities.head = location.unlock_cities.head.next
                slow_print(
                    "Verkäufer",
                    f"Wow, was ein Kampf! (Der Verkäufer erzählt dir von {location.unlock_cities.head.city.name})",
                )

    def kaufen(self):
        global inventory
        inventory = town_shop.kaufen(inventory)

    def verkaufen(self):
        global inventory
        inventory = town_shop.verkaufen(inventory)

    def fragen(self):
        town_shop.fragen(player.location.name, worldmap)

    def verlassen(self):
        self.current = "Neutral"

    # # # # # # # # # # # # # # # # World Map # # # # # # # # # # # # # # # #
    def karte(self):
        while True:
            slow_print("Erzähler", "Wohin möchtest du reisen?", resume="")
            print("\nStadt  |  Route\n")
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
        print("Möchtest du nachschauen? - ja/j oder nein/n")
        inp = input().lower()
        clear_screen()
        if inp in ["ja", "j"]:
            time.sleep(1)
            slow_print("Erzähler", "Du sammelst deinen Mut und...")
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
        else:
            slow_print("Erzähler", "Du gehst weiter. Eiskalt.")

        clear_screen()
        time.sleep(1)
        slow_print("Erzähler", "Weiter gehts!")
        time.sleep(1)

        ### Letzte Kampfmöglichkeit ###
        slow_print("Erzähler", "Ich spüre etwas...")
        clear_screen()
        time.sleep(1)
        if random.randint(1, 10) >= 8:
            slow_print("Erzähler", random.choice(strings.reise_battle))
            self.kampf(random.choice(route.enemies))
        else:
            slow_print("Erzähler", random.choice(strings.reise_no_battle))

        player.location = city
        slow_print("Erzähler", city.name.upper().center(40))

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
    print(" - ".join(options[ui.current]), "- V" "\n")

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
