""" Program to solve a Sudoku board
"""

class Sudoku:

    # working areas
    rows = [0] * 9
    cols = []
    for i in xrange(9):
        cols.append([0]*9)

    squares = []
    for i in xrange(3):
        squares.append([0]*9)

    # clear the working area
    def clear(self):
        self.reset_row()
        for i in xrange(3):
            for j in xrange(9):
                self.squares[i][j] = 0
        for i in xrange(9):
            for j in xrange(9):
                self.cols[i][j] = 0

    # @parm value, the value on board
    # @return a boolean as valid or not
    def check_row(self, value):
        #print "row    %s %d" % (self.rows, value)
        
        if self.rows[value-1] != 0:
            return False
        self.rows[value-1] = value
        return True

    # @parm value, the value on board
    # @parm col, the col index on board
    # @return a boolean as valid or not
    def check_col(self, value, col):
        #print "col    %s %d" % (self.cols[col], value)

        if self.cols[col][value-1] != 0:
            return False
        self.cols[col][value-1] = value
        return True

    # @parm value, the value on board
    # @parm row, col, the row and col index on board
    # @return a boolean as valid or not
    def check_square(self, value, col):
        square_index = col / 3

        #print "square %s %d" % (self.squares[square_index], value)

        if self.squares[square_index][value-1] != 0:
            return False
        self.squares[square_index][value-1] = value
        return True


    def reset_square(self, col):
        for i in xrange(9):
            self.squares[col/3][i] = 0

    def reset_row(self):
        for i in xrange(9):
            self.rows[i] = 0

    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        #print board
        self.clear()
        for row in xrange(9):
            for col in xrange(9):
                value = board[row][col]
                if value == '.':
                    value = 0
                else:
                    value = int(value)
                if value != 0 and (not self.check_row(value) or \
                        not self.check_col(value, col) or \
                        not self.check_square(value, col)):
                        return False
                if (row+1) % 3 == 0 and (col+1) % 3 == 0:
                    self.reset_square(col)
            self.reset_row()
        #print "good"
        print board
        return True

    def find_next(self, board):
        for row in xrange(9):
            if board[row].find(".") >= 0:
                return row
        return -1

    def fill(self, board):
        row = self.find_next(board)
        if row == -1:
            return 0

        for i in range(1, 10):
            save = ''.join(board[row])
            board[row] = board[row].replace('.', "%d" % i, 1)
            if not self.isValidSudoku(board):
                board[row] = save
            else:
                # continue to next empty space, if can not find one, try next value
                if self.fill(board) == -1:
                    board[row] = save
                else:
                    return 0

        # can not find a valid one, back track
        return -1

if __name__ == '__main__':

    # unfilled Sudoku board in 2d array
    board=[".31......",
           "...74....",
           "9....37..",
           "5..61..3.",
           ".2.....5.",
           ".9..58..2",
           "..83....5",
           "....89...",
           "......16."]
    
    import time
    pre = time.time() 

    # run the program to fill the board
    Sudoku().fill(board)

    print board
    print "%s seconds" % (time.time() - pre)

