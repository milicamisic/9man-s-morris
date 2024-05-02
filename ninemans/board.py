#AI IS BLACK AND MINIMIZER

from .piece import Piece
from .hashmap import ChainedHashMap

class Board(object):

    def __init__(self):
        # ovako tabla izgleda iznutra
        self.board = [[None, None, None, None, None, None, None, None, None],
                      [None, "(1,1)", "/", "/", "(1,4)", "/", "/", "(1,7)", None],
                      [None, "/", "(2,2)", "/", "(2,4)", "/", "(2,6)", "/", None],
                      [None, "/", "/", "(3,3)", "(3,4)", "(3,5)", "/", "/", None],
                      [None, "(4,1)", "(4,2)", "(4,3)", None, "(4,5)", "(4,6)", "(4,7)", None],
                      [None, "/", "/", "(5,3)", "(5,4)", "(5,5)", "/", "/", None],
                      [None, "/", "(6,2)", "/", "(6,4)", "/", "(6,6)", "/", None],
                      [None, "(7,1)", "/", "/", "(7,4)", "/", "/", "(7,7)", None],
                      [None, None, None, None, None, None, None, None, None]]

        self.white_pieces = 0
        self.black_pieces = 0
        self.white_mills = 0
        self.black_mills = 0
        # 0 = is not a mill piece, 1 = is mill piece
        self.is_mill_table = {"(1,1)" : 0, "(1,4)" : 0, "(1,7)" : 0,
                              "(2,2)" : 0, "(2,4)" : 0, "(2,6)" : 0,
                              "(3,3)" : 0, "(3,4)" : 0, "(3,5)" : 0,
                              "(4,1)" : 0, "(4,2)" : 0, "(4,3)" : 0, "(4,5)" : 0, "(4,6)" : 0, "(4,7)" : 0,
                              "(5,3)" : 0, "(5,4)" : 0, "(5,5)" : 0,
                              "(6,2)" : 0, "(6,4)" : 0, "(6,6)" : 0,
                              "(7,1)" : 0, "(7,4)" : 0, "(7,7)" : 0}

    def print_board(self):
        x = self.board
        # ovako tabla izgleda korisniku
        print("%5s--------------------------%5s--------------------------%5s\n"
              "  |                              |                              |  \n"
              "  |                              |                              |  \n"
              "  |                              |                              |  \n"
              "  |                              |                              |  \n"
              "  |                              |                              |  \n"
              "  |          %5s-------------%5s-------------%5s          |  \n"
              "  |            |                 |                 |            |  \n"
              "  |            |                 |                 |            |  \n"
              "  |            |                 |                 |            |  \n"
              "  |            |      %5s----%5s----%5s      |            |  \n"
              "  |            |        |                 |        |            |  \n"
              "  |            |        |                 |        |            |  \n"
              "  |            |        |                 |        |            |  \n"
              "%5s--------%5s----%5s             %5s----%5s--------%5s\n"
              "  |            |        |                 |        |            |  \n"
              "  |            |        |                 |        |            |  \n"
              "  |            |        |                 |        |            |  \n"
              "  |            |      %5s----%5s----%5s      |            |  \n"
              "  |            |                 |                 |            |  \n"
              "  |            |                 |                 |            |  \n"
              "  |            |                 |                 |            |  \n"
              "  |          %5s-------------%5s-------------%5s          |  \n"
              "  |                              |                              |  \n"
              "  |                              |                              |  \n"
              "  |                              |                              |  \n"
              "  |                              |                              |  \n"
              "  |                              |                              |  \n"
              "%5s--------------------------%5s--------------------------%5s" % (x[1][1], x[1][4], x[1][7], 
                                                                                 x[2][2], x[2][4], x[2][6],
                                                                                 x[3][3], x[3][4], x[3][5],
                                                                                 x[4][1], x[4][2], x[4][3],x[4][5], x[4][6], x[4][7],
                                                                                 x[5][3], x[5][4], x[5][5],
                                                                                 x[6][2], x[6][4], x[6][6],
                                                                                 x[7][1], x[7][4], x[7][7],))

    #available positions in phase1
    def get_available_positions1(self):
        available_positions = []
        for x in range(1, 9):
            for y in range(1, 9):
                if self.board[x][y] != None and self.board[x][y].startswith("("):
                    cords = "(" + str(x) +"," + str(y) + ")"
                    available_positions.append(cords)

        return available_positions

    #available positions in phase2
    def get_available_positions2(self,turn):
        available_positions = []
        for x in range(1, 9):
            for y in range(1,9):
                # for each position that is player color we check where can it move
                if self.board[x][y] == turn:
                    firstX = x
                    firstY = y

                    while self.board[x+1][y] == "/":
                        x += 1
                    if self.board[x+1][y] != None and self.board[x+1][y].startswith("("):
                        if self.board[x+1][y] not in available_positions:
                            available_positions.append(self.board[x+1][y])

                    x = firstX

                    while self.board[x-1][y] == "/":
                        x -= 1
                    if self.board[x-1][y] != None and self.board[x-1][y].startswith("("):
                        if self.board[x-1][y] not in available_positions:
                            available_positions.append(self.board[x-1][y])

                    x = firstX

                    while self.board[x][y+1] == "/":
                        y += 1
                    if self.board[x][y+1] != None and self.board[x][y+1].startswith("("):
                        if self.board[x][y+1] not in available_positions:
                            available_positions.append(self.board[x][y+1])

                    y = firstY

                    while self.board[x][y-1] == "/":
                        y -= 1
                    if self.board[x][y-1] != None and self.board[x][y-1].startswith("("):
                        if self.board[x][y-1] not in available_positions:
                            available_positions.append(self.board[x][y-1])

                    y = firstY
        
        if available_positions == []:
            return False
        
        return available_positions

    def get_available_positions_piece(self, turn, x, y):
        available_positions = []
        
        if self.board[x][y] == turn:
            firstX = x
            firstY = y

            while self.board[x+1][y] == "/":
                x += 1
            if self.board[x+1][y] != None and self.board[x+1][y].startswith("("):
                if self.board[x+1][y] not in available_positions:
                    available_positions.append(self.board[x+1][y])

            x = firstX

            while self.board[x-1][y] == "/":
                x -= 1
            if self.board[x-1][y] != None and self.board[x-1][y].startswith("("):
                if self.board[x-1][y] not in available_positions:
                    available_positions.append(self.board[x-1][y])

            x = firstX

            while self.board[x][y+1] == "/":
                y += 1
            if self.board[x][y+1] != None and self.board[x][y+1].startswith("("):
                if self.board[x][y+1] not in available_positions:
                    available_positions.append(self.board[x][y+1])

            y = firstY

            while self.board[x][y-1] == "/":
                y -= 1
            if self.board[x][y-1] != None and self.board[x][y-1].startswith("("):
                if self.board[x][y-1] not in available_positions:
                    available_positions.append(self.board[x][y-1])

            y = firstY

        if available_positions == []:
            return False

        return available_positions
        
    def add_piece(self, x, y, turn):
        if self.board[x][y] != None and self.board[x][y].startswith("("):
            self.board[x][y] = turn
            if turn == "WHITE":
                self.white_pieces += 1
            else:
                self.black_pieces += 1
           
            return True
        return False

    def move_piece(self, oldX, oldY, newX, newY, turn):
        available_positions = self.get_available_positions_piece(turn, oldX, oldY)
        if self.board[oldX][oldY] == turn and self.board[newX][newY] in available_positions:
            self.board[oldX][oldY] = "(" + str(oldX) + "," + str(oldY) + ")"
            self.board[newX][newY] = turn

            self.mill_undone(oldX, oldY, turn)

            return True
        return False

    def remove_piece(self, x, y, turn):
        if turn == "WHITE":
                can_eat = "BLACK"
        else:
                can_eat = "WHITE"

        non_mill_pieces = self.get_non_mill_pieces(turn)
        cords = "(" + str(x) +"," + str(y) + ")"

        if (non_mill_pieces == []) or (non_mill_pieces != [] and self.is_mill_table[cords] == 0) and self.board[x][y] == can_eat:
            self.board[x][y] = "(" + str(x) + "," + str(y) + ")"
            if turn == "WHITE":
                self.black_pieces -= 1
            else:
                self.white_pieces -= 1

            self.mill_undone(x,y,turn)
            return True

        return False

    def get_non_mill_pieces(self, turn):
        non_mill_positions = []
        for x in range(1, 8):
            for y in range(1, 8):
                cords = "(" + str(x) +"," + str(y) + ")"

                if self.board[x][y] == "WHITE" and turn=="BLACK" and self.is_mill_table[cords] == 0:
                    non_mill_positions.append(cords)

                elif self.board[x][y] == "BLACK" and turn=="WHITE" and self.is_mill_table[cords] == 0:
                    non_mill_positions.append(cords)

        return non_mill_positions

    def mill_created(self, x, y, turn, doubleCheck = None):
        piece = Piece(x, y, turn)

        # checking if our added or moved piece is first
        if self.board[x-1][y] == None or (self.board[x-1][y] == "/" and self.board[x-2][y] == None) or (self.board[x-2][y] == "/" and self.board[x-3][y] == None):
            first = self.board[x][y]

            while self.board[x+1][y] == "/":
                x += 1
            second = x + 1

            while self.board[x+2][y] == "/":
                x += 1
            third = x + 2

            x = piece.x

            if self.board[second][y] == turn and self.board[third][y] == turn:
                cords = "(" + str(x) +"," + str(y) + ")"
                self.is_mill_table[cords] = 1

                cords = "(" + str(second) +"," + str(y) + ")"
                self.is_mill_table[cords] = 1

                cords = "(" + str(third) +"," + str(y) + ")"
                self.is_mill_table[cords] = 1

                if turn == "WHITE" and doubleCheck == None:
                    self.white_mills += 1
                else:
                    self.black_mills += 1

                return True

        # checking if our added or moved piece is last
        elif self.board[x+1][y] == None or (self.board[x+1][y] == "/" and self.board[x+2][y] == None) or (self.board[x+2][y] == "/" and self.board[x+3][y] == None):
            third = self.board[x][y]

            while self.board[x-1][y] == "/":
                x -= 1
            second = x - 1

            while self.board[x-2][y] == "/":
                x -= 1
            first = x - 2

            x = piece.x

            if self.board[second][y] == turn and self.board[first][y] == turn:
                cords = "(" + str(x) +"," + str(y) + ")"
                self.is_mill_table[cords] = 1

                cords = "(" + str(second) +"," + str(y) + ")"
                self.is_mill_table[cords] = 1

                cords = "(" + str(first) +"," + str(y) + ")"
                self.is_mill_table[cords] = 1

                if turn == "WHITE" and doubleCheck == None:
                    self.white_mills += 1
                else:
                    self.black_mills += 1

                return True


        # if it isn't first or last that means it's in the middle
        else:
            while self.board[x+1][y] == "/":
                x += 1
            to_the_rightX = x + 1

            x = piece.x

            while self.board[x-1][y] == "/":
                x -= 1
            to_the_leftX = x - 1

            x = piece.x

            if self.board[to_the_rightX][y] == turn and self.board[to_the_leftX][y] == turn:
                cords = "(" + str(x) +"," + str(y) + ")"
                self.is_mill_table[cords] = 1

                cords = "(" + str(to_the_rightX) +"," + str(y) + ")"
                self.is_mill_table[cords] = 1

                cords = "(" + str(to_the_leftX) +"," + str(y) + ")"
                self.is_mill_table[cords] = 1

                if turn == "WHITE" and doubleCheck == None:
                    self.white_mills += 1
                else:
                    self.black_mills += 1
                
                return True

        # now checking the left-right direction
        # checking if our added or moved piece is first
        if self.board[x][y-1] == None or (self.board[x][y-1] == "/" and self.board[x][y-2] == None) or (self.board[x][y-2] == "/" and self.board[x][y-3] == None):
            first = self.board[x][y]

            while self.board[x][y+1] == "/":
                y += 1
            second = y + 1

            while self.board[x][y+2] == "/":
                y += 1
            third = y + 2

            y = piece.y

            if self.board[x][second] == turn and self.board[x][third] == turn:
                cords = "(" + str(x) +"," + str(y) + ")"
                self.is_mill_table[cords] = 1

                cords = "(" + str(x) +"," + str(second) + ")"
                self.is_mill_table[cords] = 1

                cords = "(" + str(x) +"," + str(third) + ")"
                self.is_mill_table[cords] = 1

                if turn == "WHITE" and doubleCheck == None:
                    self.white_mills += 1
                else:
                    self.black_mills += 1

                return True

        # checking if our added or moved piece is last
        elif self.board[x][y+1] == None or (self.board[x][y+1] == "/" and self.board[x][y+2] == None) or (self.board[x][y+2] == "/" and self.board[x][y+3] == None):
            third = self.board[x][y]

            while self.board[x][y-1] == "/":
                y -= 1
            second = y - 1

            while self.board[x][y-2] == "/":
                y -= 1
            first = y - 2

            y = piece.y

            if self.board[x][second] == turn and self.board[x][first] == turn:
                cords = "(" + str(x) +"," + str(y) + ")"
                self.is_mill_table[cords] = 1

                cords = "(" + str(x) +"," + str(second) + ")"
                self.is_mill_table[cords] = 1

                cords = "(" + str(x) +"," + str(first) + ")"
                self.is_mill_table[cords] = 1

                if turn == "WHITE" and doubleCheck == None:
                    self.white_mills += 1
                else:
                    self.black_mills += 1

                return True

        # if it isn't first or last that means it's in the middle
        else:
            while self.board[x][y+1] == "/":
                y += 1
            to_the_rightY = y + 1

            y = piece.y

            while self.board[x][y-1] == "/":
                y -= 1
            to_the_leftY = y - 1

            y = piece.y

            if self.board[x][to_the_rightY] == turn and self.board[x][to_the_leftY] == turn:
                cords = "(" + str(x) +"," + str(y) + ")"
                self.is_mill_table[cords] = 1

                cords = "(" + str(x) +"," + str(to_the_rightY) + ")"
                self.is_mill_table[cords] = 1

                cords = "(" + str(x) +"," + str(to_the_leftY) + ")"
                self.is_mill_table[cords] = 1

                if turn == "WHITE" and doubleCheck == None:
                    self.white_mills += 1
                else:
                    self.black_mills += 1

                return True

        return False

    def mill_undone(self, x, y, turn):
        piece = Piece(x, y, turn)
        cords = "(" + str(x) + "," + str(y) + ")"
        if self.is_mill_table[cords] == 1:
            # was it an up-down mill?
            # checking if our added or moved piece is first
            if self.board[x-1][y] == None or (self.board[x-1][y] == "/" and self.board[x-2][y] == None) or (self.board[x-2][y] == "/" and self.board[x-3][y] == None):
                first = self.board[x][y]

                while self.board[x+1][y] == "/":
                    x += 1
                x1 = x + 1
                cords1 = "(" + str(x1) + "," + str(y) + ")"

                while self.board[x+2][y] == "/":
                    x += 1
                x2 = x + 2
                cords2 = "(" + str(x2) + "," + str(y) + ")"

                x = piece.x

                if self.is_mill_table[cords1] == 1 and self.is_mill_table[cords2] == 1:

                    self.is_mill_table[cords] = 0
                    self.is_mill_table[cords1] = 0
                    self.is_mill_table[cords2] = 0
                    self.mill_created(x1, y, turn, "notNone")
                    self.mill_created(x2, y, turn, "notNone")

                    if turn == "WHITE":
                        self.white_mills -= 1
                    else:
                        self.black_mills -= 1

                    return True

            # checking if our added or moved piece is last
            elif self.board[x+1][y] == None or (self.board[x+1][y] == "/" and self.board[x+2][y] == None) or (self.board[x+2][y] == "/" and self.board[x+3][y] == None):
                third = self.board[x][y]

                while self.board[x-1][y] == "/":
                    x -= 1
                x1 = x - 1
                cords1 = "(" + str(x1) + "," + str(y) + ")"

                while self.board[x-2][y] == "/":
                    x -= 1
                x2 = x - 2
                cords2 = "(" + str(x2) + "," + str(y) + ")"

                x = piece.x

                if self.is_mill_table[cords1] == 1 and self.is_mill_table[cords2] == 1:

                    self.is_mill_table[cords] = 0
                    self.is_mill_table[cords1] = 0
                    self.is_mill_table[cords2] = 0
                    self.mill_created(x1, y, turn, "notNone")
                    self.mill_created(x2, y, turn, "notNone")

                    if turn == "WHITE":
                        self.white_mills -= 1
                    else:
                        self.black_mills -= 1

                    return True

            # if it isn't first or last that means it's in the middle
            else:
                while self.board[x+1][y] == "/":
                    x += 1
                x1 = x + 1
                cords1 = "(" + str(x1) + "," + str(y) + ")"

                x = piece.x

                while self.board[x-1][y] == "/":
                    x -= 1
                x2 = x - 1
                cords2 = "(" + str(x2) + "," + str(y) + ")"

                x = piece.x

                if self.is_mill_table[cords1] == 1 and self.is_mill_table[cords2] == 1:

                    self.is_mill_table[cords] = 0
                    self.is_mill_table[cords1] = 0
                    self.is_mill_table[cords2] = 0
                    self.mill_created(x1, y, turn, "notNone")
                    self.mill_created(x2, y, turn, "notNone")

                    if turn == "WHITE":
                        self.white_mills -= 1
                    else:
                        self.black_mills -= 1

                    return True
            
            # was it a left-right mill?
            # checking if our added or moved piece is first
            if self.board[x][y-1] == None or (self.board[x][y-1] == "/" and self.board[x][y-2] == None) or (self.board[x][y-2] == "/" and self.board[x][y-3] == None):
                first = self.board[x][y]

                while self.board[x][y+1] == "/":
                    y += 1
                y1 = y + 1
                cords1 = "(" + str(x) + "," + str(y1) + ")"

                while self.board[x][y+2] == "/":
                    y += 1
                y2 = y + 2
                cords2 = "(" + str(x) + "," + str(y2) + ")"

                y = piece.y

                if self.is_mill_table[cords1] == 1 and self.is_mill_table[cords2] == 1:

                    self.is_mill_table[cords] = 0
                    self.is_mill_table[cords1] = 0
                    self.is_mill_table[cords2] = 0
                    self.mill_created(x, y1, turn, "notNone")
                    self.mill_created(x, y2, turn, "notNone")

                    if turn == "WHITE":
                        self.white_mills -= 1
                    else:
                        self.black_mills -= 1

                    return True

            # checking if our added or moved piece is last
            elif self.board[x][y+1] == None or (self.board[x][y+1] == "/" and self.board[x][y+2] == None) or (self.board[x][y+2] == "/" and self.board[x][y+3] == None):
                third = self.board[x][y]

                while self.board[x][y-1] == "/":
                    y -= 1
                y1 = y - 1
                cords1 = "(" + str(x) + "," + str(y1) + ")"

                while self.board[x][y-2] == "/":
                    y -= 1
                y2 = y - 2
                cords2 = "(" + str(x) + "," + str(y2) + ")"

                y = piece.y

                if self.is_mill_table[cords1] == 1 and self.is_mill_table[cords2] == 1:

                    self.is_mill_table[cords] = 0
                    self.is_mill_table[cords1] = 0
                    self.is_mill_table[cords2] = 0
                    self.mill_created(x, y1, turn, "notNone")
                    self.mill_created(x, y2, turn, "notNone")

                    if turn == "WHITE":
                        self.white_mills -= 1
                    else:
                        self.black_mills -= 1

                    return True

            # if it isn't first or last that means it's in the middle
            else:
                while self.board[x][y+1] == "/":
                    y += 1
                y1 = y + 1
                cords1 = "(" + str(x) + "," + str(y1) + ")"

                y = piece.y

                while self.board[x][y-1] == "/":
                    y -= 1
                y2 = y - 1
                cords2 = "(" + str(x) + "," + str(y2) + ")"

                y = piece.y

                if self.is_mill_table[cords1] == 1 and self.is_mill_table[cords2] == 1:

                    self.is_mill_table[cords] = 0
                    self.is_mill_table[cords1] = 0
                    self.is_mill_table[cords2] = 0
                    self.mill_created(x, y1, turn, "notNone")
                    self.mill_created(x, y2, turn, "notNone")

                    if turn == "WHITE":
                        self.white_mills -= 1
                    else:
                        self.black_mills -= 1

                    return True

        else: 
            return False

    # functions that help evaluate the board
    def get_blocked_pieces(self):
        white_blocked = 0
        black_blocked = 0
        for x in range(1, 9):
            for y in range(1, 9):
                if self.board[x][y] == "WHITE":
                    if self.get_available_positions_piece("WHITE", x, y) == False:
                        white_blocked += 1
                elif self.board[x][y] == "BLACK":
                    if self.get_available_positions_piece("BLACK", x, y) == False:
                        black_blocked += 1

        return white_blocked, black_blocked

    def next_to(self, piece1_str, piece2_str):
        x, y = int(piece1_str.split(",")[0][1]), int(piece1_str.split(",")[1][0])
        x2, y2 = int(piece2_str.split(",")[0][1]), int(piece2_str.split(",")[1][0])
        firstX = x
        firstY = y

        if self.board[x-1][y] == None or (self.board[x-1][y] == "/" and self.board[x-2][y] == None) or (self.board[x-2][y] == "/" and self.board[x-3][y] == None):
            while self.board[x + 1][y] == "/":
                x += 1
            bot = x + 1

            x = firstX

            if bot == x2 and y == y2:
                return True

        elif self.board[x+1][y] == None or (self.board[x+1][y] == "/" and self.board[x+2][y] == None) or (self.board[x+2][y] == "/" and self.board[x+3][y] == None):
            while self.board[x - 1][y] == "/":
                x -= 1
            top = x - 1

            x = firstX

            if top == x2 and y == y2:
                return True

        else:
            while self.board[x + 1][y] == "/":
                x += 1
            bot = x + 1

            x = firstX

            while self.board[x - 1][y] == "/":
                x -= 1
            top = x - 1

            x = firstX

            if (top == x2 or bot == x2) and y == y2:
                return True

        if self.board[x][y-1] == None or (self.board[x][y-1] == "/" and self.board[x][y-2] == None) or (self.board[x][y-2] == "/" and self.board[x][y-3] == None):

            while self.board[x][y+1] == "/":
                y += 1
            right = y + 1

            y = firstY

            if x == x2 and right == y2:
                return True

        elif self.board[x][y+1] == None or (self.board[x][y+1] == "/" and self.board[x][y+2] == None) or (self.board[x][y+2] == "/" and self.board[x][y+3] == None):

            while self.board[x][y-1] == "/":
                y -= 1
            left = y - 1

            y = firstY

            if x == x2 and left == y2:
                return True

        else:
            while self.board[x][y+1] == "/":
                y += 1
            right = y + 1

            y = firstY

            while self.board[x][y-1] == "/":
                y -= 1
            left = y - 1

            y = firstY

            if x == x2 and (right == y2 or left == y2):
                return True

        return False
        
    def get_23_conf_double_mill(self):
        white_2_conf = 0
        white_3_conf = 0
        black_2_conf = 0
        black_3_conf = 0
        double_mills_white = 0
        double_mills_black = 0

        in_2_piece_white = ChainedHashMap()
        in_2_piece_white["(1,1)"] = 0
        in_2_piece_white["(1,4)"] = 0
        in_2_piece_white["(1,7)"] = 0
        in_2_piece_white["(2,2)"] = 0
        in_2_piece_white["(2,4)"] = 0
        in_2_piece_white["(2,6)"] = 0
        in_2_piece_white["(3,3)"] = 0
        in_2_piece_white["(3,4)"] = 0
        in_2_piece_white["(3,5)"] = 0
        in_2_piece_white["(4,1)"] = 0
        in_2_piece_white["(4,2)"] = 0
        in_2_piece_white["(4,3)"] = 0
        in_2_piece_white["(4,5)"] = 0
        in_2_piece_white["(4,6)"] = 0
        in_2_piece_white["(4,7)"] = 0
        in_2_piece_white["(5,3)"] = 0
        in_2_piece_white["(5,4)"] = 0
        in_2_piece_white["(5,5)"] = 0
        in_2_piece_white["(6,2)"] = 0
        in_2_piece_white["(6,4)"] = 0
        in_2_piece_white["(6,6)"] = 0
        in_2_piece_white["(7,1)"] = 0
        in_2_piece_white["(7,4)"] = 0
        in_2_piece_white["(7,7)"] = 0

        in_2_piece_black = {"(1,1)" : 0, "(1,4)" : 0, "(1,7)" : 0,
                            "(2,2)" : 0, "(2,4)" : 0, "(2,6)" : 0,
                            "(3,3)" : 0, "(3,4)" : 0, "(3,5)" : 0,
                            "(4,1)" : 0, "(4,2)" : 0, "(4,3)" : 0, "(4,5)" : 0, "(4,6)" : 0, "(4,7)" : 0,
                            "(5,3)" : 0, "(5,4)" : 0, "(5,5)" : 0,
                            "(6,2)" : 0, "(6,4)" : 0, "(6,6)" : 0,
                            "(7,1)" : 0, "(7,4)" : 0, "(7,7)" : 0}

        double_white = {"(1,1)" : 0, "(1,4)" : 0, "(1,7)" : 0,
                        "(2,2)" : 0, "(2,4)" : 0, "(2,6)" : 0,
                        "(3,3)" : 0, "(3,4)" : 0, "(3,5)" : 0,
                        "(4,1)" : 0, "(4,2)" : 0, "(4,3)" : 0, "(4,5)" : 0, "(4,6)" : 0, "(4,7)" : 0,
                        "(5,3)" : 0, "(5,4)" : 0, "(5,5)" : 0,
                        "(6,2)" : 0, "(6,4)" : 0, "(6,6)" : 0,
                        "(7,1)" : 0, "(7,4)" : 0, "(7,7)" : 0}

        double_black = {"(1,1)" : 0, "(1,4)" : 0, "(1,7)" : 0,
                        "(2,2)" : 0, "(2,4)" : 0, "(2,6)" : 0,
                        "(3,3)" : 0, "(3,4)" : 0, "(3,5)" : 0,
                        "(4,1)" : 0, "(4,2)" : 0, "(4,3)" : 0, "(4,5)" : 0, "(4,6)" : 0, "(4,7)" : 0,
                        "(5,3)" : 0, "(5,4)" : 0, "(5,5)" : 0,
                        "(6,2)" : 0, "(6,4)" : 0, "(6,6)" : 0,
                        "(7,1)" : 0, "(7,4)" : 0, "(7,7)" : 0}

        for x in range(1, 8):
            for y in range(1, 8):
                if self.board[x][y] == "WHITE" or self.board[x][y] == "BLACK":
                    if self.board[x][y] == "WHITE":
                        turn = "WHITE"
                    else:
                        turn = "BLACK"
                    firstX = x
                    firstY = y

                    # if it is first
                    if self.board[x-1][y] == None or (self.board[x-1][y] == "/" and self.board[x-2][y] == None) or (self.board[x-2][y] == "/" and self.board[x-3][y] == None):

                        while self.board[x+1][y] == "/":
                            x += 1
                        second = x + 1

                        while self.board[x+2][y] == "/":
                            x += 1
                        third = x + 2

                        x = firstX

                        if (self.board[second][y] == turn and self.board[third][y].startswith("(")) or (self.board[third][y] == turn and self.board[second][y].startswith("(")):
                            cords = "(" + str(firstX) +"," + str(y) + ")"
                            if turn == "WHITE":
                                in_2_piece_white[cords] += 1
                            else:
                                in_2_piece_black[cords] += 1

                            if self.board[second][y] == turn:
                                cords = "(" + str(second) +"," + str(y) + ")"
                            else:
                                cords = "(" + str(third) +"," + str(y) + ")"

                            if turn == "WHITE":
                                in_2_piece_white[cords] += 1
                            else:
                                in_2_piece_black[cords] += 1

                        elif (self.board[second][y] == turn and self.board[third][y] == turn):
                            cords = "(" + str(firstX) +"," + str(y) + ")"
                            cords1 = "(" + str(second) +"," + str(y) + ")"
                            cords2 = "(" + str(third) +"," + str(y) + ")"
                            if turn == "WHITE":
                                double_white[cords] += 1
                                double_white[cords1] += 1
                                double_white[cords2] += 1
                            else:
                                double_black[cords] += 1
                                double_black[cords1] += 1
                                double_black[cords2] += 1

                    # if it is last
                    elif self.board[x+1][y] == None or (self.board[x+1][y] == "/" and self.board[x+2][y] == None) or (self.board[x+2][y] == "/" and self.board[x+3][y] == None):
                        while self.board[x-1][y] == "/":
                            x -= 1
                        second = x - 1

                        while self.board[x-2][y] == "/":
                            x -= 1
                        first = x - 2

                        x = firstX

                        if (self.board[second][y] == turn and self.board[first][y].startswith("(")) or (self.board[first][y] == turn and self.board[second][y].startswith("(")):
                            cords = "(" + str(firstX) +"," + str(y) + ")"

                            if turn == "WHITE":
                                in_2_piece_white[cords] += 1
                            else:
                                in_2_piece_black[cords] += 1

                            if self.board[second][y] == turn:
                                cords = "(" + str(second) +"," + str(y) + ")"
                            else:
                                cords = "(" + str(first) +"," + str(y) + ")"

                            if turn == "WHITE":
                                in_2_piece_white[cords] += 1
                            else:
                                in_2_piece_black[cords] += 1

                        elif (self.board[second][y] == turn and self.board[first][y] == turn):
                            cords = "(" + str(firstX) +"," + str(y) + ")"
                            cords1 = "(" + str(second) +"," + str(y) + ")"
                            cords2 = "(" + str(first) +"," + str(y) + ")"
                            if turn == "WHITE":
                                double_white[cords] += 1
                                double_white[cords1] += 1
                                double_white[cords2] += 1
                            else:
                                double_black[cords] += 1
                                double_black[cords1] += 1
                                double_black[cords2] += 1

                    #if it is middle
                    else:
                        while self.board[x+1][y] == "/":
                            x += 1
                        to_the_rightX = x + 1

                        x = firstX

                        while self.board[x-1][y] == "/":
                            x -= 1
                        to_the_leftX = x - 1

                        x = firstX

                        if (self.board[to_the_rightX][y] == turn and self.board[to_the_leftX][y].startswith("(")) or (self.board[to_the_leftX][y] == turn and self.board[to_the_rightX][y].startswith("(")):
                            cords = "(" + str(firstX) +"," + str(y) + ")"

                            if turn == "WHITE":
                                in_2_piece_white[cords] += 1
                            else:
                                in_2_piece_black[cords] += 1

                            if self.board[to_the_rightX][y] == turn:
                                cords = "(" + str(to_the_rightX) +"," + str(y) + ")"
                            else:
                                cords = "(" + str(to_the_leftX) +"," + str(y) + ")"
                            
                            if turn == "WHITE":
                                in_2_piece_white[cords] += 1
                            else:
                                in_2_piece_black[cords] += 1

                        elif (self.board[to_the_rightX][y] == turn and self.board[to_the_leftX][y] == turn):
                            cords = "(" + str(firstX) +"," + str(y) + ")"
                            cords1 = "(" + str(to_the_rightX) +"," + str(y) + ")"
                            cords2 = "(" + str(to_the_leftX) +"," + str(y) + ")"
                            if turn == "WHITE":
                                double_white[cords] += 1
                                double_white[cords1] += 1
                                double_white[cords2] += 1
                            else:
                                double_black[cords] += 1
                                double_black[cords1] += 1
                                double_black[cords2] += 1


                    # now checking the left-right direction
                    # if it is first
                    if self.board[x][y-1] == None or (self.board[x][y-1] == "/" and self.board[x][y-2] == None) or (self.board[x][y-2] == "/" and self.board[x][y-3] == None):
                        while self.board[x][y+1] == "/":
                            y += 1
                        second = y + 1

                        while self.board[x][y+2] == "/":
                            y += 1
                        third = y + 2

                        y = firstY

                        if (self.board[x][second] == turn and self.board[x][third].startswith("(")) or (self.board[x][third] == turn and self.board[x][second].startswith("(")):
                            cords = "(" + str(x) +"," + str(firstY) + ")"

                            if turn == "WHITE":
                                in_2_piece_white[cords] += 1
                            else:
                                in_2_piece_black[cords] += 1

                            if self.board[x][second] == turn:
                                cords = "(" + str(x) +"," + str(second) + ")"
                            else:
                                cords = "(" + str(x) +"," + str(third) + ")"
                            
                            if turn == "WHITE":
                                in_2_piece_white[cords] += 1
                            else:
                                in_2_piece_black[cords] += 1

                        elif (self.board[x][second] == turn and self.board[x][third] == turn):
                            cords = "(" + str(x) +"," + str(y) + ")"
                            cords1 = "(" + str(x) +"," + str(second) + ")"
                            cords2 = "(" + str(x) +"," + str(third) + ")"
                            if turn == "WHITE":
                                double_white[cords] += 1
                                double_white[cords1] += 1
                                double_white[cords2] += 1
                            else:
                                double_black[cords] += 1
                                double_black[cords1] += 1
                                double_black[cords2] += 1
                        
                    # if it is last 
                    elif self.board[x][y+1] == None or (self.board[x][y+1] == "/" and self.board[x][y+2] == None) or (self.board[x][y+2] == "/" and self.board[x][y+3] == None):
                        while self.board[x][y-1] == "/":
                            y -= 1
                        second = y - 1

                        while self.board[x][y-2] == "/":
                            y -= 1
                        first = y - 2

                        y = firstY

                        if (self.board[x][second] == turn and self.board[x][first].startswith("(")) or (self.board[x][first] == turn and self.board[x][second].startswith("(")):
                            cords = "(" + str(x) +"," + str(firstY) + ")"

                            if turn == "WHITE":
                                in_2_piece_white[cords] += 1
                            else:
                                in_2_piece_black[cords] += 1

                            if self.board[x][second] == turn:
                                cords = "(" + str(x) +"," + str(second) + ")"
                            else:
                                cords = "(" + str(x) +"," + str(first) + ")"
                            
                            if turn == "WHITE":
                                in_2_piece_white[cords] += 1
                            else:
                                in_2_piece_black[cords] += 1

                        elif (self.board[x][second] == turn and self.board[x][first] == turn):
                            cords = "(" + str(x) +"," + str(y) + ")"
                            cords1 = "(" + str(x) +"," + str(second) + ")"
                            cords2 = "(" + str(x) +"," + str(first) + ")"
                            if turn == "WHITE":
                                double_white[cords] += 1
                                double_white[cords1] += 1
                                double_white[cords2] += 1
                            else:
                                double_black[cords] += 1
                                double_black[cords1] += 1
                                double_black[cords2] += 1

                    # if it is middle
                    else:
                        while self.board[x][y+1] == "/":
                            y += 1
                        to_the_rightY = y + 1

                        y = firstY

                        while self.board[x][y-1] == "/":
                            y -= 1
                        to_the_leftY = y - 1

                        y = firstY

                        if (self.board[x][to_the_rightY] == turn and self.board[x][to_the_leftY].startswith("(")) or (self.board[x][to_the_leftY] == turn and self.board[x][to_the_rightY].startswith("(")):
                            cords = "(" + str(x) +"," + str(firstY) + ")"

                            if turn == "WHITE":
                                in_2_piece_white[cords] += 1
                            else:
                                in_2_piece_black[cords] += 1

                            if self.board[x][to_the_rightY] == turn:
                                cords = "(" + str(x) +"," + str(to_the_rightY) + ")"
                            else:
                                cords = "(" + str(x) +"," + str(to_the_leftY) + ")"
                            
                            if turn == "WHITE":
                                in_2_piece_white[cords] += 1
                            else:
                                in_2_piece_black[cords] += 1

                        elif (self.board[x][to_the_rightY] == turn and self.board[x][to_the_leftY] == turn):
                            cords = "(" + str(x) +"," + str(y) + ")"
                            cords1 = "(" + str(x) +"," + str(to_the_rightY) + ")"
                            cords2 = "(" + str(x) +"," + str(to_the_leftY) + ")"
                            if turn == "WHITE":
                                double_white[cords] += 1
                                double_white[cords1] += 1
                                double_white[cords2] += 1
                            else:
                                double_black[cords] += 1
                                double_black[cords1] += 1
                                double_black[cords2] += 1                      

        has4 = []
        for x in in_2_piece_white:
            if in_2_piece_white[x] == 2:
                white_2_conf += 1
            if in_2_piece_white[x] == 4:
                white_2_conf += 2
                white_3_conf += 1
                has4.append(x)
            # we have to check ar two pieces that are in 2 diff 3 config next to eachother
        diff = False
        if len(has4) > 1:
            for i in range(len(has4) - 1):
                if self.next_to(has4[i], has4[i+1]) == True:
                    diff = True
                    break
        if diff is True:
            white_2_conf = int(white_2_conf / 2 - white_3_conf * 1.5)
        else:
            white_2_conf = int(white_2_conf / 2 - white_3_conf * 2)

        has4 = []
        for x in in_2_piece_black:
            if in_2_piece_black[x] == 2:
                black_2_conf += 1
            if in_2_piece_black[x] == 4:
                black_2_conf += 2
                black_3_conf += 1
                has4.append(x)
            # we have to check ar two pieces that are in 2 diff 3 config next to eachother
        diff = False
        if len(has4) > 1:
            for i in range(len(has4) - 1):
                if self.next_to(has4[i], has4[i+1]) == True:
                    diff = True
                    break
        if diff is True:
            black_2_conf = int(black_2_conf / 2 - black_3_conf * 1.5)
        else:
            black_2_conf = int(black_2_conf / 2 - black_3_conf * 2)

        for x in double_white:
            if double_white[x] == 6:
                double_mills_white += 1
                self.white_mills -= 2

        for x in double_black:
            if double_black[x] == 6:
                double_mills_black += 1
                self.black_mills -= 2

        return white_2_conf, white_3_conf, black_2_conf, black_3_conf, double_mills_white, double_mills_black

    def the_end(self):
        if self.white_pieces <= 2:
            return "BLACK"
        elif self.black_pieces <= 2:
            return "WHITE"
        elif self.get_available_positions2("WHITE") == False:
            return "BLACK"
        elif self.get_available_positions2("BLACK") == False:
            return "WHITE"
        return False

    def evaluate_board(self, phase1):
        white_blocked, black_blocked = self.get_blocked_pieces()
        white_2conf, white_3conf, black_2conf, black_3conf, white_double_mill, black_double_mill = self.get_23_conf_double_mill()
        end = 0
        if self.the_end() == "WHITE":
            end = 1086
        elif self.the_end() == "BLACK":
            end = -1086

        if phase1 == True:
            return (self.white_mills - self.black_mills) * 26 + (black_blocked - white_blocked) * 1 + (self.white_pieces - self.black_pieces) * 9 + (white_2conf - black_2conf) * 10 + (white_3conf - black_3conf) * 7 + (white_double_mill - black_double_mill) * 3
        else:
            return (self.white_mills - self.black_mills) * 43 + (black_blocked - white_blocked) * 10 + (self.white_pieces - self.black_pieces) * 11 + (white_double_mill - black_double_mill) * 8 + end

    def removable_pieces(self, turn):
        non_mill = self.get_non_mill_pieces(turn)
        if non_mill == []:
            for x in range(1,8):
                for y in range(1,8):
                    if (self.board[x][y] == "BLACK" and turn == "WHITE") or (self.board[x][y] == "WHITE" and turn == "BLACK"):
                        cords = "(" + str(x) + "," + str(y) + ")"
                        non_mill.append(cords)
        return non_mill

    def get_pieces(self, turn):
        pieces = []
        for x in range(1,8):
                for y in range(1,8):
                    if self.board[x][y] == turn:
                        pieces.append("(" + str(x) + "," + str(y) + ")")

        return pieces
