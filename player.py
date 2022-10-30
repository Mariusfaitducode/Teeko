from constante import *


class Player:

    def __init__(self, grid, token):

        self.list_pieces = []
        self.token = token

        for l in range(NB_LINE):
            for c in range(NB_COLUMN):

                if grid[l][c] == self.token:
                    self.list_pieces.append((l, c))










