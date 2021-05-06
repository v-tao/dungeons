from modules.Character import Character
from modules.Maze import Maze
from modules.Item import Item
from random import randint
from enums.DEFAULT import Default

name = input("What is your character's name?\n")
player = Character(name, Default.HEALTH.value, Default.STRENGTH.value)
player.status()