from random import randint
from Tile import Tile
from Tile import Wall
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
                maze_row.append("X")
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

    def generate_maze(self):
        #starting cell
        start_x = randint(0, self.width-1)
        start_y = (randint(0, self.height-1))
        self.blocked.remove((start_x, start_y))
        self.passage.append((start_x, start_y))
        self.maze[start_x][start_y] = " "
        self.add_frontiers((start_x, start_y))
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
    
    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in self.blocked:
                    self.maze[i][j] = "▓▓"
                else:
                    self.maze[i][j] = "  "
            print("".join(self.maze[i]))