from enums.DEFAULT import Default
from constants.ITEMS import Items

class Character:
    def __init__(self, name, max_health, strength=Default.STRENGTH, defense=Default.DEFENSE, 
        weapon=Items.NONE_WEAPON, armor=Items.NONE_ARMOR):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.pos = (Default.POS_I.value, Default.POS_J.value)
        self.inventory = []
        self.strength = strength
        self.defense = defense
        self.weapon = weapon
        self.armor = armor
    
    #returns True if win
    def combat(self, character):
        print("You encountered " + character.name + ".")
        while self.health > 0 and character.health > 0:
            damage_dealt = self.strength + self.weapon.attack - character.armor.defense - character.defense
            damage_received = character.strength + character.weapon.attack - self.armor.defense - self.defense
            character.health -= damage_dealt if damage_dealt > 0 else 0
            if character.health <= 0:
                print(character.name + " died")
                print("You have " + str(self.health) + " HP remaining.")
                return True
            self.health -= damage_received if damage_received > 0 else 0
            if self.health <= 0:
                print("You died.")
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
            print("Your inventory is empty.\n")
        else: 
            for i, item in enumerate(self.inventory):
                print(str(i + 1) + " - " + item.name)
            print(" ")