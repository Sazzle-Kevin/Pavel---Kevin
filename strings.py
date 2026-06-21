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
    slow_print("Dorfbewohner", "Ich glaube, er wacht auf.")
    slow_print(
        "Dorfbewohner2",
        "Er hat es fast geschafft! Er hat das legendäre Schwert Braht D. Wuhurst.. fast..  aus dem Stein gezogen!",
    )
    slow_print("Dorfbewohner3", "Der Auserwählte!"),
    slow_print("Dorfbewohner3", "  ...", 1)
    slow_print("Dorfbewohner", "Hallo?")
    slow_print("Dorfbewohner", "Kannst du uns hören?")
    slow_print("Dorfbewohner3", "Wie war nochmal sein Name?")

    print("\n\n\nName: ", end="")
    player_name = input()
    player = Player(player_name, 100, 10, location=location.village)

    slow_print(f"Dorfbewohner", f"{player.name}!")
    print(end="")
    clear_screen()
    time.sleep(1)

    slow_print("Erzähler", "Und da stand er nun.", fresh=False)
    slow_print(
        "Erzähler",
        "Viele Dorfbewohner haben versucht das legendäre Schwert aus dem Stein zu ziehen.",
        fresh=False,
    )
    slow_print(
        "Erzähler",
        "Doch laut Prophezeiung sollte nur der Auserwählte, der ein reines Herz und einen gesunden Appetit in sich trägt, Herr dieses Schwertes werden.",
        fresh=False,
    )
    slow_print(
        "Erzähler",
        "Und so gelang jenes legendäre Schwert in die Hände eines Helden, dessen Ziel es war, die entführte Prinzessin zu retten!",
        fresh=False,
    )

    clear_screen()
    time.sleep(1)
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

# # # # # # # # # # # # # # # # Boss Strings # # # # # # # # # # # # # # # #


def boss():
    slow_print("Erzähler", "...", delay=1)
    slow_print("Erzähler", "Du betrittst das Schloss.")
    slow_print(
        "Erzähler", "Du merkst, wie eine unheilvolle Finsternis dich umschließt!"
    )
    slow_print(
        "Erzähler",
        "Deine Sicht schwindet. Flüsternde Stimmen sprechen zu dir, bitten dich um Hilfe... bitten dich, ihnen die Freiheit zu gewähren.",
    )
    slow_print(
        "Erzähler",
        "Das riesige, modrige Holztor schlägt hinter dir zu. Du stehst in vollkommener Dunkelheit.",
    )
    clear_screen()
    time.sleep(2)

    slow_print("Erzähler", "Die Stimmen verstummen.")
    slow_print("Erzähler", "Im ganzen Raum glimmern kleine Punkte auf.")
    slow_print(
        "Erzähler",
        "Wie aus dem Nichts entzünden sich blau lodernde Kerzen. Die Flammen peitschen wild empor und tauchen den Saal in ein gleißendes Licht!",
    )
    slow_print("Erzähler", "Am Ende des Raumes sitzt jemand auf dem Thron.")
    slow_print(
        "Erzähler",
        "Zwei unheilvoll grün leuchtende Augen durchbohren dich mit ihrem Blick.",
    )
    slow_print(
        "Erzähler",
        "Neben der finsteren Gestalt siehst du noch jemanden in Ketten sitzen.",
    )
    slow_print(
        "Prinzessin Nix Die Code",
        "Bitte Held, rette mich! Ich bin eine entführte Prinzessin!",
    )
    slow_print(
        "Erzähler",
        "Das ist der Moment, auf den jeder Held wartet. Doch bevor du handeln kannst, erhebt sich eine weitere Stimme.",
    )
    clear_screen()
    time.sleep(1)
    slow_print(
        "Vampir Lord Byte von Code",
        "Ich habe schon von einem Helden gehört, der auf dem Weg sein soll, um mich zu besiegen.",
    )
    slow_print(
        "Vampir Lord Byte von Code", "So früh habe ich dich jedoch nicht erwartet..."
    )
    slow_print("Vampir Lord Byte von Code", "Ich bin beeindruckt.")
    slow_print(
        "Vampir Lord Byte von Code",
        "Ein Held, würdig des Auftrages, die Prinzessin zu befreien.",
    )
    slow_print(
        "Vampir Lord Byte von Code",
        "Doch Mut allein reicht nicht. Besitzt du die Stärke, die nötig ist, um dich mir entgegenzustellen?",
    )
    slow_print("Vampir Lord Byte von Code", "Zeig es mir!")


# # # # # # # # # # # # # # # # Outro # # # # # # # # # # # # # # # #


def outro(char):
    slow_print(
        "Erzähler",
        f"Und so besiegte {char.name} den gefürchteten Vampir Lord Byte von Code.",
    )
    slow_print("Prinzessin Nix Die Code", "Du.. hast mich gerettet. 👁️👄👁️")
    slow_print(
        "Erzähler",
        "Und so machten sich die Prinzessin und der Held auf den Weg zurück.",
    )
    slow_print(
        "Erzähler",
        "Sie lebten von dort an glücklich zusammen und der Held vollbrachte noch viele Heldentaten.",
    )
    slow_print("Erzähler", "ENDE")

    slow_print("", "Danke fürs Spielen!".center(40), delay=0.1)
    while True:
        clear_screen()
        print("Danke fürs Spielen!".center(40))
        time.sleep(5)
