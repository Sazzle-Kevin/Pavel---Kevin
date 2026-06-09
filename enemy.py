class Enemy:
    def __init__(self, name, health, attack=10):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack

    def __str__(self):
        return (
            f"{self.name}: Health={self.health}/{self.max_health}, Attack={self.attack}"
        )

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been defeated!")
        else:
            print(
                f"{self.name} takes {damage} damage and has {self.health} health left."
            )

    def deal_damage(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack} damage!")
        target.take_damage(self.attack)

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {amount} and now has {self.health} health.")
