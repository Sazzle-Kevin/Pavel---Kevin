from text import slow_print, clear


class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.weapon = None
        self.weapon_attack = 0
        self.level = 1
        self.xp = 0
        self.location = None

    def __str__(self):
        return f"{self.name}: Health={self.health}/{self.max_health}, Attack={self.attack+self.weapon_attack}, Level={self.level}, XP={self.xp}/{self.level*25}"

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def deal_damage(self, target, damage):
        if damage != 0:
            target.take_damage(self, damage)

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

        slow_print(
            "Erzähler",
            f"{self.name} heilt sich um {amount} Lebenspunkte und hat jetzt {self.health} Lebenspunkte.\n",
            resume="",
        )

    def use_weapon(self, name, attack):
        self.weapon_attack = attack
        self.weapon = name

    def get_xp(self, xp):
        self.xp += xp
        slow_print("Erzähler", f"{self.name} erhält {xp} Erfahrungspunkte!", resume="")
        self.level_up()

    def level_up(self):
        while self.xp >= self.level * 25:
            self.level += 1
            self.attack += 2
            self.xp -= (self.level - 1) * 25
            slow_print(
                "Erzähler",
                f"{self.name} wird stärker und erreicht Level {self.level}! Angriff +2.",
                resume="",
            )
