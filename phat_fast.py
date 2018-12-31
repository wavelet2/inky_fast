from . import inky_fast


class InkyPHATFast(inky_fast.InkyFast):
    WIDTH = 212
    HEIGHT = 104

    WHITE = 0
    BLACK = 1
    RED = 2
    YELLOW = 2

    def __init__(self, colour):
        inky_fast.InkyFast.__init__(
            self,
            resolution=(self.WIDTH, self.HEIGHT),
            colour=colour,
            h_flip=False,
            v_flip=False)
