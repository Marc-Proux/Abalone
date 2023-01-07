def minimax_decision(board, turn, queue):
    global explored_nodes
    possible_moves = board.get_possible_moves()
    best_move = possible_moves[0]
    best_value = -2
    for move in possible_moves:
        updated_board = board.copy()
        updated_board.grid[move[0]][move[
            1]] = turn % 2 + 1  # l'IA met une valeur dans la grille , soit 1 soit 2 (dÃ©pend de son tour de jeu, pour Ãªtre en accord avec la mÃ©thode move)
        value = min_value(updated_board, turn + 1)
        if value > best_value:
            best_value = value
            best_move = move
    explored_nodes += len(possible_moves)
    print("EXPLORED NODES : ", explored_nodes)
    print("BEST VALUE : ", best_value)
    explored_nodes = 0
    queue.put(best_move)


def min_value(board, turn):
    global explored_nodes
    if board.check_victory(update_display=False):
        return 1
    elif turn > 9:
        return 0
    possible_moves = board.get_possible_moves()
    value = 2
    explored_nodes += len(possible_moves)
    for move in possible_moves:
        updated_board = board.copy()
        updated_board.grid[move[0]][move[1]] = turn % 2 + 1
        max_val = max_value(updated_board, turn + 1)
        value = min(value, max_val)
    return value


def max_value(board, turn):
    global explored_nodes
    if board.check_victory(update_display=False):
        return -1
    elif turn > 9:
        return 0
    possible_moves = board.get_possible_moves()
    value = -2
    explored_nodes += len(possible_moves)
    for move in possible_moves:
        updated_board = board.copy()
        updated_board.grid[move[0]][move[1]] = turn % 2 + 1
        min_val = min_value(updated_board, turn + 1)
        value = max(value, min_val)
    return value