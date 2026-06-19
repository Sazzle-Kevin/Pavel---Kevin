import random
import time
from text import slow_print, clear_screen
from player import Player
from enemy import Enemy
from inventory import Inventory
import items


class Combat:
    def __init__(self, player, enemy, inventory):
        self.player = player
        self.enemy = enemy
        self.inventory = inventory
        self.menu = {"1": "Angreifen", "2": "Heiltrank benutzen", "3": "Waffe ausrüsten", "4": "Fliehen"}
        self.multiplier = [[0, 0.5, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5, 1.5, 2],
                           [0.5, 1, 1, 1, 1, 1, 1, 1.5, 1.5, 2]]

    def combat_menu(self):  # Show combat menu
        for key, value in self.menu.items():
            print(key + ": " + value)

    def potion_menu(self):  # Show available potion options
        if self.inventory.has_item("Kleiner Heiltrank"):
            print("1. Kleinen Heiltrank benutzen")
        if self.inventory.has_item("Großer Heiltrank"):
            print("2. Großen Heiltrank benutzen")
        print("3. Zurück")

    def weapon_menu(self):
        weapons = {}
        index = 1
        for weapon_name, weapon in items.weapons.items():
            if self.inventory.has_item(weapon_name):
                weapons[index] = weapon        
                print(f"{index}: {weapon.name} (+{weapon.damage})")
                index += 1
        if weapons == {}:
            print("Keine Waffen im Inventar.")
        if self.player.weapon is not None:
            print(f"{index}: Waffe weglegen")
            index += 1
        print(f"{index}: Zurück")
        choice = input("Deine Wahl: ")
        if not choice.isdigit():
            print("Ungültige Auswahl!")
            time.sleep(1)
            return self.weapon_menu()
        choice = int(choice)
        if choice in weapons:
            weapon = weapons[choice]
            if self.player.weapon is not None:
                self.inventory.add_item(self.player.weapon, 1)
            self.player.use_weapon(weapon.name, weapon.damage)
            self.inventory.remove_item(weapon.name, 1)
            slow_print(
                "Erzähler",
                f"{self.player.name} rüstet {weapon.name} aus! Angriff +{weapon.damage}.\n",
                resume="",
            )
        elif choice == index - 1 and self.player.weapon is not None:
            self.inventory.add_item(self.player.weapon, 1)
            old_weapon = self.player.weapon
            self.player.weapon = None
            self.player.weapon_attack = 0
            slow_print(
                "Erzähler",
                f"{self.player.name} legt {old_weapon} weg.\n",
                resume="",
            )
        elif choice == index:
            return "back"
        else:
            print("Ungültige Auswahl!")
            time.sleep(1)
            return self.weapon_menu()
        

    def damage_multiplier(self, multiplier):  # Randomize attack strength
        damage_multiplier = random.choice(multiplier)
        match damage_multiplier:
            case 0:
                slow_print("Erzähler", "Verfehlt!\n\n", sleep=2, resume="")
            case 0.5:
                slow_print(
                    "Erzähler",
                    "Nur ein Streiftreffer!",
                    sleep=2,
                    resume="",
                )
            case 1:
                pass
            case 1.5:
                slow_print("Erzähler", "Starker Treffer!", sleep=2, resume="")
            case 2:
                slow_print("Erzähler", "Kritischer Treffer!", sleep=2, resume="")
        return damage_multiplier

    def player_attack(self):  # Calculate and deal player damage
        self.player.deal_damage(
            self.enemy,
            int((self.player.attack + self.player.weapon_attack) * self.damage_multiplier(self.multiplier[1] if self.player.weapon is not None else self.multiplier[0])),
        )

    def enemy_attack(self):  # Calculate and deal enemy damage
        self.enemy.deal_damage(
            self.player, int(self.enemy.attack * self.damage_multiplier(self.multiplier[0]))
        )

    def fight_intro(self):  # Show fight intro animation
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

    def player_turn(self):  # Handle player's turn
        self.combat_menu()
        choose = input("Deine Wahl: ")
        match choose:
            case "1":
                self.player_attack()
            case "2":
                self.potion_menu()
                choose_potion = input("Deine Wahl: ")
                match choose_potion:
                    case "1":
                        if self.inventory.has_item("Kleiner Heiltrank"):
                            self.player.heal(items.item_dict["Kleiner Heiltrank"].heal)
                            self.inventory.remove_item("Kleiner Heiltrank", 1)
                        else:
                            print("Ungültige Auswahl!")
                            time.sleep(1)
                            self.player_turn()
                    case "2":
                        if self.inventory.has_item("Großer Heiltrank"):
                            self.player.heal(items.item_dict["Großer Heiltrank"].heal)
                            self.inventory.remove_item("Großer Heiltrank", 1)
                        else:
                            print("Ungültige Auswahl!")
                            time.sleep(1)
                            self.player_turn()
                    case "3":
                        self.player_turn()
                    case _:
                        print("Ungültige Auswahl!")
                        time.sleep(1)
                        self.player_turn()
            case "3":
                if self.weapon_menu() == "back":
                    self.player_turn()
            case "4":
                slow_print("Erzähler", f"{self.player.name} flieht aus dem Kampf!")
                return "end_of_fight"
            case _:
                print("Ungültige Auswahl!")
                time.sleep(1)
                self.player_turn()

    def enemy_turn(self):  # Handle enemy's turn
        if self.enemy.is_alive():
            slow_print(
                "Erzähler",
                f"Jetzt ist {self.enemy.name} am Zug.\n",
                sleep=2,
                resume="",
                fresh=False,
            )
            self.enemy_attack()
        else:
            return

    def status(self):  # Show current fight status
        print(self.player, end=" ------ ")
        print(self.enemy)
        if self.player.weapon:
            print(
                " " * (len(self.player.name) + 1),
                f"Waffe: {self.player.weapon} (+{self.player.weapon_attack})"
            )
        else:
            print(
                " " * (len(self.player.name) + 1),
                "Waffe: Keine"
            )
        print(
            " " * (len(self.player.name) + 1),
            "Kleiner Heiltrank: ",
            self.inventory.get_quantity("Kleiner Heiltrank"),
        )
        print(
            " " * (len(self.player.name) + 1),
            "Großer Heiltrank:  ",
            self.inventory.get_quantity("Großer Heiltrank"),
            "\n",
        )

    def fight(self):  # Main fight loop
        start = random.choice(["player", "enemy"])
        self.fight_intro()
        while self.player.is_alive() and self.enemy.is_alive():
            self.status()
            time.sleep(3)
            if start == "player":
                if self.player_turn() == "end_of_fight":
                    return "fled"
                self.enemy_turn()
            else:
                self.enemy_turn()
                if self.player.is_alive():
                    clear_screen()
                    self.status()
                    if self.player_turn() == "end_of_fight":
                        return "fled"
                else:
                    return


# Test code - only runs when this file is executed directly
""" if __name__ == "__main__":
    player = Player("Kevin", 100, 10)
    enemy = Enemy("Goblin", 50, 25)
    inventory = Inventory()
    inventory.add_item("Kleiner Heiltrank", 3)
    inventory.add_item("Großer Heiltrank", 1)
    inventory.add_item("Holzaxt", 1)
    inventory.add_item("Holzschwert", 1)
    inventory.add_item("Kleiner Heiltrank", 3)
    combat = Combat(player, enemy, inventory)
    combat.fight()
    enemy = Enemy("Wolf", 35, 10, 6)
    combat = Combat(player, enemy, inventory)
    combat.fight() """
