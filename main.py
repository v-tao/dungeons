from modules.Character import Character
from modules.Maze import Maze
from modules.Item import Item
from modules.Tile import Tile
from random import randint
from enums.DEFAULT import Default
from enums.TILE_TYPES import TileTypes
# name = input("What is your character's name?\n")
# #PLAYER INIT
player = Character("name", Default.HEALTH.value, Default.STRENGTH.value)

#MAZE INIT
maze = Maze(Default.MAZE_WIDTH, Default.MAZE_HEIGHT)
maze.generate()
maze.populate()

while player.pos != (maze.height-2, maze.width-2) and not player.health <= 0:
    player.status()
    maze.print(player.pos)
    print("What direction would you like to move in?")
    for move in maze.legal_moves(player.pos):
        print(str(move.value) + " - " + str(move.name))
    choice = input()
    while choice not in [str(move.value) for move in maze.legal_moves(player.pos)]:
        print("Please pick a legal move")
        choice = input()
    player.pos = maze.new_position(player.pos, int(choice))
    if maze.check_combat(player.pos):
        combat_won = player.combat(maze.get_tile(player.pos).content)
        if combat_won:
            maze.set_tile(player.pos, Tile(TileTypes.EMPTY))
    if maze.check_item(player.pos):
        item = maze.get_tile(player.pos).content
        player.inventory.append(item)
        print("You have picked up the " + item.name)
        maze.set_tile(player.pos, Tile(TileTypes.EMPTY))
if player.pos == (maze.height-2, maze.width-2):
    print("You beat the maze!")
elif player.health <= 0:
    print("You died")