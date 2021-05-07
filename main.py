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
maze.print(player.pos)

while player.pos != (maze.height-2, maze.width-2):
    print("What direction would you like to move in?")
    for move in maze.legal_moves(player.pos):
        print(str(move.value) + " - " + str(move.name))
    choice = input()
    while int(choice) not in [move.value for move in maze.legal_moves(player.pos)]:
        print("Please pick a legal move")
        choice = input()
    player.pos = maze.new_position(player.pos, int(choice))
    maze.print(player.pos)
print("You solved the maze!")