from random import randint
from modules.Tile import Tile
from modules.Item import Item
from modules.Character import Character
from enums.DEFAULT import Default
from enums.TILE_TYPES import TileTypes
from enums.ACTIONS import Actions
from enums.ITEM_TYPES import ItemTypes
from constants.ITEMS import Items

characters = []
items=[]

class Maze:
    def __init__(self, width, height, characters=characters, items=items):
        self.width = width
        self.height = height
        self.walls = []
        self.empty = []
        self.frontiers = []
        self.maze = []
        self.items = items
        self.characters = characters
        for i in range(height):
            maze_row = []
            for j in range(width):
                maze_row.append(Tile(TileTypes.WALL, (i, j)))
                self.walls.append((i, j))
            self.maze.append(maze_row)
    
    def is_legal(self, pos):
        if (pos[0] >= 0 and pos[0] < self. height
        and pos[1] >= 0 and pos[1] < self.width):
            return True
        else:
            return False
    
    def add_frontiers(self, pos):
        candidates = [(pos[0] + 2, pos[1]), (pos[0] - 2, pos[1]), 
        (pos[0], pos[1] + 2), (pos[0], pos[1] - 2)]
        for candidate in candidates:
            if self.is_legal(candidate) and candidate in self.walls and candidate not in self.frontiers:
                self.frontiers.append(candidate)
    
    def generate_neighbors(self, pos):
        neighbors = []
        candidates = [(pos[0] + 2, pos[1]), (pos[0] - 2, pos[1]), 
        (pos[0], pos[1] + 2), (pos[0], pos[1] - 2)]
        for candidate in candidates:
            if self.is_legal(candidate) and candidate not in self.walls:
                neighbors.append(candidate)
        return neighbors

    def generate_passages(self):
        #start from (1,1)
        self.walls.remove((1, 1))
        self.add_frontiers((1, 1))
        while self.frontiers:
            #random cell from list of frontier cells
            cell = self.frontiers[randint(0, len(self.frontiers)-1)]
            self.walls.remove(cell)
            #neighbors = all cells in distance 2 in state passage
            neighbors = self.generate_neighbors(cell)
            #pick random neighbor
            neighbor = neighbors[randint(0, len(neighbors)-1)]
            shift = (int((neighbor[0] - cell[0])/2), int((neighbor[1] - cell[1])/2))
            #turns in between cell into passage
            new_passage = (cell[0] + shift[0], cell[1] + shift[1])
            self.walls.remove(new_passage)
            #compute the frontier cells of the chosen frontier cell and add them to frontier list
            self.add_frontiers(cell)
            #remove the chosen frontier cell from the list of frontier cells
            self.frontiers.remove(cell)

    def generate(self):
        self.generate_passages()
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in self.walls:
                    self.maze[i][j] = Tile(TileTypes.WALL, (i, j))
                else:
                    self.empty.append((i, j))
                    self.maze[i][j] = Tile(TileTypes.EMPTY, (i, j))
        self.maze[-2][-2] = Tile(TileTypes.GOAL, (self.height-2, self.height-2))
    
    def populate(self):
        self.empty.remove((Default.POS_I.value, Default.POS_J.value))
        self.empty.remove((self.width-2, self.height-2))
        for character in self.characters:
            rand_pos = self.empty[randint(0, len(self.empty) - 1)]
            self.maze[rand_pos[0]][rand_pos[1]].update_tile(character, TileTypes.CHARACTER)
            self.empty.remove(rand_pos)
        for item in self.items:
            rand_pos = self.empty[randint(0, len(self.empty) - 1)]
            self.maze[rand_pos[0]][rand_pos[1]].update_tile(item, TileTypes.ITEM)
            self.empty.remove(rand_pos)

    def print(self, player_pos):
        maze_display = [[tile.get_display() for tile in row] for row in self.maze]
        maze_display[player_pos[0]][player_pos[1]] = " P "
        for i in range(len(maze_display)):
            print("".join(maze_display[i]))
        print("")

    def legal_actions(self, pos):
        directions = {
            (pos[0] - 1, pos[1]) : Actions.MOVE_NORTH,
            (pos[0], pos[1] + 1) : Actions.MOVE_EAST,
            (pos[0] + 1, pos[1]) : Actions.MOVE_SOUTH,
            (pos[0], pos[1] - 1) : Actions.MOVE_WEST,
        }
        actions = [Actions.CHECK_STATUS, Actions.CHECK_INVENTORY]
        for direction in directions:
            if self.is_legal(direction) and direction not in self.walls:
                actions.append(directions[direction])
        return actions
    
    def get_tile(self, pos):
        return self.maze[pos[0]][pos[1]]

    def set_tile(self, pos, tile):
        self.maze[pos[0]][pos[1]] = tile

    def check_combat(self, pos):
        return True if self.get_tile(pos).category == TileTypes.CHARACTER else False

    def check_item(self, pos):
        return True if self.get_tile(pos).category == TileTypes.ITEM else False

    def new_position(self, pos, move):
        new_pos = pos
        if move == Actions.MOVE_EAST.value:
            new_pos = (new_pos[0], new_pos[1] + 1)
            while ((new_pos[0], new_pos[1] + 1) not in self.walls 
            and (new_pos[0] + 1, new_pos[1]) in self.walls
            and (new_pos[0] - 1, new_pos[1]) in self.walls
            and self.maze[new_pos[0]][new_pos[1]].category == TileTypes.EMPTY):
                new_pos = (new_pos[0], new_pos[1] + 1)
        elif move == Actions.MOVE_WEST.value:
            new_pos = (new_pos[0], new_pos[1] - 1)
            while ((new_pos[0], new_pos[1] - 1) not in self.walls 
            and (new_pos[0] + 1, new_pos[1]) in self.walls
            and (new_pos[0] - 1, new_pos[1]) in self.walls
            and self.maze[new_pos[0]][new_pos[1]].category == TileTypes.EMPTY):
                new_pos = (new_pos[0], new_pos[1] - 1)
        elif move == Actions.MOVE_NORTH.value:
            new_pos = (new_pos[0] - 1, new_pos[1])
            while ((new_pos[0] - 1, new_pos[1]) not in self.walls 
            and (new_pos[0], new_pos[1] + 1) in self.walls
            and (new_pos[0], new_pos[1] - 1) in self.walls
            and self.maze[new_pos[0]][new_pos[1]].category == TileTypes.EMPTY):
                new_pos = (new_pos[0] - 1, new_pos[1])
        elif move == Actions.MOVE_SOUTH.value:
            new_pos = (new_pos[0] + 1, new_pos[1])
            while ((new_pos[0] + 1, new_pos[1]) not in self.walls 
            and (new_pos[0], new_pos[1] + 1) in self.walls
            and (new_pos[0], new_pos[1] - 1) in self.walls
            and self.maze[new_pos[0]][new_pos[1]].category == TileTypes.EMPTY):
                new_pos = (new_pos[0] + 1, new_pos[1])
        return new_pos