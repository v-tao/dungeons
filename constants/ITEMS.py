from modules.Item import Item, Weapon, Armor, Potion
class Items
    ##### POTIONS #####
    SMALL_HEALTH_POTION = Potion("SMALL HEALTH POTION", 10, "Restores 10 HP.")
    MEDIUM_HEALTH_POTION = Potion("MEDIUM HEALTH POTION", 25, "Restores 25 HP.")
    LARGE_HEALTH_POTION = Potion("LARGE HEALTH POTION", 75, "Restores 75 HP.")
    
    ##### WEAPONS #####
    KNIFE = Weapon("KNIFE", 5, "A small attack knife. Deals 5 attack.")
    SWORD = Weapon("SWORD", 12, "A trustworthy sword. Deals 12 attack.")
    ALBERT_QI = Weapon("ALBERT QI", 100, "That's a lot of damage. Deals 100 attack.")