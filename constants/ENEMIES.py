from modules.Character import Character, Enemy
from constants.ITEMS import Items

class Enemies:
    IMP = Enemy("IMP", 20, 2, [Items.SMALL_HEALTH_POTION],level=1, strength=5)
    TROLL = Enemy("TROLL", 30, 5, [Items.MEDIUM_HEALTH_POTION], level=3, strength=10, defense=3)
    DRAGON = Enemy("DRAGON", 50, 20, [Items.CHAINMAIL_ARMOR], level=5, strength=20, defense=10)