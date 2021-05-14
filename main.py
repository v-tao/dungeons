from modules.Character import Character
from modules.Maze import Maze
from modules.Item import Item
from modules.Tile import Tile
from enums.DEFAULT import Default
from enums.TILE_TYPES import TileTypes
from enums.ACTIONS import Actions
from constants.ITEMS import Items
from constants.ENEMIES import Enemies

# PLAYER INIT
name = input("What is your character's name?\n")
player = Character(name, Default.HEALTH.value, weapon=Items.KNIFE, armor=Items.LEATHER_ARMOR)

items = [Items.SMALL_HEALTH_POTION, Items.MEDIUM_HEALTH_POTION, Items.LARGE_HEALTH_POTION,
        Items.KNIFE, Items.SWORD, Items.ALBERT_QI,
        Items.LEATHER_ARMOR, Items.CHAINMAIL_ARMOR, Items.ALBERT_QI]

enemies = [Enemies.IMP, Enemies.TROLL, Enemies.DRAGON]

level = 0

def combat():
    combat_won = player.combat(maze.get_tile(player.pos).content)
    if combat_won:
        maze.set_tile(player.pos, Tile(TileTypes.EMPTY))

def pick_up_item():
    item = maze.get_tile(player.pos).content
    player.inventory.append(item)
    print("\nYou have picked up the " + item.name + "\n")
    maze.set_tile(player.pos, Tile(TileTypes.EMPTY))

def check_inventory():
    player.print_inventory()
    if player.inventory:
        item = input("What item would you like to inspect? Enter 0 to go back\n")
        while item not in [str(i) for i in range(len(player.inventory) + 1)]:
            item = input("Please enter a valid input\n")
        print("")
        if int(item) != 0:
            print("===== " + player.inventory[int(item)-1].name + " =====")
            print(player.inventory[int(item)-1].description + "\n")
            choice = input("What would you like to do?\n0 - GO BACK\n1 - USE ITEM\n2 - DISCARD ITEM\n")
            while choice not in [str(i) for i in range(3)]:
                choice = input("Please enter a valid input\n")
            if int(choice) == Actions.USE_ITEM:
                player.inventory[int(item)-1].use(player)
            elif int(choice) == Actions.DISCARD_ITEM:
                print(player.inventory[int(item)-1].name + " has been discarded.\n")
                player.inventory.pop(int(item)-1)
# MAZE INIT
maze = Maze(Default.MAZE_WIDTH, Default.MAZE_HEIGHT, enemies=enemies, items=items)
maze.generate()
maze.populate()
player.print_status()
maze.print(player.pos)
while not player.health <= 0:
    level += 1
    while player.pos != (maze.height-2, maze.width-2) and player.health > 0:
        print("What action will you take?")
        for action in Actions:
            print(str(action.value) + " - " + str(action.name).replace("_", " "))
        choice = input()
        while choice not in [str(move.value) for move in maze.legal_actions(player.pos)]:
            choice = input("Please pick a legal move\n")
        if int(choice) == Actions.CHECK_STATUS.value:
            player.print_status()
        elif int(choice) == Actions.CHECK_INVENTORY.value:
            check_inventory()
        elif int(choice) == Actions.DISPLAY_MAZE:
            maze.print(player.pos)
        else:
            player.pos = maze.new_position(player.pos, int(choice))
            if maze.check_combat(player.pos):
                combat()
            if maze.check_item(player.pos):
                pick_up_item()
            maze.print(player.pos)
    if player.pos == (maze.height-2, maze.width-2) and player.health > 0:
        print("You have completed level " + str(level) + ".")
        maze = Maze(maze.width + 2, maze.height + 2, enemies=enemies, items=items)
        player.pos = (1,1)
        player.max_health += 25
        player.health += 25
        print("Your max health has been raised by 25 HP.")
        maze.generate()
        maze.populate()
        player.print_status()
        maze.print(player.pos)
print("You died. You reached level " + str(level) + ".")