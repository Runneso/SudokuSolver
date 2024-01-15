class SudokuPole:
    def __init__(self, pole: list[list]):
        if not self.verify_pole(pole):
            raise ValueError("Invalid board!")
        self.pole = pole

    def __repr__(self):
        return repr(self.pole)

    def __str__(self):
        return str(self.pole)

    def __getitem__(self, index: int) -> list:
        return self.pole[index]

    def __setitem__(self, index: int, value: list):
        self.pole[index] = value

    @staticmethod
    def get_variants(pole: list[list], index_i: int, index_j: int):
        block = SudokuPole.get_block(pole, index_i, index_j)
        row = SudokuPole.get_row(pole, index_i, index_j)
        col = SudokuPole.get_col(pole, index_i, index_j)
        return block | row | col

    @staticmethod
    def get_row(pole: list[list], index_i: int, index_j: int):
        return set(pole[index_i]) - {"."}

    @staticmethod
    def get_col(pole: list[list], index_i: int, index_j: int):
        col = set()
        for index in range(9):
            col.add(pole[index][index_j])
        return col - {"."}

    @staticmethod
    def get_block(pole: list[list], index_i: int, index_j: int):
        index_i = index_i // 3 * 3
        index_j = index_j // 3 * 3
        block = set()
        for add_i in range(3):
            for add_j in range(3):
                block.add(pole[index_i + add_i][index_j + add_j])
        return block - {"."}

    @staticmethod
    def verify_pole(pole: list[list]) -> bool:

        if len(pole) != 9:
            return False

        if any(len(row) != 9 for row in pole):
            return False

        result = []
        for i in range(9):
            for j in range(9):
                element = pole[i][j]
                if element != '.':
                    result += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(result) == len(set(result))


def main(pole: SudokuPole):
    def solve(row, col):
        if row == 9:
            return True
        if col == 9:
            return solve(row + 1, 0)
        if pole[row][col] == ".":
            variants = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"} - SudokuPole.get_variants(pole.pole, row, col)
            for variant in map(str, range(1, 10)):
                if variant in variants:
                    pole[row][col] = variant
                    if solve(row, col + 1):
                        return True
                    else:
                        pole[row][col] = "."
            return False
        else:
            return solve(row, col + 1)

    if solve(0, 0):
        return pole
    return "No solution!"
