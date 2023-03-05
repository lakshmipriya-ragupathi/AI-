import math

# we want X to win

S0 = [
    ['X', 'O', 'O'],
    [' ', ' ', 'X'],
    [' ', 'X', 'O']
]


# who is currently playing
def Player(state):
    X_count = sum(row.count('X') for row in state)
    O_count = sum(row.count('O') for row in state)
    if X_count > O_count:
        return 'O'
    if O_count > X_count:
        return 'X'
    if O_count == X_count:
        return 'X'


# return legal moves in state
# return all empty places where the current player could go
def Actions(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                moves.append((i, j))
    return moves


# check if the game ended
def Terminal(state):
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2]:
            return True
        if state[0][i] == state[1][i] == state[2][i]:
            return True

    empt = sum(row.count(' ') for row in state)
    if empt == 0:
        return True
    else:
        return False
    return False


# final numerical value for a terminal state
def Utility(state):
    for i in range(3):
        # check match in rows
        if state[i][0] == state[i][1] == state[i][2]:
            if state[i][0] == 'X':
                return 1
            elif state[i][0] == 'O':
                return -1

        # check match in columns
        if state[0][i] == state[1][i] == state[2][i]:
            if state[0][i] == 'X':
                return 1
            elif state[0][i] == 'O':
                return -1

    # check match in diagonals
    if state[0][0] == state[1][1] == state[2][2]:
        if state[0][0] == 'X':
            return 1
        elif state[0][0] == 'O':
            return -1
    if state[0][2] == state[1][1] == state[2][0]:
        if state[0][2] == 'X':
            return 1
        elif state[0][2] == 'O':
            return -1

    return 0


# returns state after an action / move
def Result(state, action):
    cur_player = Player(state)
    board = state
    board[action[0]][action[1]] = cur_player
    return board


# minimax algorithm
# given a state a:
# MAX picks action a in Actions(s) that produces highest value of MIN-VALUE(Result(s,a))
# prune if alpha>= beta

def MAX_VALUE(state, Alpha, Beta):
    if Terminal(state):
        return Utility(state)
    v = -math.inf
    for action in Actions(state):
        v = max(v, MIN_VALUE(Result(state, action), Alpha, Beta))
        # pruning
        if v >= Beta:
            return v
        Alpha = max(Alpha, v)
    return v


# MIN picks action a in Actions(s) that produces smallest value of MAX-VALUE(Result(s,a))
def MIN_VALUE(state, Alpha, Beta):
    if Terminal(state):
        return Utility(state)
    v = math.inf
    for action in Actions(state):
        v = min(v, MAX_VALUE(Result(state, action), Alpha, Beta))
        # pruning
        if v <= Alpha:
            return v
        Beta = min(Beta, v)
    return v


# assuming current player is X and we want to maximise X
def minimax_alpha_beta(state):
    v = -math.inf
    alpha = -math.inf
    for action in Actions(state):
        min_val = MIN_VALUE(Result(state, action), alpha, math.inf)
        if min_val > v:
            v = min_val
            move = action
        alpha = max(alpha, v)
    return move


print(S0)
print("For X to win, current move of X should be : ", minimax_alpha_beta(S0))

