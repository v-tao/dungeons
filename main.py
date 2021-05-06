from modules.Character import Character
from modules.Maze import Maze
from modules.Item import Item
from random import randint
from enums.DEFAULT import Default

# name = input("What is your character's name?\n")
# #PLAYER INIT
# player = Character(name, Default.HEALTH.value, Default.STRENGTH.value)
# player.status()

#MAZE INIT
maze = Maze(Default.MAZE_WIDTH, Default.MAZE_HEIGHT)
maze.generate()
maze.populate()
maze.print()