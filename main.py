import time
from player import Player
from text import slow_print, clear

options = {
    "Inventar": True,
    "Umgebung": True,
    "Shop": False,
    "Weiter reisen": True,
}

## Start ##

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
clear(50)
time.sleep(2)

print("Und da stand er nun.".center(80))
time.sleep(2)
print(
    "Viele Dorfbewohner haben versucht das legendäre Schwert aus dem Stein zu ziehen.".center(
        80
    )
)
time.sleep(3)
print(
    "Doch laut Prophezeiung wird nur der Auserwählte, der ein reines Herz und einen gesunden Appetit in sich trägt, dazu in der Lage sein.".center(
        80
    )
)
time.sleep(5)
print(
    "Und so gelang jenes legendäre Schwert in die Hände eines Helden, dessen Ziel es war, die entführte Prinzessin zu retten!".center(
        80
    )
)
time.sleep(6)
clear(50)
time.sleep(1.5)


slow_print("Erzähler", "--STATS--", 1)
slow_print("Erzähler", f"Name: {player.name}", rows=2)
slow_print(
    "Erzähler",
    "Äußeres: Gold glänzendes Haar, weißes Hemd, grüne Hose, braune Stiefel",
    rows=1,
)
slow_print("Erzähler", "Körperbau: Naja", rows=1)
slow_print("Erzähler", "Traum: Eines Tages ein Held sein", rows=1)
slow_print("Erzähler", "Vorteile: Mut, reines Herz", rows=1)
slow_print(
    "Erzähler",
    "Nachteile: Schmächtig, arm, klein, geizig, impulsiv, kann nicht mit Waffen umgehen, leichtgläubig, naiv, schusselig,\n überheblich, verpeilt, dumm, zerstreut, hungrig",
    4,
    rows=1,
)

clear(50)
time.sleep(1)
slow_print(
    "Erzähler",
    f"Und so begab sich {player.name} auf seinen Weg die Prinzessin zu befreien und ein echter Held zu werden!",
)

## Start Ende ##

## Spiel Beginn ##

titel_name = "DUNGEON QUEST".center(80)
slow_print("", titel_name, 3, 0.1)
clear(50)
time.sleep(1)

slow_print("Erzähler", "Dises Spiel ist ein Text-Based RPG Adventure.", 3)
slow_print(
    "Erzähler",
    "Interagiere mit der Welt oder führe Aktionen aus, indem du eine der angezeigten Befehle eingibst.",
    3,
    rows=1,
)
slow_print("Erzähler", "Viel Erfolg junger Held.", 3, rows=1)

print(" - ".join(key for key in options if options[key] is True))
