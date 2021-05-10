from enums.ITEM_TYPES import ItemTypes

class Item:
    def __init__(self, name, category):
        self.name = name
        self.category = category

class Weapon(Item):
    def __init__(self, name, attack):
        super(Weapon, self).__init__(name, ItemTypes.WEAPON)
        self.attack = attack

class Armor(Item):
    def __init__(self, name, armor):
        super(Armor, self).__init__(name, ItemTypes.ARMOR)
        self.armor = armor

class Potion(Item):
    def __init__(self, name, health):
        super(Potion, self).__init__(name, ItemTypes.POTION)
        self.health = health