import numpy as np

class SudokuBoard:
    def __init__(self):
        self._board = np.zeros((9, 9))

    @property
    def board(self) -> np.array:
        return self._board

    @board.setter
    def board(self, board: np.ndarray):
        if isinstance(board, np.ndarray):  # Make sure board is np numpy array.
            if self.is_square(board) and self.has_decimal_square_root(board.shape[0]):
                self._board = board.copy()
            else:
                print('Please enter square board with number of columns and rows have a square root')
        else:
            print('Please enter board as a square numpy array')

    def is_save(self, num: int, row: int, col: int) -> bool:
        '''
        Check if can put number in specific location in the board.
        :param num: number want to locate in specific position.
        :param row: row position.
        :param col: column position.
        :return: bool.
        '''
        if self.check_row(num, row) and \
                self.check_col(num, col) and \
                self.check_box(num, row, col):
            return True
        else:
            return False

    def check_row(self, num: int, row: int) -> bool:
        '''
        Check if can put number in specific row in the board.
        :param num: number want to locate in specific row.
        :param row: row position.
        :return: bool.
        '''
        if num in self._board[row]:
            return False
        else:
            return True

    def check_col(self, num: int, col: int) -> bool:
        '''
        Check if can put number in specific column in the board.
        :param num: number want to locate in specific column.
        :param col: column position.
        :return: bool.
        '''
        if num in self._board.T[col]:
            return False
        else:
            return True

    def check_box(self, num: int, row: int, col: int) -> bool:
        '''
        Check if can put number in specific box in the board.
        :param num: number want to locate in specific box.
        :param row: row position.
        :param col: column position
        :return: bool.
        '''
        box_size = int(np.sqrt(self._board.shape[0]))
        s_row = (row // box_size) * box_size
        s_col = (col // box_size) * box_size
        box = self._board[s_row: s_row + box_size, s_col: s_col + box_size].flatten()
        if num in box:
            return False
        else:
            return True

    @staticmethod
    def is_square(board: np.ndarray) -> bool:
        '''
        Check if ndarray is square.
        :param board: ndarray want to check.
        :return: bool
        '''
        return len(board.shape) == 2 and board.shape[0] == board.shape[1]


    @staticmethod
    def has_decimal_square_root(num: int) -> bool:
        '''
        Check if number has a square root or not.
        :param num: number want to check.
        :return : bool
        '''
        return np.sqrt(num) % 1 == 0

if __name__ == '__main__':
    board = SudokuBoard()
    board.board = np.array([[5, 4, 0, 0, 2, 0, 8, 0, 6],
                            [0, 1, 9, 0, 0, 7, 0, 0, 3],
                            [0, 0, 0, 3, 0, 0, 2, 1, 0],
                            [9, 0, 0, 4, 0, 5, 0, 2, 0],
                            [0, 0, 1, 0, 0, 0, 6, 0, 4],
                            [6, 0, 4, 0, 3, 2, 0, 8, 0],
                            [0, 6, 0, 0, 0, 0, 1, 9, 0],
                            [4, 0, 2, 0, 0, 9, 0, 0, 5],
                            [0, 9, 0, 0, 7, 0, 4, 0, 2]
                            ])
    #print(board.board)