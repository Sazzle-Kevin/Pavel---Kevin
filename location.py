from enemy import Enemy


def spawn_wolf():
    return Enemy("Wolf", 0, 0)


def spawn_boar():
    return Enemy("Wildschwein", 0, 0)


def spawn_golden_pig():
    return Enemy("Goldenes Schwein", 0, 0)


def spawn_spider():
    return Enemy("Spinne", 0, 0)


def spawn_bat():
    return Enemy("Fledermaus", 0, 0)


def spawn_cave_man():
    return Enemy("Steinzeitlicher Höhlenmensch", 0, 0)


def spawn_vampire():
    return Enemy("Vampir", 0, 0)


def spawn_goblin():
    return Enemy("Goblin", 0, 0)


class Location:

    def __init__(self, name, city=False, enemies=None, rare_encounter=None):
        self.name = name
        self.city = city
        self.enemies = enemies
        self.rare_encounter = rare_encounter


dorf = Location("Dorf", city=True)
forrest = Location(
    "Wald", enemies=[spawn_wolf, spawn_boar], rare_encounter=spawn_golden_pig
)
cave = Location(
    "Höhle", enemies=[spawn_spider, spawn_bat], rare_encounter=spawn_cave_man
)
sollum = Location("Sollum", city=True)
monda = Location("Monda", city=True)
castle = Location("Finsteres Schloss", enemies=[spawn_vampire, spawn_goblin])
