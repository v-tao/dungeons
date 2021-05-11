from modules.Character import Character
from modules.Maze import Maze
from modules.Item import Item
from modules.Tile import Tile
from random import randint
from enums.DEFAULT import Default
from enums.TILE_TYPES import TileTypes
from enums.ACTIONS import Actions
from constants.ITEMS import Items
# name = input("What is your character's name?\n")
# #PLAYER INIT
player = Character("name", Default.HEALTH.value, Default.STRENGTH.value)

items = [Items.SMALL_HEALTH_POTION, Items.MEDIUM_HEALTH_POTION, Items.LARGE_HEALTH_POTION]

#MAZE INIT
maze = Maze(Default.MAZE_WIDTH, Default.MAZE_HEIGHT, characters=[], items=items)
maze.generate()
maze.populate()

player.print_status()
maze.print(player.pos)

while player.pos != (maze.height-2, maze.width-2) and not player.health <= 0:
    print("What action will you take?")
    for action in Actions:
        print(str(action.value) + " - " + str(action.name).replace("_", " "))
    choice = input()
    while choice not in [str(move.value) for move in maze.legal_actions(player.pos)]:
        print("Please pick a legal move")
        choice = input()
    if int(choice) == Actions.CHECK_STATUS.value:
        player.print_status()
    elif int(choice) == Actions.CHECK_INVENTORY.value:
        player.print_inventory()
    else:
        player.pos = maze.new_position(player.pos, int(choice))
        if maze.check_combat(player.pos):
            combat_won = player.combat(maze.get_tile(player.pos).content)
            if combat_won:
                maze.set_tile(player.pos, Tile(TileTypes.EMPTY))
        if maze.check_item(player.pos):
            item = maze.get_tile(player.pos).content
            player.inventory.append(item)
            print("\nYou have picked up the " + item.name + "\n")
            maze.set_tile(player.pos, Tile(TileTypes.EMPTY))
        maze.print(player.pos)
if player.pos == (maze.height-2, maze.width-2):
    print("You beat the maze!")
elif player.health <= 0:
    print("You died")