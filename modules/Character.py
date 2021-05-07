from enums.DEFAULT import Default
class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.pos = (Default.POS_I.value, Default.POS_J.value)
        self.inventory = []
    
    #returns True if win
    def combat(self, character):
        while self.health > 0 or character.health > 0:
            character.health -= self.strength
            if character.health <= 0:
                character.health = 0
                print(character.name + " died")
                return True
            self.health -= character.strength
            if self.health <= 0:
                self.health = 0
                print(character.name + " died")
                return False

    def status(self):
        print(self.name)
        print("HEALTH: " + str(self.health))
        print("STRENGTH: " + str(self.strength))
    
    def show_inventory(self):
        for item in self.inventory:
            print(item.name)