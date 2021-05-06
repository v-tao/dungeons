from enums.TILE_TYPES import TileTypes
class Tile:
    def __init__(self, category, content=None):
        self.category = category
        self.content = content
        self.displays = {
            TileTypes.WALL : "▓▓▓",
            TileTypes.PLAYER : " P ",
            TileTypes.GOAL : " ★ ",
            TileTypes.EMPTY : "   ",
            TileTypes.CHARACTER: " C ",
            TileTypes.ITEM: " I "
        }
        self.display = self.displays[category]

    def get_display(self):
        return self.display

    def update_tile(self, content, category):
        self.content = content
        self.category = category
        self.display = self.displays[category]