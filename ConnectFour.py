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

    def helperCount(self, val, col_index, col_step, row_index, row_step):
        count = 0
        col_index += col_step
        row_index += row_step
        while 0 <= col_index <= 6  and 0 <= row_index <= 5 and count < 4 and self.board[col_index][row_index] == val:
            col_index += col_step
            row_index += row_step
            count += 1
        return count

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

    def checkWinOptimize(self, val, col_index, row_index):
        # Horizontal Direction check
        print("Horizontal check going right (optimized)")
        right_count = self.helperCount(val, col_index, 1, row_index, 0)
        print("Horizontal check going left (optimized)")
        left_count = self.helperCount(val, col_index, -1, row_index, 0)

        if right_count + left_count + 1 >= 4:
            return True

        # Vertical Direction Check
        print("Vertical Check going up")
        up_count = self.helperCount(val, col_index, 0, row_index, -1)
        print("Vertical Check going down")
        down_count = self.helperCount(val, col_index, 0, row_index, 1)

        if up_count + down_count + 1 >= 4:
            return True

        # Positive Axis
        print("Check diagonal up and right")
        up_and_right = self.helperCount(val, col_index, 1, row_index, -1)
        print("Check diagonal down and left")
        down_and_left = self.helperCount(val, col_index, -1, row_index, 1)

        if up_and_right + down_and_left + 1 >= 4:
            return True

        # Negative Axis
        print("Check diagonal down and right")
        down_and_right = self.helperCount(val, col_index, 1, row_index, 1)
        print("Check diagonal up and left")
        up_and_left = self.helperCount(val, col_index, -1, row_index, -1)

        if down_and_right + up_and_left + 1 >= 4:
            return True

        return False

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

    def userMove(self, user_name: str, val: str):
        breakout = False

        while not breakout:
            col_no = input(f"{user_name} make move with {val}, give a column number.\n")

            if not col_no:
                print(f"{user_name} provide input!")
                continue

            if not col_no.isdigit():
                print(f"{user_name} provided invalid input, provide a integer")
                continue

            if int(col_no) not in range(7):
                print(f"Out of bounds! Choose a column between 0 and 6.")
                continue

            row_index = self.gravity(int(col_no), val)

            if row_index == -1:
                print(f"{user_name} provide another input, column is full!")
                continue

            self.printBoard()
            breakout = True

        return col_no, row_index

    def userInterface(self):
        moves = 0
        while True:
            moves +=1
            col_index, row_index = self.userMove("User 1", "o")
            if self.checkWinOptimize('o', int(col_index), row_index):
                print("User 1 has won!")
                return
            col_index, row_index = self.userMove("User 2", "x")
            if self.checkWinOptimize('x', int(col_index), row_index):
                print("User 2 has won!")
                return
            if moves >= 21:
                print(f"Its a Draw!.")
                return


def main():
    """Main function to run the Connect Four game practice."""
    game = ConnectFour()
    print("Welcome to Connect Four!")
    game.printBoard()

    game.userInterface()


if __name__ == "__main__":
    main()
