class Item:
    def __init__(self, category, name):
        self.name = name
        self.category = category

class Weapon(Item):
    def __init__(self, name, attack):
        super(Weapon, self).__init__("weapon", name)
        self.attack = attack