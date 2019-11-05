
class NQueens:
    def __init__(self, size):
        self.size = size
        self.solutions = 0

    def solve(self):
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print("Found", self.solutions, "solutions.")
        return self.solutions

    def put_queen(self, positions, target_row):
        if target_row == self.size:
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:

                return False
        return True
        

def queens(n):
    return NQueens(n).solve()

# Test cases: 8 <= n <= 14
def test_queens():
    assert queens(8) == 92
    assert queens(9) == 352
    assert queens(10) == 724
    assert queens(11) == 2680
    assert queens(12) == 14200
    assert queens(13) == 73712
    #assert queens(14) == 365596
