class ConnectFour:
    def __init__(self, rows=6, cols=7):
        """Initializes the Connect Four board."""
        self.board = [['.' for row in range(6)] for col in range(7)]

    def printBoard(self):
        # We have 6 rows (indices 0 to 5). The terminal prints top-to-bottom.
        for row_idx in range(6):
            row_output = ""

            # We have 7 columns (indices 0 to 6). The terminal prints left-to-right.
            for col_idx in range(7):
                # Grab the exact slot from the current column, at the current row depth
                row_output += self.board[col_idx][row_idx] + " "

            print(row_output)

    def getBoard(self):
        return self.board

    def gravity(self, col_number, val):
        target_column = self.board[col_number]
        for row_index in range(5, -1, -1):
            # 4. As we go up, is this spot empty?
            if target_column[row_index] == '.':
                target_column[row_index] = val
                # 5. Yes! It fell to this row. Return the row number.
                return row_index
        # Nothing Empty!
        return -1

    def checkWin(self, val, col_index, row_index):
        # Horizontal Check going right
        print("Horizontal Check going right")
        right_count = 0
        temp_col = col_index + 1 # Row is fixed.
        while temp_col <= 6 and right_count < 4 and self.board[temp_col][row_index] == val:
            temp_col += 1 # Move right we have a match
            right_count += 1 # Increment count as we have a match

        print("Horizontal Check going left")
        temp_col = col_index - 1  # Row is fixed.
        left_count = 0
        while temp_col >= 0 and left_count < 4 and self.board[temp_col][row_index] == val:
            temp_col -= 1  # Move right we have a match
            left_count += 1  # Increment count as we have a match

        if right_count + left_count + 1 >= 4:
            return True

        # Vertical Check going up
        up_count = 0
        temp_row = row_index - 1
        print("Vertical Check going up")
        while temp_row >= 0 and up_count < 4 and self.board[col_index][temp_row] == val:
            temp_row -= 1 # Moving up
            up_count += 1

        print("Vertical Check going down")
        down_count = 0
        temp_row = row_index + 1
        while temp_row <= 5 and down_count < 4 and self.board[col_index][temp_row] == val:
            temp_row += 1 # Moving down
            down_count += 1

        if up_count + down_count + 1 >= 4:
            return True

        # Diagonals (Axis 1)
        print("Diagonal Check going up right")
        up_diagonal_right_count = 0
        temp_col = col_index + 1 # Go right
        temp_row  = row_index - 1 # Go up

        while temp_row >= 0 and temp_col <= 6 and up_diagonal_right_count < 4  and self.board[temp_col][temp_row] == val:
            up_diagonal_right_count += 1 # add to the count
            temp_col += 1
            temp_row -= 1

        print("Diagonal Check going down left")
        down_diagonal_left_count = 0
        temp_col = col_index - 1 # Go left
        temp_row = row_index + 1 # Go down

        while temp_row <= 5 and temp_col >= 0 and down_diagonal_left_count < 4 and self.board[temp_col][temp_row] == val:
            down_diagonal_left_count += 1
            temp_row += 1
            temp_col -= 1

        if up_diagonal_right_count + down_diagonal_left_count + 1 >= 4:
            return True

        # Diagonal (Axis 2)
        print("Diagonal Check going up left")
        up_diagonal_left_count = 0
        temp_col = col_index - 1 # Go left
        temp_row = row_index - 1 # Go up

        while temp_row >= 0 and temp_col >= 0 and up_diagonal_left_count < 4 and self.board[temp_col][temp_row] == val:
            temp_col -= 1
            temp_row -= 1
            up_diagonal_left_count += 1

        print("Diagonal Check going down right")
        down_diagonal_right_count = 0
        temp_col = col_index + 1
        temp_row = row_index + 1

        while temp_row <= 5 and temp_col <= 6 and down_diagonal_right_count < 4 and self.board[temp_col][temp_row] == val:
            down_diagonal_right_count += 1
            temp_col += 1
            temp_row += 1

        if down_diagonal_right_count + up_diagonal_left_count + 1 >= 4:
            return True

        return False


def main():
    """Main function to run the Connect Four game practice."""
    game = ConnectFour()
    print("Welcome to Connect Four!")
    game.printBoard()

    game.gravity(3, 'o')
    game.gravity(2, 'o')
    game.gravity(2, 'o')
    game.gravity(2, 'o')
    game.gravity(1, 'o')
    game.gravity(1, 'o')
    row_index = game.gravity(0, 'o')
    print(f"row_index = {row_index}\n")
    game.printBoard()
    print(f"{game.checkWin('o', 2, row_index)}\n")


if __name__ == "__main__":
    main()
