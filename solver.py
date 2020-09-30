# Python Sudoku Solver

def output(grid):
    print("-------------------------")
    for row in grid:
        print(row)
    print("-------------------------")


# check if the given number is valid when put into a specific position in the sudoku grid
def check_validity(grid, number, position):
    row_idx, column_idx = position

    # check if number already exists in the row
    if number in grid[row_idx]:
        return False
    
    # check if number already exists in the column
    column = [row[column_idx] for row in grid]
    if number in column:
        return False

    # check if number already exists in the 3x3 box
    row_box = row_idx // 3
    col_box = column_idx // 3
    for row in grid[row_box*3: row_box*3 + 3]:
        for element in row[col_box*3: col_box*3 + 3]:
            if element == number:
                return False

    return True

# find the indices of the next empty position in the grid, False otherwise
def get_next_empty_cell(grid):
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[row_idx])):
            if grid[row_idx][col_idx] == None:
                return (row_idx, col_idx)
    return False

# add a number to the grid
def add_to_grid(grid, number, position):
    row_idx, column_idx = position
    grid[row_idx][column_idx] = number
    return grid

# remove a number from the grid
def remove_from_grid(grid, number, position):
    row_idx, column_idx = position
    grid[row_idx][column_idx] = None
    return grid


# recursive function for each cell
def sudoku_step(grid):
    next_position = get_next_empty_cell(grid)

    # return true if grid is complete
    if next_position == False:
        return True
    
    # else fill in a number
    for number in range(1, 10, 1):
        if check_validity(grid, number, next_position):
            grid = add_to_grid(grid, number, next_position)
            if sudoku_step(grid):
                return True
            else:
                grid = remove_from_grid(grid, number, next_position)
    else:
        # print("Cannot fill any valid number, backtracking...")
        return False



if __name__=="__main__": 
    
    grid = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]
    ]

    grid = [
        [None, None, None, 2, 6, None, 7, None, 1],
        [6, 8, None, None, 7, None, None, 9, None],
        [1, 9, None, None, None, 4, 5, None, None],
        [8, 2, None, 1, None, None, None, 4, None],
        [None, None, 4, 6, None, 2, 9, None, None],
        [None, 5, None, None, None, 3, None, 2, 8],
        [None, None, 9, 3, None, None, None, 7, 4],
        [None, 4, None, None, 5, None, None, 3, 6],
        [7, None, 3, None, 1, 8, None, None, None]
    ]

    if sudoku_step(grid):
        print("Sudoku solved!")
        output(grid)
    else:
        print("No solution exists. Check your input again!")