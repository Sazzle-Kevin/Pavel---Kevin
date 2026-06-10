import random
import time
from text import slow_print, clear, clear_screen
from player import Player
from enemy import Enemy


class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.menu = {"1": "Angreifen", "2": "Heiltrank benutzen", "3": "Fliehen"}

    def combat_menu(self):
        for key, value in self.menu.items():
            print(key + ": " + value)

    def player_attack(self):
        damage_multiplier = random.choice(
            [0, 0.5, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5, 1.5, 2]
        )
        match damage_multiplier:
            case 0:
                slow_print("Erzähler", "Verfehlt!")
            case 0.5:
                slow_print("Erzähler", "Nur ein Streiftreffer!")
            case 1:
                pass
            case 1.5:
                slow_print("Erzähler", "Starker Treffer!")
            case 2:
                slow_print("Erzähler", "Kritischer Treffer!")
        self.player.deal_damage(
            self.enemy,
            int((self.player.attack + self.player.weapon) * damage_multiplier),
        )

    def enemy_attack(self):
        self.enemy.deal_damage(self.player)

    def fight(self):
        start = random.choice(["player", "enemy"])
        for _ in range(5):
            clear_screen()
            time.sleep(0.1)
            print("######   ##      #####     ##    ##   #########")
            print("##       ##     ##   ##    ##    ##      ##")
            print("##       ##    ##          ##    ##      ##")
            print("#####    ##   ##    ####   ########      ##")
            print("##       ##    ##     ##   ##    ##      ##")
            print("##       ##     ##   ##    ##    ##      ##")
            print("##       ##      #####     ##    ##      ##")
            print()
            time.sleep(0.2)
        if start == "player":
            while self.player.is_alive() and self.enemy.is_alive():
                print(self.player, end=" ------ ")
                print(self.enemy, "\n")
                self.combat_menu()
                choose = input("Deine Wahl: ")
                match choose:
                    case "1":
                        self.player_attack()
                    case "2":
                        self.player.heal(50)
                    case "3":
                        slow_print(
                            "Erzähler", f"{self.player.name} flieht aus dem Kampf!"
                        )
                        return
                if self.enemy.is_alive():
                    print(self.player, end=" ------ ")
                    print(self.enemy, "\n")
                    slow_print("Erzähler", f"Jetzt ist {self.enemy.name} am Zug.\n")
                    self.enemy_attack()
                else:
                    return
        else:
            while self.player.is_alive() and self.enemy.is_alive():
                if self.enemy.is_alive():
                    print(self.player, end=" ------ ")
                    print(self.enemy, "\n")
                    slow_print("Erzähler", f"Jetzt ist {self.enemy.name} am Zug.\n")
                    self.enemy_attack()
                if self.player.is_alive():
                    print(self.player, end=" ------ ")
                    print(self.enemy, "\n")
                    self.combat_menu()
                    choose = input("Deine Wahl: ")
                    match choose:
                        case "1":
                            self.player_attack()
                        case "2":
                            self.player.heal(50)
                        case "3":
                            slow_print(
                                "Erzähler", f"{self.player.name} flieht aus dem Kampf!"
                            )
                            return
                else:
                    return


# Test Code - Kevin vs Goblin :-D
# player = Player("Kevin", 100, 10)
# enemy = Enemy("Goblin", 50)
# combat = Combat(player, enemy)
# combat.fight()
