from enums.DEFAULT import Default
from constants.ITEMS import Items
from math import floor,log
from random import choice

class Character:
    def __init__(self, name, max_health, level=Default.LEVEL.value, strength=Default.STRENGTH.value, defense=Default.DEFENSE.value, 
        weapon=Items.NONE_WEAPON, armor=Items.NONE_ARMOR):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.level = level
        self.level_up_xp = floor(10 * log(self.level + 1))
        self.xp = 0
        self.pos = (Default.POS_I.value, Default.POS_J.value)
        self.inventory = []
        self.strength = strength
        self.defense = defense
        self.weapon = weapon
        self.armor = armor
    
    def check_level_up(self):
        # xp to level up is 10ln(level + 1)
        if self.xp >= self.level_up_xp:
            self.level += 1
            self.xp = self.xp - self.level_up_xp
            self.level_up_xp = floor(10 * log(self.level + 1))
            print("You have leveled up to level " + str(self.level) + ".")

    #returns True if win
    def combat(self, enemy):
        print("You encountered " + enemy.name + ".")
        while self.health > 0 and enemy.health > 0:
            damage_dealt = (1 + floor(0.5 * log(self.level))) * (self.strength + self.weapon.attack) - enemy.armor.defense - enemy.defense
            damage_received = (1 + floor(0.5 * log(enemy.level))) * (enemy.strength + enemy.weapon.attack) - self.armor.defense - self.defense
            enemy.health -= damage_dealt if damage_dealt > 0 else 0
            if enemy.health <= 0:
                print(enemy.name + " died")
                print("You have " + str(self.health) + " HP remaining.")
                # pick up loot 
                loot = choice(enemy.loot_table)
                self.inventory.append(loot)
                print("You have picked up a " + loot.name + ".")
                # gain xp
                self.xp += enemy.xp_reward
                print("You have gained " + str(enemy.xp_reward) + " XP.")
                self.check_level_up()
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
        print("LEVEL: " + str(self.level))
        print("XP: " + str(self.xp) + "/" + str(self.level_up_xp))
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

class Enemy(Character):
    def __init__(self, name, health, xp_reward, loot_table, level=Default.LEVEL, strength=Default.STRENGTH, defense=Default.DEFENSE,
        weapon=Items.NONE_WEAPON, armor=Items.NONE_ARMOR):
        super(Enemy, self).__init__(name, health, level, strength, defense, weapon, armor)
        self.xp_reward = xp_reward
        self.loot_table = loot_table