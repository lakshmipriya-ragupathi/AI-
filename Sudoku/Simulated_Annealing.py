import random
import math

# Initialize the Sudoku grid
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


# Define the cost function
def cost_function(State):
    cost = 0
    for i in range(9):
        # Check rows for duplicates
        cost += len(set(State[i])) - 9
        # Check columns for duplicates
        col = [State[j][i] for j in range(9)]
        cost += len(set(col)) - 9
    # Check 3x3 subgrids for duplicates
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = []
            for k in range(3):
                subgrid += State[i + k][j:j + 3]
            cost += len(set(subgrid)) - 9
    return cost


# Get the valid list of empty spaces that must be filled
def valid_indexes(State):
    zeros = []
    for i in range(len(State)):
        for j in range(len(State[i])):
            if State[i][j] == 0:
                zeros.append((i, j))
    return zeros


def print_board(State):
    row_ = 0
    for row in State:
        if row_ % 3 == 0 and row_ != 0:
            print()
        print(row[0:3], ' ', row[3:6], ' ', row[6:9])
        row_ += 1

    return


# find a valid number to place in the grid
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


def find_valid(State, i, j):
    for k in range(1, 10):
        if Validity(State, i, j, k):
            return k
    return -1


# Simulated annealing algorithm
def simulated_annealing(State, cost_func):
    #schedule :
    T = 100.0
    T_min = 0.0001
    alpha = 0.9


    iterations = 0
    while T > T_min:
        print(iterations)
        print_board(State)
        print()
        iterations += 1
        indices_list = valid_indexes(State)
        i, j = random.choice(indices_list)
        old_val = State[i][j]
        new_val = find_valid(State, i, j)
        while new_val == old_val:
            new_val = random.randint(1, 9)
        old_grid = [row[:] for row in State]

        State[i][j] = new_val
        delta = cost_func(State) - cost_func(old_grid)
        if delta > 0:
            if math.exp(-delta / T) < random.random():
                State[i][j] = old_val
        T *= alpha

    return State


# Solve the Sudoku puzzle using simulated annealing
solution = simulated_annealing(S0, cost_function)
