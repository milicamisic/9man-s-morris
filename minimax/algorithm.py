#AI IS BLACK AND MINIMIZER

from copy import deepcopy

def minimax1(board, depth, alpha, beta, maximizer, counter):
    if depth == 0:
        if counter > 17:
            return board.evaluate_board(False), board
        else:
            return board.evaluate_board(True), board    # as long as the counter is 17 or less we evaluate for phase1

    if maximizer: # if it is maximizer we know it's white
        max_score = float("-inf")
        best_move = None
        for move in get_all_moves_phase1(board, "WHITE"):
            if counter == 17:
                evaluation = minimax2(move, depth - 1, alpha, beta, False)[0]
            else:
                evaluation = minimax1(move, depth - 1, alpha, beta, False, counter + 1)[0]

            max_score = max(max_score, evaluation)
            if max_score == evaluation:
                best_move = move

            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        
        return best_move.evaluate_board(True), best_move

    else:
        min_score = float("inf")
        best_move = None
        for move in get_all_moves_phase1(board, "BLACK"):
            if counter == 17:
                evaluation = minimax2(move, depth - 1, alpha, beta, True)[0]
            else:
                evaluation = minimax1(move, depth - 1, alpha, beta, True, counter + 1)[0]

            min_score = min(min_score, evaluation)
            if min_score == evaluation:
                best_move = move

            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        
        return best_move.evaluate_board(True), best_move

def minimax2(board, depth, alpha, beta, maximizer):
    if depth == 0 or board.the_end() != False:
        return board.evaluate_board(False), board

    if maximizer: # if it is maximizer we know it's white
        max_score = float("-inf")
        best_move = None
        for move in get_all_moves_phase2(board, "WHITE"):
            evaluation = minimax2(move, depth - 1, alpha, beta, False)[0]

            max_score = max(max_score, evaluation)
            if max_score == evaluation:
                best_move = move

            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        
        return best_move.evaluate_board(False), best_move

    else:
        min_score = float("inf")
        best_move = None
        for move in get_all_moves_phase2(board, "BLACK"):
            evaluation = minimax2(move, depth - 1, alpha, beta, True)[0]

            min_score = min(min_score, evaluation)
            if min_score == evaluation:
                best_move = move

            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        
        return best_move.evaluate_board(False), best_move

def get_all_moves_phase1(board, turn):
    moves = []

    for move in board.get_available_positions1():
        x, y = int(move.split(",")[0][1]), int(move.split(",")[1][0])
        temp_board = deepcopy(board)
        temp_board.add_piece(x, y, turn)

        if temp_board.mill_created(x, y, turn) == True:
            for remove in temp_board.removable_pieces(turn):
                Xremoved, Yremoved = int(remove.split(",")[0][1]), int(remove.split(",")[1][0])
                temp_board2 = deepcopy(temp_board)
                temp_board2.remove_piece(Xremoved, Yremoved, turn)

                moves.append(temp_board2)
        else:
            moves.append(temp_board)

    return moves

def get_all_moves_phase2(board, turn):
    moves = []

    for piece in board.get_pieces(turn):
        oldX, oldY = int(piece.split(",")[0][1]), int(piece.split(",")[1][0])
        if board.get_available_positions_piece(turn, oldX, oldY) != False:
            for move in board.get_available_positions_piece(turn, oldX, oldY):
                newX, newY = int(move.split(",")[0][1]), int(move.split(",")[1][0])
                temp_board = deepcopy(board)
                temp_board.move_piece(oldX, oldY, newX, newY, turn)

                if temp_board.mill_created(newX, newY, turn) == True:
                    for remove in temp_board.removable_pieces(turn):
                        Xremoved, Yremoved = int(remove.split(",")[0][1]), int(remove.split(",")[1][0])
                        temp_board2 = deepcopy(temp_board)
                        temp_board2.remove_piece(Xremoved, Yremoved, turn)

                        moves.append(temp_board2)
                else:
                    moves.append(temp_board)

    return moves