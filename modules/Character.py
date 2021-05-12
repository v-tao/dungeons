from enums.DEFAULT import Default
from constants.ITEMS import Items

class Character:
    def __init__(self, name, health, strength=Default.STRENGTH, defense=Default.DEFENSE, 
        weapon=Items.NONE_WEAPON, armor=Items.NONE_ARMOR):
        self.name = name
        self.health = health
        self.pos = (Default.POS_I.value, Default.POS_J.value)
        self.inventory = []
        self.strength = strength
        self.defense = defense
        self.weapon = weapon
        self.armor = armor
    
    #returns True if win
    def combat(self, character):
        while self.health > 0 or character.health > 0:
            #each attack is the strength of the character + strength of the weapon
            character.health -= (self.strength + self.weapon.attack - character.armor.defense - character.defense)
            if character.health <= 0:
                character.health = 0
                print(character.name + " died")
                return True
            self.health -= (character.strength + character.weapon.attack - self.armor.defense - self.defense)
            if self.health <= 0:
                self.health = 0
                print(character.name + " died")
                return False
    
    def equip_weapon(self, weapon):
        if self.weapon:
            self.inventory.append(self.weapon)
        self.weapon = weapon
        self.inventory.remove(weapon)
        print(weapon.name + " has been equipped.\n")
    
    def equip_armor(self, armor):
        if self.armor:
            self.inventory.append(self.armor)
        self.armor = armor
        self.inventory.remove(armor)
        print(armor.name + " has been equipped")

    def print_status(self):
        print("\n" + self.name)
        print("HEALTH: " + str(self.health))
        print("WEAPON: " + self.weapon.name + " - " + self.weapon.description)
        print("ARMOR: " + self.armor.name + " - " + self.armor.description + "\n")
    
    def print_inventory(self):
        print("\n===== INVENTORY =====")
        if not self.inventory:
            print("You have no items in your inventory\n")
        else: 
            for i, item in enumerate(self.inventory):
                print(str(i + 1) + " - " + item.name)
            print(" ")