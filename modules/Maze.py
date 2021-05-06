from random import randint
from modules.Tile import Tile
from enums.TILE_TYPES import TileTypes

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.blocked = []
        self.passage = []
        self.frontiers = []
        self.maze = []
        for i in range(height):
            maze_row = []
            for j in range(width):
                maze_row.append(Tile(TileTypes.WALL, (i, j)))
                self.blocked.append((i, j))
            self.maze.append(maze_row)
    
    def is_legal(self, coordinate):
        if (coordinate[0] >= 0 and coordinate[0] < self. height
        and coordinate[1] >= 0 and coordinate[1] < self.width):
            return coordinate
        else:
            return False
    
    def add_frontiers(self, coordinate):
        candidates = [(coordinate[0] + 2, coordinate[1]), (coordinate[0] - 2, coordinate[1]), 
        (coordinate[0], coordinate[1] + 2), (coordinate[0], coordinate[1] - 2)]
        for candidate in candidates:
            if self.is_legal(candidate) and candidate in self.blocked and candidate not in self.frontiers:
                self.frontiers.append(candidate)
    
    def generate_neighbors(self, coordinate):
        neighbors = []
        candidates = [(coordinate[0] + 2, coordinate[1]), (coordinate[0] - 2, coordinate[1]), 
        (coordinate[0], coordinate[1] + 2), (coordinate[0], coordinate[1] - 2)]
        for candidate in candidates:
            if self.is_legal(candidate) and candidate not in self.blocked:
                neighbors.append(candidate)
        return neighbors

    def generate_coordinates(self):
        #start from (1,1)
        self.blocked.remove((1, 1))
        self.passage.append((1, 1))
        self.add_frontiers((1, 1))
        i = 0
        while self.frontiers:
            #random cell from list of frontier cells
            cell = self.frontiers[randint(0, len(self.frontiers)-1)]
            self.blocked.remove(cell)
            #neighbors = all cells in distance 2 in state passage
            neighbors = self.generate_neighbors(cell)
            #pick random neighbor
            neighbor = neighbors[randint(0, len(neighbors)-1)]
            shift = (int((neighbor[0] - cell[0])/2), int((neighbor[1] - cell[1])/2))
            #turns in between cell into passage
            new_passage = (cell[0] + shift[0], cell[1] + shift[1])
            self.blocked.remove(new_passage)
            #compute the frontier cells of the chosen frontier cell and add them to frontier list
            self.add_frontiers(cell)
            #remove the chosen frontier cell from the list of frontier cells
            self.frontiers.remove(cell)
            i += 1
    
    def generate_maze(self):
        self.generate_coordinates()
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in self.blocked:
                    self.maze[i][j] = Tile(TileTypes.WALL, (i, j))
                else:
                    self.maze[i][j] = Tile(TileTypes.EMPTY, (i, j))
        self.maze[-2][-2] = Tile(TileTypes.GOAL, (i, j))
    
    def print(self):
        maze_display = [(tile.get_display() for tile in row) for row in self.maze]
        for i in range(len(maze_display)):
            print("".join(maze_display[i]))