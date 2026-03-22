def evaluate(position): 
    piece_values = {
        "white_pawn": 100,
        "white_rook": 500,
        "white_knight": 320,
       "white_bishop": 330,
        "white_queen": 900,
        "white_king": 20000,
        "black_pawn": -100,
        "black_rook": -500,
        "black_knight": -320,
       "black_bishop": -330,
        "black_queen": -900,
        "black_king": -20000
    }
    
    material_score = 0

    for row in position:
        for piece in row:
            material_score += piece_values.get(piece, 0)

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