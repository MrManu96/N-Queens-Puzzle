import sqlalchemy as db
import pandas as pd

class NQueens:
    """Generate all valid solutions for the n queens puzzle"""
    def __init__(self, size, connection, emp, engine):
        # Store the board size, the number of valid solutions and the setup of connection to the database
        self.size = size
        self.connection = connection
        self.emp = emp
        self.engine = engine
        self.solutions = 0
        self.j = 1
        self.solve()

    def solve(self):
        """Solve the n queens puzzle and print the number of solutions"""
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print("Found", self.solutions, "solutions.")

    def put_queen(self, positions, target_row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to place a queen
        on the next row until all N queens are placed on the board.
        """
        # Stop case: when all N rows are occupied
        if target_row == self.size:
            #self.show_full_board(positions) #Show a board where Q represents a Queen and a point . is an empty space
            self.show_short_board(positions) #Show the position of each queen per row in form of a list
            self.solutions += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (column and diagonal positions)
        """
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:

                return False
        return True

    def show_full_board(self, positions):
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def show_short_board(self, positions):
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

        #Inserting record one by one into the table
        query = self.emp.insert().values(positions=str(line))
        ResultProxy = self.connection.execute(query)
        

def main():
    #n = int(input("Please enter number of queens: "))

    #Connection to Database and creation of engine
    engine = db.create_engine('postgresql://postgres:password@localhost:5432/queens')

    connection = engine.connect()
    metadata = db.MetaData()

    #Iterating through n: Maximum n with processing within 10 minutes is 14
    for n in range(8,15):

        emp = db.Table(str(n), metadata,
            db.Column('Id', db.Integer(), primary_key = True),
            db.Column('positions', db.String(255)) #nullable = False
            )

        metadata.create_all(engine) #Creates the table

        NQueens(n, connection, emp, engine)

if __name__ == "__main__":
    # Execute only if run as a script
    main()