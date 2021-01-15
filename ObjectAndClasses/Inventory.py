class Inventory:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        result = self.__capacity
        return result

    def __repr__(self):
        free_space = self.__capacity - len(self.items)
        my_items = ', '.join(self.items)
        return f"Items: {my_items}.\nCapacity left: {free_space}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)
