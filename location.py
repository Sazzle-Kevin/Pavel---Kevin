################################################################################
#                                  LOCATION                                    #
################################################################################

from enemy import Enemy

################################################################################
#                            BASE GEGNER FÜR PAVEL                             #
################################################################################


########## Wald-Gegner ##########
def spawn_wolf():
    return Enemy("Wolf", 0, 0)


def spawn_boar():
    return Enemy("Wildschwein", 0, 0)


# Rare #
def spawn_golden_pig():
    return Enemy("Goldenes Schwein", 0, 0)


########## Höhlen-Gegner ##########
def spawn_spider():
    return Enemy("Spinne", 0, 0)


def spawn_bat():
    return Enemy("Fledermaus", 0, 0)


# Rare #
def spawn_cave_man():
    return Enemy("Steinzeitlicher Höhlenmensch", 0, 0)


########## Schloss- Gegner ##########
def spawn_vampire():
    return Enemy("Vampir", 0, 0)


def spawn_goblin():
    return Enemy("Goblin", 0, 0)


################################################################################
#                              KLASSE: LOCATION                                #
################################################################################


class Location:

    def __init__(
        self,
        name,
        description,
        city=False,
        events=None,
        enemies=None,
        rare_encounter=None,
    ):
        self.name = name
        self.city = city
        self.description = description
        self.events = events if events else []
        self.enemies = enemies
        self.rare_encounter = rare_encounter


################################################################################
#                                    STÄDTE                                    #
################################################################################

## Startgebiet ##
dorf = Location(
    "Dorf", "Ein schönes, kleines Dorf. Die Luft riecht wunderbar rein.", city=True
)

## Stadt 1 ##
sollum = Location("Sollum", "Die Häußer ragen bis in die Wolken!", city=True)

## Stadt 2 ##
monda = Location(
    "Monda", "Alles in der Stadt ist bunt und fantasievoll geschmückt.", city=True
)

## Letztes Gebiet ##
castle = Location(
    "Finsteres Schloss",
    "Das Schloss sieht verlassen aus.",
    enemies=[spawn_vampire, spawn_goblin],
)


################################################################################
#                               ZWISCHENGEBIETE                                #
################################################################################

## Wald ##
forrest = Location(
    "Wald",
    "Ein dichter Wald voller Geräusche.",
    events=[
        "Du siehst einen merkwürdigen Stein.",
        "Im Busch ist etwas.",
        "Dir fällt ein kleiner Erdhaufen auf.",
        "Du merkst etwas unter deinem Schuh.",
    ],
    enemies=[spawn_wolf, spawn_boar],
    rare_encounter=spawn_golden_pig,
)

## Höhle ##
cave = Location(
    "Höhle",
    "Eine dunkle Höhle. Tief drinnen hört man Wasser tropfen.",
    events=[
        "Im Dunkeln funkelt etwas.",
        "In einem Seitengang hörst du Wasser tropfen, doch nicht auf den nassen Boden, wie es sonst der Fall ist.",
        "Du spürst etwas über dir.",
        "Du merkst etwas unter deinem Schuh.",
    ],
    enemies=[spawn_spider, spawn_bat],
    rare_encounter=spawn_cave_man,
)

routes = [forrest, cave]
