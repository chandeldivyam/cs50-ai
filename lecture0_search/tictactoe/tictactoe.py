"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
v_minus = -999
v_plus = 999


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return X
    
    previous_turns = 0

    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j]:
                previous_turns += 1

    if previous_turns%2 == 0:
        return X
    
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j] is EMPTY:
                possible_actions.add((i,j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    move_of = player(board)
    i,j = action

    new_board = copy.deepcopy(board)

    if board[i][j] is not None:
        raise Exception
    
    new_board[i][j] = move_of
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X,O):
        #check horizontal
        for row in board:
            if row.count(player) == 3:
                return player
        
        for i in range(0,3):
            column = [board[x][i] for x in range(0,3)]
            if column.count(player) == 3:
                return player
            
        if [board[i][i] for i in range(0, 3)].count(player) == 3:
            return player
        
        if [board[i][~i] for i in range(0, 3)].count(player) == 3:
            return player
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    #all moves exhausted
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if not terminal(board):
        raise NotImplementedError
    
    winning_player = winner(board)
    
    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    curr_player = player(board)

    if terminal(board):
        return None
    
    if curr_player == X:
        optimal_move = max_value(board)[1]
        return optimal_move
    
    elif curr_player == O:
        optimal_move = min_value(board)[1]
        return optimal_move
    
    else:
        raise Exception

def max_value(board):
    if terminal(board):
        return (utility(board), ())
    v = -999
    optimial_move = ()
    for action in actions(board):
        v_new = min_value(result(board, action))[0]
        if v_new > v:
            optimial_move = action
            v = v_new

    return (v, optimial_move)

def min_value(board):
    if terminal(board):
        return (utility(board), ())
    v = 999

    optimial_move = ()
    for action in actions(board):
        v_new = max_value(result(board, action))[0]
        if v_new < v:
            optimial_move = action
            v = v_new
        
    return (v, optimial_move)