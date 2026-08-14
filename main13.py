# tic_tac_toe_win_checks.py

# --- Step 1: Define your functions below ---
#
# Each function receives a 3x3 tic-tac-toe board represented as
# a List-of-Lists.
#
# Example board:
#
# [
#     ["x", "o", "x"],
#     ["o", "x", "o"],
#     ["o", "x", "x"]
# ]
#
# Empty spaces are represented by "" (an empty string).
#
# Each function should return:
#     True  -> if the specified type of win exists
#     False -> otherwise


def check_column_win(board):
    """
    TODO:

    Determine whether either player has won by filling an entire COLUMN.

    Instructions:
    - Use a for-loop to examine each column.
    - For each column, compare the values in:
          row 0
          row 1
          row 2
    - Ignore columns whose first value is an empty string.
    - Return True as soon as a winning column is found.
    - Return False if no column contains a win.
    """
    for column in range(3):
        Top_Piece = board[0][column]
        Middle_Piece = board[1][column]
        Bottom_Piece = board[2][column]
        if Top_Piece == Middle_Piece and Middle_Piece == Bottom_Piece:
            return True
        return False


def check_row_win(board):
    """
    TODO:

    Determine whether either player has won by filling an entire ROW.

    Instructions:
    - Use a for-loop to examine each row.
    - Compare all three values in the row.
    - Ignore rows whose first value is an empty string.
    - Return True as soon as a winning row is found.
    - Return False if no row contains a win.
    """
    for row in board:
        left_piece = row[0]
        middle_piece = row[1]
        right_piece = row[2]
    return


def check_diagonal_win(board):
    """
    TODO:

    Determine whether either player has won diagonally.

    There are only TWO possible diagonals:

        Top-left  -> Bottom-right

        Top-right -> Bottom-left

    Instructions:
    - Check both diagonals.
    - Ignore a diagonal if its first square is empty.
    - Return True if either diagonal contains three matching pieces.
    - Otherwise return False.
    """
    pass


# ---------------------------------------------------------
# Tests
# ---------------------------------------------------------

def run_tests():
    print("Running Tic-Tac-Toe win detection tests...")

    # -----------------------------------------------------
    # Column Wins
    # -----------------------------------------------------

    column_x_win = [
        ["x", "o", ""],
        ["x", "", "o"],
        ["x", "", ""]
    ]

    column_o_win = [
        ["x", "o", ""],
        ["", "o", "x"],
        ["x", "o", ""]
    ]

    no_column_win = [
        ["x", "o", ""],
        ["o", "x", ""],
        ["", "", "o"]
    ]

    assert check_column_win(column_x_win) == True
    assert check_column_win(column_o_win) == True
    assert check_column_win(no_column_win) == False

    # -----------------------------------------------------
    # Row Wins
    # -----------------------------------------------------

    row_x_win = [
        ["x", "x", "x"],
        ["o", "", "o"],
        ["", "", ""]
    ]

    row_o_win = [
        ["x", "", ""],
        ["o", "o", "o"],
        ["x", "", "x"]
    ]

    no_row_win = [
        ["x", "o", "x"],
        ["o", "x", "o"],
        ["o", "x", "o"]
    ]

    assert check_row_win(row_x_win) == True
    assert check_row_win(row_o_win) == True
    assert check_row_win(no_row_win) == False

    # -----------------------------------------------------
    # Diagonal Wins
    # -----------------------------------------------------

    diagonal_down = [
        ["x", "o", ""],
        ["", "x", "o"],
        ["", "", "x"]
    ]

    diagonal_up = [
        ["", "", "o"],
        ["", "o", "x"],
        ["o", "x", "x"]
    ]

    no_diagonal = [
        ["x", "o", ""],
        ["o", "x", "o"],
        ["o", "x", ""]
    ]

    assert check_diagonal_win(diagonal_down) == True
    assert check_diagonal_win(diagonal_up) == True
    assert check_diagonal_win(no_diagonal) == False

    print("✅ All Tic-Tac-Toe tests passed!")


if __name__ == "__main__":
      run_tests()