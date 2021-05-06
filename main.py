from Character import Character
from Maze import Maze
from Item import Item
from random import randint
from DEFAULT import Default

name = input("What is your character's name?\n")
player = Character(name, Default.HEALTH.value, Default.STRENGTH.value)
player.status()