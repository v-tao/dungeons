from enums.TILE_TYPES import TileTypes
class Tile:
    def __init__(self, category, coordinate):
        self.category = category
        displays = {
            TileTypes.WALL : "▓▓▓",
            TileTypes.PLAYER : " P ",
            TileTypes.GOAL : " ★ ",
            TileTypes.EMPTY : "   ",
            TileTypes.CHARACTER: " C ",
            TileTypes.ITEM: " I "
        }
        self.display = displays[category]
    
    def get_display(self):
        return self.display