import unittest
from main import SudokuPole, main


class TestSudokuPole(unittest.TestCase):

    def test_init_valid_board(self):
        valid_board = [
            [".", "2", ".", "6", ".", "8", ".", ".", "."],
            ["5", "8", ".", ".", ".", "9", "7", ".", "."],
            [".", ".", ".", ".", "4", ".", ".", ".", "."],
            ["3", "7", ".", ".", ".", ".", "5", ".", "."],
            ["6", ".", ".", ".", ".", ".", ".", ".", "4"],
            [".", ".", "8", ".", ".", ".", ".", "1", "3"],
            [".", ".", ".", ".", "2", ".", ".", ".", "."],
            [".", ".", "9", "8", ".", ".", ".", "3", "6"],
            [".", ".", ".", "3", ".", "6", ".", "9", "."]
        ]
        sudoku = SudokuPole(valid_board)
        self.assertEqual(sudoku.pole, valid_board)

    def test_init_invalid_board(self):
        invalid_board = [
            [".", "2", ".", ".", ".", "8", ".", ".", "."],  # Short row
            ["5", "8", ".", ".", ".", "9", "7", ".", "."],
        ]
        with self.assertRaises(ValueError):
            SudokuPole(invalid_board)

    def test_get_row(self):
        board = [["." for _ in range(9)] for _ in range(9)]
        board[0][1] = "2"
        sudoku = SudokuPole(board)
        row = sudoku.get_row(sudoku.pole, 0, 0)
        self.assertEqual(row, {"2"})

    def test_get_col(self):
        board = [["." for _ in range(9)] for _ in range(9)]
        board[1][0] = "3"
        sudoku = SudokuPole(board)
        col = sudoku.get_col(sudoku.pole, 0, 0)
        self.assertEqual(col, {"3"})

    def test_get_block(self):
        board = [["." for _ in range(9)] for _ in range(9)]
        board[1][1] = "4"
        sudoku = SudokuPole(board)
        block = sudoku.get_block(sudoku.pole, 0, 0)
        self.assertEqual(block, {"4"})

    def test_verify_pole_valid(self):
        valid_board = [
            [".", "2", ".", "6", ".", "8", ".", ".", "."],
            ["5", "8", ".", ".", ".", "9", "7", ".", "."],
            [".", ".", ".", ".", "4", ".", ".", ".", "."],
            ["3", "7", ".", ".", ".", ".", "5", ".", "."],
            ["6", ".", ".", ".", ".", ".", ".", ".", "4"],
            [".", ".", "8", ".", ".", ".", ".", "1", "3"],
            [".", ".", ".", ".", "2", ".", ".", ".", "."],
            [".", ".", "9", "8", ".", ".", ".", "3", "6"],
            [".", ".", ".", "3", ".", "6", ".", "9", "."]
        ]
        self.assertTrue(SudokuPole.verify_pole(valid_board))

    def test_verify_pole_invalid(self):
        invalid_board = [
            [".", "2", ".", ".", ".", "8", ".", ".", "."],
            ["5", "8", ".", ".", ".", "9", "7", ".", "."],
        ]
        self.assertFalse(SudokuPole.verify_pole(invalid_board))

    def test_main_solvable(self):
        board = [
            [".", "2", ".", "6", ".", "8", ".", ".", "."],
            ["5", "8", ".", ".", ".", "9", "7", ".", "."],
            [".", ".", ".", ".", "4", ".", ".", ".", "."],
            ["3", "7", ".", ".", ".", ".", "5", ".", "."],
            ["6", ".", ".", ".", ".", ".", ".", ".", "4"],
            [".", ".", "8", ".", ".", ".", ".", "1", "3"],
            [".", ".", ".", ".", "2", ".", ".", ".", "."],
            [".", ".", "9", "8", ".", ".", ".", "3", "6"],
            [".", ".", ".", "3", ".", "6", ".", "9", "."]
        ]
        sudoku = SudokuPole(board)
        solved_sudoku = main(sudoku)
        self.assertNotEqual(solved_sudoku, "No solution!")

    def test_main_unsolvable(self):
        board = [
            ["5", "1", "6", "8", "4", "9", "7", "3", "2"],
            ["3", ".", "7", "6", ".", "5", ".", ".", "."],
            ["8", ".", "9", "7", ".", ".", ".", "6", "5"],
            ["1", "3", "5", ".", "6", ".", "9", ".", "7"],
            ["4", "7", "2", "5", "9", "1", ".", ".", "6"],
            ["9", "6", "8", "3", "7", ".", ".", "5", "."],
            ["2", "5", "3", "1", "8", "6", ".", "7", "4"],
            ["6", "8", "4", "2", ".", "7", "5", ".", "."],
            ["7", "9", "1", ".", "5", ".", "6", ".", "8"]
        ]
        sudoku = SudokuPole(board)
        solved_sudoku = main(sudoku)
        self.assertEqual(solved_sudoku, "No solution!")


if __name__ == "__main__":
    unittest.main()
