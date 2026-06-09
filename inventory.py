class Inventory:
    def __init__(self):
        self.inventory = {}

    def __str__(self):
        if not self.inventory:
            return "Inventory is empty."
        return "Inventory:\n" + "\n".join(
            f"{item}: {quantity}" for item, quantity in self.inventory.items()
        )

    def add_item(self, item_name, quantity=1):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item(self, item_name, quantity=1):
        if item_name in self.inventory and self.inventory[item_name] >= quantity:
            self.inventory[item_name] -= quantity
            if self.inventory[item_name] == 0:
                del self.inventory[item_name]
        else:
            print(f"Not enough {item_name} in inventory.")

    def get_inventory(self):
        return self.inventory

    def has_item(self, item_name):
        return item_name in self.inventory and self.inventory[item_name] > 0
