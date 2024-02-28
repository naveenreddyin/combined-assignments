class Plateau(object):
    def __init__(self, width, height, min_width=0, min_height=0):
        self.width = width
        self.height = height
        self.min_width = min_width
        self.min_height = min_height

    def can_move(self, position):
        return (
            self.min_height <= position.x <= self.width
            and self.min_height <= position.y <= self.height
        )
