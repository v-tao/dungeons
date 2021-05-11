from enums.ITEM_TYPES import ItemTypes

class Item:
    def __init__(self, name, category, description):
        self.name = name
        self.category = category
        self.description = description

class Weapon(Item):
    def __init__(self, name, attack, description):
        super(Weapon, self).__init__(name, ItemTypes.WEAPON, description)
        self.attack = attack

class Armor(Item):
    def __init__(self, name, armor, description):
        super(Armor, self).__init__(name, ItemTypes.ARMOR, description)
        self.armor = armor

class Potion(Item):
    def __init__(self, name, health, description):
        super(Potion, self).__init__(name, ItemTypes.POTION, description)
        self.health = health