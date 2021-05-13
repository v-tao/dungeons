from modules.Item import Item, Weapon, Armor, Potion
class Items:
    ##### POTIONS #####
    SMALL_HEALTH_POTION = Potion("SMALL HEALTH POTION", 10, "Restores 10 HP.")
    MEDIUM_HEALTH_POTION = Potion("MEDIUM HEALTH POTION", 25, "Restores 25 HP.")
    LARGE_HEALTH_POTION = Potion("LARGE HEALTH POTION", 75, "Restores 75 HP.")
    
    ##### WEAPONS #####
    NONE_WEAPON = Weapon("None", 0, "None.")
    KNIFE = Weapon("KNIFE", 5, "2 attack. A small attack knife.")
    SWORD = Weapon("SWORD", 12, "12 attack. A trustworthy sword.")
    ALBERT_QI = Weapon("ALBERT QI", 100, "100 attack. That's a lot of damage.")

    ##### ARMOR #####
    NONE_ARMOR = Armor("None", 0, "None.")
    LEATHER_ARMOR = Armor("LEATHER ARMOR", 5, "5 defense. Flimsy armor.")
    CHAINMAIL_ARMOR = Armor("CHAINMAIL ARMOR", 12, "12 defense. Armor made from chains.")
    ALBERT_QI = Armor("ALBERT QI", 100, "100 defense. Will guard you from all harm")