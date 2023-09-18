import sys

import numpy as np
from Sudoku import SudokuBoard
import copy

class BackTrackSolver:
    def solve(self, board: SudokuBoard, row: int = 0, col: int = 0) -> SudokuBoard:
        board_size = board.board.shape[0]
        if row <= board_size - 1 and col <= board_size - 1:
            next_row, next_col = self.get_next_row_and_col(board, row, col)
            if board.board[row, col] == 0:
                for num in range(1, board_size + 1):
                    if board.is_save(num, row, col):
                        board.board[row, col] = num
                        result = self.solve(board, next_row, next_col)
                        if result is None:
                            board.board[row, col] = 0
                        else:
                            return result

            else:
                result = self.solve(board, next_row, next_col)
                if result is not None:
                    return result
        else:
            return board

    @staticmethod
    def get_next_row_and_col(board: SudokuBoard, row: int, col: int) -> tuple:
        row += (col + 1) // board.board.shape[0]
        col = (col + 1) % board.board.shape[0]
        return row, col


if __name__ == '__main__':
    board = SudokuBoard()
    board.board = np.array([[11, 9, 16, 0, 15, 0, 0, 2, 0, 0, 0, 14, 0, 10, 0, 0],
                            [5, 0, 14, 13, 1, 0, 8, 9, 2, 10, 0, 6, 0, 0, 0, 7],
                            [0, 0, 3, 0, 0, 0, 0, 6, 13, 0, 11, 0, 0, 4, 0, 15],
                            [7, 12, 0, 2, 0, 0, 10, 0, 8, 16, 0, 0, 0, 9, 0, 6],
                            [0, 10, 0, 0, 0, 1, 15, 0, 7, 0, 0, 0, 2, 5, 0, 0],
                            [0, 6, 1, 0, 4, 0, 0, 16, 0, 5, 12, 0, 0, 0, 9, 0],
                            [0, 0, 0, 0, 6, 0, 7, 0, 0, 1, 14, 16, 0, 8, 0, 0],
                            [0, 0, 0, 11, 0, 10, 15, 12, 0, 0, 8, 15, 3, 0, 0, 1],
                            [0, 0, 0, 14, 12, 0, 0, 0, 0, 13, 10, 0, 5, 2, 0, 16],
                            [12, 11, 0, 0, 0, 0, 13, 0, 1, 8, 0, 0, 0, 0, 0, 10],
                            [13, 0, 0, 0, 0, 14, 0, 0, 0, 0, 4, 7, 0, 0, 15, 0],
                            [0, 1, 10, 0, 5, 0, 6, 0, 3, 0, 0, 0, 4, 12, 11, 0],
                            [0, 5, 0, 7, 0, 12, 0, 8, 14, 6, 1, 0, 0, 0, 0, 9],
                            [16, 0, 0, 10, 0, 0, 1, 0, 0, 3, 7, 0, 11, 0, 5, 2],
                            [0, 0, 9, 4, 10, 0, 0, 14, 5, 0, 0, 0, 12, 0, 13, 3],
                            [0, 0, 6, 0, 0, 0, 3, 7, 0, 0, 9, 0, 1, 14, 8, 0]])

    solver = BackTrackSolver()
    result = solver.solve(copy.deepcopy(board))
    print(result.board)
