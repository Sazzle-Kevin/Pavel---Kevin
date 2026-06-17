################################################################################
#                                   STRINGS                                    #
################################################################################

import time
import random
import location
from player import Player
from text import slow_print, clear, clear_screen

################################################################################
#                            INTRO / NAME SELECTION                            #
################################################################################


def intro():
    slow_print("Dorfbewohner", "Ich glaube, er wacht auf.", 2)
    slow_print(
        "Dorfbewohner2",
        "Er hat es wirklich geschafft! Er hat das legendäre Schwert Braht'wuhurst aus dem Stein gezogen!",
        2,
    )
    slow_print("Dorfbewohner3", "Der Auserwählte!", 2),
    slow_print("Dorfbewohner3", "  ...", 1, 1)
    slow_print("Dorfbewohner", "Hallo?", 1.5)
    slow_print("Dorfbewohner", "Kannst du uns hören?", 1.5)
    slow_print("Dorfbewohner3", "Wie war nochmal sein Name?")

    print("  Name: ", end="")
    player_name = input()
    player = Player(player_name, 100, 10)

    slow_print(f"Dorfbewohner", f"{player.name}!", 2)
    print(end="")
    clear_screen()
    time.sleep(2)

    slow_print("Gott", "Und da stand er nun.", fresh=False)
    slow_print(
        "Gott",
        "Viele Dorfbewohner haben versucht das legendäre Schwert aus dem Stein zu ziehen.",
        fresh=False,
    )
    slow_print(
        "Gott",
        "Doch laut Prophezeiung sollte nur der Auserwählte, der ein reines Herz und einen gesunden Appetit in sich trägt, dazu in der Lage sein.",
        fresh=False,
    )
    slow_print(
        "Gott",
        "Und so gelang jenes legendäre Schwert in die Hände eines Helden, dessen Ziel es war, die entführte Prinzessin zu retten!",
        fresh=False,
    )

    clear_screen()
    time.sleep(1.5)
    slow_print(
        "Erzähler",
        f"So begab sich {player.name} auf seinen Weg die Prinzessin zu befreien und ein echter Held zu werden!",
    )
    return player


################################################################################
#                                 GAME START                                   #
################################################################################


def game_start():
    print()
    titel_name = "DUNGEON QUEST".center(80)
    slow_print("", titel_name, 3, 0.1)
    clear_screen
    time.sleep(1)

    slow_print("Erzähler", "Dises Spiel ist ein Text-Based RPG Adventure.", 3)
    slow_print(
        "Erzähler",
        "Interagiere mit der Welt oder führe Aktionen aus, indem du eine der angezeigten Befehle eingibst.",
        3,
        rows=1,
    )
    slow_print("Erzähler", "Viel Erfolg junger Held.", 3, rows=1)
    clear_screen


################################################################################
#                                   STRINGS                                    #
################################################################################

# # # # # # # # # # # # # # # # Reise Strings # # # # # # # # # # # # # # # #

reise_battle = [
    "Es hat Füß! Achtung!",
    "Es hat Hände! Achtung!",
    "Es hat Augen! Achtung!",
    "Es hat wuschige Augenbrauen! Achtung!",
]
reise_no_battle = [
    "Ein Schmetterling.",
    "Ein Frosch.",
    "Ein blauer Pilz neben einem roten Pilz.",
    "Eine frische Brise.",
]
