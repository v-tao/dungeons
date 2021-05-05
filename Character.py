class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def combat(self, character):
        while self.health > 0 or character.health > 0:
            print(self.name + " attacks for " + str(self.strength) + " damage!")
            character.health -= self.strength
            if character.health <= 0:
                character.health = 0
                print(character.name + " died")
                break
            print(character.name + " has " + str(character.health) + " health left.")
            print(character.name + " attacks for " + str(character.strength) + " damage!")
            self.health -= character.strength
            if self.health <= 0:
                self.health = 0
                print(character.name + " died")
                break
            print(self.name + " has " + str(self.health) + " health left.")