class Tile:
    def __init__(self, category, display):
        self.category = category

class Wall(Tile):
    def __init__(self):
        super(Wall, self).__init__("wall", "▓▓")