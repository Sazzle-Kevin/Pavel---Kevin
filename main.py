################################################################################
#                                    MAIN                                      #
################################################################################

import time
import random
import strings
import world_map
import world_map
import location
from inventory import Inventory
from player import Player
from text import slow_print, clear, clear_screen

################################################################################
#                             SPIELER - INVENTORY                              #
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

    ########## Inventory ##########   ## Wird vermutlich noch überarbeitet ##
    def tasche(self):
        self.current = "Tasche"

        for item, quantity in inventory.inventory.items():
            print(f"{item}  x{quantity}")

        while True:
            print("Welchen Gegenstand willst du benutzen? Verlassen/V zum zurückkehren")
            inp = input()

            if inp.lower() == "verlassen":
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

    ########## Look around ##########
    def umschauen(self):
        local = player.location

        if local.events:
            slow_print("Erzähler", random.choice(local.events))
        else:
            slow_print("Erzähler", local.description)

    ########## Shop ##########
    def laden(self):
        self.current = "Laden"

    def kaufen(self):  ### Nicht fertig ###
        return

    def verkaufen(self):  ### Nicht fertig ###
        return

    def verlassen(self):
        self.current = "Neutral"

    ########## World Map ##########
    def karte(self):
        self.current = "Karte"
        print("Wohin möchtest du reisen?")

    def wegstecken(self):
        self.current = "Neutral"

    def ziel(self, location):
        self.reisen()
        self.current = "Neutral"
        player.location = location

    ########## Reisen ##########

    def reisen(self):
        route = random.choice(location.routes)
        slow_print(
            "Erzähler",
            f"{player.name} macht sich auf die Reise. Route: {route.name}.",
        )
        slow_print("Erzähler", f"{route.description}")

        ## Erste Kampfmöglichkeit ##
        if random.randint(1, 10) >= 8:
            self.kampf(route)

        ## Mitte der Reise - Event ##
        slow_print("Erzähler", random.choice(route.events))
        print("Möchtest du nachschauen? - ja/j oder nein/n")
        inp = input().lower()
        if inp in ["ja", "j"]:
            clear_screen()
            time.sleep(1)
            slow_print("Erzähler", "Du sammelst deinen Mut und...")
            chance = random.randint(1, 10)
            if chance >= 7:
                slow_print(
                    "Erzähler", "Nice! Du hast einen Pudding gefunden!"
                )  ### Nicht fertig ###
            else:
                slow_print("Erzähler", "Oh nein, ein Überfall!")
                self.kampf(route)
        else:
            slow_print("Erzähler", "Du gehst weiter. Eiskalt.")

        ### Letzte Kampfmöglichkeit ###
        if random.randint(1, 10) >= 8:
            self.kampf(route)

    ########## Kampf ##########

    def kampf(self, location):
        old_curr = self.current
        enemy = random.choice(location.enemies)
        self.current = "Kampf"

        while self.current != "Fliehen":
            print(" - ".join(options[ui.current]), "\n")

            result = None
            player_input = input().title()
            if player_input in options[ui.current]:
                if player_input == "Attacke":
                    options[ui.current][player_input](enemy)
                else:
                    result = options[ui.current][player_input]()
            else:
                print(f"{player_input} konnte nicht ausgeführt werden.")
                continue

            if enemy.health <= 0:
                slow_print("Erzähler", f"{enemy.name} wurde besiegt!")
                slow_print(
                    "Erzähler", f"{player.name} erhält: Pudding"
                )  ### Muss ich noch bearbeitet werden ###
                break

            if result == "Fliehen":
                slow_print(
                    "Erzähler",
                    "Du konntest erfolgreich fliehen und setzt deine Reise fort.",
                )
                break

            enemy.deal_damage(player)
        self.current = old_curr

    def attacke(self, enemy):
        player.deal_damage(enemy)

    def kampf_items(self):  ### Bearbeiten ich noch ###
        pass
        return "Kampf"

    def fliehen(self):
        return "Fliehen"


################################################################################
#                          START - INTRO + NAMESWAHL                           #
################################################################################

player = strings.intro()

strings.game_start()


################################################################################
#                                     GAME                                     #
################################################################################
inventory = Inventory()
items = {}
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
    "Kampf": {"Attacke": ui.attacke, "Items": ui.kampf_items, "Fliehen": ui.fliehen},
}

while True:
    if ui.current not in options:
        ui.current = "Neutral"
    run_game()
