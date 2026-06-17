################################################################################
#                                    MAIN                                      #
################################################################################

import time
import random
import strings
import world_map
import world_map
import location
import combat
import items
import enemy
from inventory import Inventory
from player import Player
from text import slow_print, clear, clear_screen

################################################################################
#                                   RUN GAME                                   #
################################################################################


def run_game():
    print(" - ".join(options[ui.current]), "\n")

    player_input = input().title()
    if player_input in options[ui.current]:
        options[ui.current][player_input]()
    else:
        print(f"{player_input} konnte nicht ausgeführt werden.")


################################################################################
#                                     UI                                       #
################################################################################


class UserInterface:

    def __init__(self):
        self.current = "Neutral"

    # # # # # # # # # # # # # # # # Inventory # # # # # # # # # # # # # # # #  ## Wird vermutlich noch überarbeitet ##
    def tasche(self):
        self.current = "Tasche"

        for item, quantity in inventory.inventory.items():
            print(f"{item}  x{quantity}")

        while True:
            print("Welchen Gegenstand willst du benutzen? V zum zurückkehren")
            inp = input()

            if inp.lower() == "v":
                self.current = "Neutral"
                return
            elif inp.title() in inventory.inventory and items[inp.title()].use is True:
                print(
                    f"Möchtest du {inp.title()} benutzen?\n", "ja/j - nein/n"
                )  ### Anzeige Verringerung der Anzahl später ###
                sec_inp = input()
                if sec_inp.lower() in ["ja", "j"]:
                    inventory.remove_item(inp.title())
                    slow_print("Erzähler", f"{player.name} benutzt {inp.title()}!")
                elif sec_inp.lower() in ["nein", "n"]:
                    continue
                else:
                    print(f"{sec_inp} wurde nicht erkannt.")
            else:
                if inp.title() not in inventory.inventory:
                    print(f"Du besitzt kein {inp}")
                else:
                    print(f"{inp} kann nicht benutzt werden.")

    def schließen(self):  ## Wird gerade nie benutzt ##
        self.current = "Neutral"

    # # # # # # # # # # # # # # # # Look around # # # # # # # # # # # # # # # #
    def umschauen(self):
        local = player.location

        if local.events:
            slow_print("Erzähler", random.choice(local.events))
        else:
            slow_print("Erzähler", local.description)

    # # # # # # # # # # # # # # # # Shop # # # # # # # # # # # # # # # #
    def laden(self):
        self.current = "Laden"

    def kaufen(self):  ### Nicht fertig ###
        return

    def verkaufen(self):  ### Nicht fertig ###
        return

    def verlassen(self):
        self.current = "Neutral"

    # # # # # # # # # # # # # # # # World Map # # # # # # # # # # # # # # # #
    def karte(self):
        self.current = "Karte"
        print("Wohin möchtest du reisen?")

    def wegstecken(self):
        self.current = "Neutral"

    def ziel(self, location):
        self.reisen()
        self.current = "Neutral"
        player.location = location

    # # # # # # # # # # # # # # # # Reisen # # # # # # # # # # # # # # # #

    def reisen(self):
        route = random.choice(location.routes)
        slow_print(
            "Erzähler",
            f"{player.name} macht sich auf die Reise. Route: {route.name}.",
        )
        slow_print("Erzähler", f"{route.description}")

        ## Erste Kampfmöglichkeit ##
        slow_print("Erzähler", "Hier ist etwas...")
        time.sleep(1)
        if random.randint(1, 10) >= 8:
            slow_print("Erzähler", random.choice(strings.reise_battle), delay=0.03)
            self.kampf(route)
        else:
            slow_print("Erzähler", random.choice(strings.reise_no_battle))

        time.sleep(1)
        slow_print("Erzähler", "Weiter gehts!")
        time.sleep(1)

        ## Mitte der Reise - Event ##
        slow_print("Erzähler", random.choice(route.events))
        print("Möchtest du nachschauen? - ja/j oder nein/n")
        inp = input().lower()
        if inp in ["ja", "j"]:
            clear_screen()
            time.sleep(1)
            slow_print("Erzähler", "Du sammelst deinen Mut und...")
            chance = random.randint(1, 10)
            time.sleep(1)
            if chance >= 7:
                loot = random.choice(event_items)
                slow_print("Erzähler", f"Nice! Du hast {loot.name} gefunden!")
                inventory[loot] = inventory.get(loot, 0) + 1
            else:
                slow_print("Erzähler", "Oh nein, ein Überfall!")
                self.kampf(route)
        else:
            slow_print("Erzähler", "Du gehst weiter. Eiskalt.")

        time.sleep(1)
        slow_print("Erzähler", "Weiter gehts!")
        time.sleep(1)

        ### Letzte Kampfmöglichkeit ###
        slow_print("Erzähler", "Ich spüre etwas...")
        if random.randint(1, 10) >= 8:
            slow_print("Erzähler", random.choice(strings.reise_battle), delay=0.03)
            self.kampf(route)
        else:
            slow_print("Erzähler", random.choice(strings.reise_no_battle))

    # # # # # # # # # # # # # # # # Kampf # # # # # # # # # # # # # # # #

    def kampf(self, route):
        enemy = random.choice(route.enemies)()
        battle = combat.Combat(player, enemy, inventory)

        battle.fight()


################################################################################
#                          START - INTRO + NAMESWAHL                           #
################################################################################

# player = strings.intro()

# strings.game_start()
player = Player("Bob", 100, 10)  ### Intro überspringen


################################################################################
#                                     GAME                                     #
################################################################################
inventory = Inventory()
event_items = [
    items.small_potion,
    items.small_potion,
    items.small_potion,
    items.small_potion,
    items.small_potion,
    items.big_potion,
    items.big_potion,
    items.big_potion,
    items.wood_axe,
    items.wood_sword,
]
worldmap = world_map.WorldMap()
ui = UserInterface()
options = {
    "Neutral": {
        "Umschauen": ui.umschauen,
        "Tasche": ui.tasche,
        "Laden": ui.laden,
        "Karte": ui.karte,
    },
    "Tasche": {"Schließen": ui.schließen},
    "Laden": {
        "Kaufen": ui.kaufen,
        "Verkaufen": ui.verkaufen,
        "Verlassen": ui.verlassen,
    },
    "Karte": {
        "Dorf": lambda: ui.ziel(location.dorf),
        "Sollum": lambda: ui.ziel(location.sollum),
        "Monda": lambda: ui.ziel(location.monda),
        "Wegstecken": ui.wegstecken,
    },
}

while True:
    if ui.current not in options:
        ui.current = "Neutral"
    run_game()
