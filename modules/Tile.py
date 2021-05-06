class Tile:
    def __init__(self, category):
        self.category = category
        displays = {
            "empty" : "  ",
            "wall" : "▓▓",
            "character" : "CC",
            "item" : "II",
        }
        self.display = displays[category]