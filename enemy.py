from text import slow_print, clear
import time


class Enemy:
    def __init__(self, name, health, xp, attack=10):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.xp = xp

    def __str__(self):
        return (
            f"{self.name}: Health={self.health}/{self.max_health}, Attack={self.attack}"
        )

    def take_damage(self, target, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            target.get_xp(self.xp)
            slow_print("Erzähler", f"{self.name} wurde besiegt!")
        else:
            slow_print(
                "Erzähler",
                f"{self.name} erleidet {damage} Schaden und hat noch {self.health} Lebenspunkte.\n\n",
                resume="",
            )

    def deal_damage(self, target, damage):
        if damage != 0:
            slow_print(
                "Erzähler",
                f"{self.name} greift {target.name} an und verursacht {damage} Schaden!\n\n",
                sleep=0.5,
                resume="",
            )
            target.take_damage(damage)

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(
            f"{self.name} heals for {amount} and now has {self.health} health.",
            resume="",
        )
