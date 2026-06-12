from text import slow_print, clear


class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.weapon = 0

    def __str__(self):
        return (
            f"{self.name}: Health={self.health}/{self.max_health}, Attack={self.attack}"
        )

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def deal_damage(self, target, damage):
        target.take_damage(damage)

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

        slow_print(
            "Erzähler",
            f"{self.name} heals for {amount} and now has {self.health} health.",
            resume="",
        )

    def use_weapon(self, attack):
        self.weapon = attack
