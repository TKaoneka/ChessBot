import chess

def evaluate(position): 
    piece_values = {
        chess.PAWN: 100,
        chess.ROOK: 500,
        chess.KNIGHT: 320,
        chess.BISHOP: 330,
        chess.QUEEN: 900,
        chess.KING: 20000
        }
    
    material_score = 0

    for piece in chess.PIECE_TYPES:
        material_advantage += len(position.pieces(piece, chess.WHITE)) * piece_values[piece]
        material_advantage -= len(position.pieces(piece, chess.BLACK)) * piece_values[piece]

    return material_score
        

def minimax(position, max_depth, maximizing_player, alpha, beta):
    if not position or max_depth == 0:
        return evaluate(position)

    if maximizing_player:
        value = float("-inf")

        for child in position.children:
            value = max(value, minimax(child, max_depth - 1, False, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")

        for child in position.children:
            value = min(value, minimax(child, max_depth - 1, True, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
    
def best_move(position, depth):
    best_move_value = float("-inf")
    best_move = None
    possible_positions = position.legal_moves

    for move in possible_positions:
        position.push(move)
        move_value = minimax(position, depth)

        if move_value > best_move_value or not best_move:
            best_move_value = move_value
            best_move = move

        position.pop()

    return best_move