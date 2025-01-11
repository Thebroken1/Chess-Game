


class Sqr: #intializing the squares

    def __init__(self,rows,cols,piece = None):
        self.rows = rows
        self.cols = cols
        self.piece = piece

    def has_piece(self):
        return self.piece != None
