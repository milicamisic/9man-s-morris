#AI IS BLACK AND MINIMIZER

from time import time
from .board import Board
from minimax.algorithm import minimax1, minimax2

class Game(object):
    
    def __init__(self, first):
        self.board = Board()
        self.turn = first
        self.is_over = False

    def play(self):

        # PHASE 1
        print("Phase 1: Place your pieces on the board")
        #it's not possible to win during this phase so there is no need to check for it
        
        for plays in range(18):

            #IF THE AI IS PLAYING
            
            if self.turn == "BLACK":
                time1 = time()
                score, self.board = minimax1(self.board, 3, float("-inf"), float("inf"), False, plays)
                time2 = time()
                print("Time:" + str(time2-time1) + "s.")

            else:
                self.board.print_board()
                available_positions = self.board.get_available_positions1()
                print("The available positions are: " + str(available_positions))

                while True:
                    try:
                        x = int(input("Choose the x coordinate: "))
                        y = int(input("Choose the y coordinate: "))
                        if self.board.add_piece(int(x), int(y), self.turn) == True:
                            break
                        else:
                            print("You chose invaild coordinates, please try again.")

                    except:
                        print("You chose invaild coordinates, please try again.")

                if self.board.mill_created(x, y, self.turn) == True:
                    self.board.print_board()
                    print("Wonderful, you made a mill, choose an opponent piece to remove. Removable pieces: " + str(self.board.removable_pieces(self.turn)))
                    while True:
                        try:
                            x = int(input("Choose the x coordinate: "))
                            y = int(input("Choose the y coordinate: "))

                            if self.board.remove_piece(x, y, self.turn) == True:
                                break
                            else:
                                print("You chose invaild coordinates, please try again.")

                        except:
                            print("You chose invaild coordinates, please try again.")
        
            if self.turn == "WHITE":
                self.turn = "BLACK"
            else:
                self.turn = "WHITE"

        # PHASE 2
        print()
        print("Phase 2: Move your piece's to create a mill.")
        while self.is_over == False:
            
            if self.turn == "BLACK":
                time1 = time()
                score, self.board = minimax2(self.board, 3, float("-inf"), float("inf"), False)
                time2 = time()
                print("Time:" + str(time2-time1) + "s.")

            else:
                self.board.print_board()
                available_positions = self.board.get_available_positions2(self.turn)
                print("The available positions are: " + str(available_positions))
                while True:
                    try:
                        oldX = int(input("Choose the x coordinate of the piece you want to move: "))
                        oldY = int(input("Choose the y coordinate of the piece you want to move: "))
                        newX = int(input("Choose the x coordinate: "))
                        newY = int(input("Choose the y coordinate: "))

                        if self.board.move_piece(int(oldX), int(oldY), int(newX), int(newY),self.turn) == True:
                            break
                        else:
                            print("You chose invaild coordinates, please try again.")

                    except:
                        print("You chose invaild coordinates, please try again.")

                if self.board.mill_created(newX, newY, self.turn) == True:
                    self.board.print_board()
                    print("Wonderful, you made a mill, choose an opponent piece to remove. Removable pieces: " + str(self.board.removable_pieces(self.turn)))
                    while True:
                        try:
                            x = int(input("Choose the x coordinate: "))
                            y = int(input("Choose the y coordinate: "))

                            if self.board.remove_piece(x, y, self.turn) == True:
                                break
                            else:
                                print("You chose invaild coordinates, please try again.")

                        except:
                            print("You chose invaild coordinates, please try again.")

            if self.turn == "WHITE":
                self.turn = "BLACK"
            else:
                self.turn = "WHITE"
                
            self.is_over = self.the_end(self.turn)
         
    def the_end(self,turn):
        if self.board.white_pieces <= 2:
            print("Game is over. Black won.")
            return True
        elif self.board.black_pieces <= 2:
            print("Game is over. White won.")
            return True
        elif self.board.get_available_positions2(turn) == False:
            if turn == "WHITE":
                print("Game is over. Black won.")
                return "BLACK"
            else:
                print("Game is over. White won.")
                return "WHITE"
        return False
