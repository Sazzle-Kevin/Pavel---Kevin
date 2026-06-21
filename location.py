################################################################################
#                                  LOCATION                                    #
################################################################################

import enemy

################################################################################
#                              KLASSE: WORLDMAP                                #
################################################################################


class WorldMap:

    def __init__(self):
        self.locations = {
            village: {monda: forrest},
            monda: {village: forrest},
            sollum: {},
            castle: {},
        }

    def add_city(self, city):
        if city == monda:
            self.locations[sollum][monda] = self.locations[monda][sollum] = cave
            self.locations[sollum][village] = self.locations[village][sollum] = cave
        elif city == sollum:
            self.locations[castle][sollum] = self.locations[sollum][castle] = dark_moor
            self.locations[castle][monda] = self.locations[monda][castle] = dark_moor
            self.locations[castle][village] = self.locations[village][castle] = (
                dark_moor
            )

    def print(self, current):
        for location, distance in self.locations[current].items():
            print(f"{location.name}:     {distance.name}")
        print("\n\n-- V zum Verlassen --\n\n\n")


################################################################################
#                                 BASE GEGNER                                  #
################################################################################


########## Stadt - Gegner ##########
def spawn_shopkeeper():
    return enemy.Enemy(
        "Verkäufer", 1, 1, 1
    )  ############################# Stats noch ändern (Pavel) ####################################⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️


########## Wald - Gegner ##########
def spawn_wolf():
    return enemy.Enemy("Wolf", 35, 10, 6)


def spawn_boar():
    return enemy.Enemy("Wildschwein", 45, 15, 8)


# Rare #
def spawn_golden_pig():
    return enemy.Enemy("Goldenes Schwein", 25, 30, 4)


########## Höhlen - Gegner ##########
def spawn_spider():
    return enemy.Enemy("Spinne", 40, 12, 7)


def spawn_bat():
    return enemy.Enemy("Fledermaus", 25, 8, 5)


# Rare #
def spawn_cave_man():
    return enemy.Enemy("Steinzeitlicher Höhlenmensch", 65, 35, 12)


########## Finstermoor - Gegner ##########
def spawn_vampire():
    return enemy.Enemy("Vampir", 80, 20, 15)


def spawn_goblin():
    return enemy.Enemy("Goblin", 50, 20, 10)


# Rare #
def spawn_corrupted_syntax():
    return enemy.Enemy(
        "Korrumpierter Lord Synt von Ax", 1, 1, 1
    )  ############################# Stats noch ändern (Pavel) ####################################⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️


########## Schloss ##########


def spawn_vampire_lord():
    return enemy.Enemy(
        "Vampir Lord Byte von Code", 1, 1, 1
    )  ############################ Stats noch ändern (Pavel) ####################################⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️


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
village = Location(
    "Dorf",
    "Ein schönes, kleines Dorf. Die Luft riecht wunderbar rein.",
    city=True,
)

## Stadt 1 ##
monda = Location(
    "Monda",
    "Alles in der Stadt ist bunt und fantasievoll geschmückt.",
    city=True,
)

## Stadt 2 ##
sollum = Location(
    "Sollum",
    "Die Häußer ragen bis in die Wolken!",
    city=True,
)

## Letztes Gebiet ##
castle = Location(
    "Finsteres Schloss",
    "Das Schloss sieht verlassen aus.",
    enemies=[spawn_vampire_lord],
)

cities = [village, monda, sollum, castle]

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

## Finstermoor ##
dark_moor = Location(
    "Finstermoor",
    "Deine Stiefel geben nach im Moor. Totes Land, schwarze Gewässer und lauernde Schatten",
    events=[
        "Im Schlamm funkelt etwas.",
        "Hinter einem toten Baum verbirgt sich etwas.",
        "Hey, pass auf wo du hintrittst!",
        "Du merkst etwas in deinem Schuh.",
    ],
    enemies=[spawn_vampire, spawn_goblin],
    rare_encounter=spawn_cave_man,
)

routes = [forrest, cave, dark_moor]

################################################################################
#                              STÄDTE FREISCHALTEN                             #
################################################################################


class LockedCities:

    def __init__(self, city):
        self.city = city
        self.next = None


class Unlocks:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, city):
        new_city = LockedCities(city)
        if self.head is None:
            self.head = self.tail = new_city
            return

        self.tail.next = new_city
        self.tail = self.tail.next


unlock_cities = Unlocks()

for city in cities[1:]:
    unlock_cities.append(city)
