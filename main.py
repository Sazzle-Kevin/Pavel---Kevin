import time
import strings
import world_map
from world_map import current_location
import location
from inventory import Inventory
from player import Player
from text import slow_print, clear, clear_screen

inventory = Inventory()


def run_game():
    print(" - ".join(key for key in options if options[key] is True), "\n")

    player_input = input().title()
    if options.get(player_input):
        options_input[player_input]()


def interact_inventory():
    while True:
        print(" - ".join(["Öffnen", "Benutzen", "Schließen"]))
        inventory_input = input()
        clear_screen()
        if inventory_input.title() == "Öffnen":
            print(inventory, "\n")
        elif inventory_input.title() == "Benutzen":
            break  ## pass
        elif inventory_input.title() == "Schließen":
            break  ## pass


options = {
    "Inventar": True,
    "Umgebung": True,
    "Laden": False,
    "Karte": True,
}

options_input = {
    "Inventar": interact_inventory,
    "Umgebung": interact_inventory,  ## pass
    "Laden": interact_inventory,  ## pass
    "Karte": interact_inventory,  ## pass
}

################################################################################
#                          START - INTRO + NAMESWAHL                           #
################################################################################

strings.intro()

strings.game_start()


################################################################################
#                                     GAME                                     #
################################################################################

while True:
    run_game()
