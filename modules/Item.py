class Item:
    def __init__(self, name, category):
        self.name = name
        self.category = category

class Weapon(Item):
    def __init__(self, name, attack):
        super(Weapon, self).__init__(name, "weapon")
        self.attack = attack