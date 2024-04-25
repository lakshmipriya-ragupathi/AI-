
S0 = [
    [0, 0, 0, 1, 0, 4, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 8, 0, 0],
    [0, 8, 0, 7, 0, 3, 0, 6, 0],
    [9, 0, 7, 0, 0, 0, 1, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 4, 0, 0, 0, 5, 0, 8],
    [0, 0, 0, 2, 0, 6, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 8, 0, 5, 0, 0, 0]
]


# Exhaustive Search
def Find_next_empty(State):
    for i in range(9):
        for j in range(9):
            if State[i][j] == 0:
                return i, j
    return -1, -1


def Validity(State, i, j, k):
    # check the row
    valid_row = True
    valid_col = True
    valid_sub = True
    valid_grid = False
    for m in range(9):
        if k == State[i][m]:
            valid_row = False
    # check the column if row is valid
    if valid_row:
        for n in range(9):
            if k == State[n][j]:
                valid_col = False

    # check the sub-grid if both row and column are valid
    if valid_row and valid_col:
        x, y = (i // 3) * 3, (j // 3) * 3
        for a in range(x, x + 3):
            for b in range(y, y + 3):
                if State[a][b] == k:
                    valid_sub = False

    if valid_row and valid_col and valid_sub:
        return True

    return False


def print_board(State):
    row_ = 0
    for row in State:
        if row_ % 3 == 0 and row_ != 0:
            print()
        print(row[0:3], ' ', row[3:6], ' ', row[6:9])
        row_ += 1

    return


def Solve(State, i=0, j=0, iterations=0):
    i, j = Find_next_empty(State)
    # if terminal reached
    if i == -1:
        return True, iterations

    for k in range(1, 10):
        if Validity(State, i, j, k):
            State[i][j] = k
            print(iterations)
            print_board(State)
            print()
            iterations += 1
            success, iterations = Solve(State, i, j, iterations)
            if success:
                return True, iterations

            State[i][j] = 0

    return False, iterations

Solve(S0)

