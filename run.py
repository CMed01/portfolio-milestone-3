# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    

def display_grid(width):
    """
    Builds game border and displays to terminal
    Header row contains numbers using the width parameter
    Remaining game grid consists of three rows that are repeated
    Using for loop in a for loop
    on both row and columne as per the width parameter:
       
    1st row =    |     |
    2nd row =  1 |  ?  |
    3rd row =    |_____|

    ? = mine_value
    """
    print("\t\t ChrisSweeper: Mine Hunter\n")

    # Prints header row from the width paraeter
    # Starting at number 1
    row = "   "
    for row_header in range(width):
        row = row + "     " + str(row_header + 1)
    
    print(row)

    # Prints the remainder of the game grid
    for row_std in range(width):
        # Prints the bottom header border
        row = "    "
        if row_std == 0:
            for column in range(width):
                row = row + "______"
            print(row)

        # prints the 1st row border
        row = "    |"
        for column in range(width):
            row = row + "     |"
        print(row)

        # prints second row
        row = str(row_std + 1) + "   |"
        for column in range(width):
            row = row + "  M" + "  |"
        print(row)

        # prints third row
        row = "    |"
        for column in range(width):
            row = row + "_____|"
        print(row)

    print()

grid_size = input("Please enter the game grd size (between 5-9)")
display_grid(int(grid_size))