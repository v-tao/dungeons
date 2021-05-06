from modules.Character import Character
from modules.Maze import Maze
from modules.Item import Item
from random import randint
from enums.DEFAULT import Default

# name = input("What is your character's name?\n")
# #PLAYER INIT
player = Character("name", Default.HEALTH.value, Default.STRENGTH.value)

#MAZE INIT
maze = Maze(Default.MAZE_WIDTH, Default.MAZE_HEIGHT)
maze.generate()
maze.populate()
maze.print()
print(maze.legal_moves(player.pos))

# while player.pos != (maze.height-2, maze.width-2):
    
    