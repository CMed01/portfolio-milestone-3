# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Board:
    def __init__(self, square):
        self.square = square
    

def display_grid(square):
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
    for row_header in range(square):
        row = row + "     " + str(row_header + 1)
    
    print(row)

    # Prints the remainder of the game grid
    for row_std in range(square):
        # Prints the bottom header border
        row = "    "
        if row_std == 0:
            for column in range(square):
                row = row + "______"
            print(row)

        # prints the 1st row border
        row = "    |"
        for column in range(square):
            row = row + "     |"
        print(row)

        # prints second row
        row = str(row_std + 1) + "   |"
        for column in range(square):
            row = row + "  M" + "  |"
        print(row)

        # prints third row
        row = "    |"
        for column in range(square):
            row = row + "_____|"
        print(row)

    print()

def get_grid_size():
    """
    Gets grid size data from user input
    """
    while True:
        grid_value = input("Please enter the game grd size (between 5-9):  ")

        if validate_grid_size(grid_value):
            print("Data is valid")
            break
    
    return grid_value


def validate_grid_size(value):
    """
    Checks the user input and validates data
    Ensures number is a integer and between the value of 5 and 9
    """
    try:
        value = int(value)
        if value < 5 or value > 9:
            raise ValueError("Please enter a number between 5 and 9")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def main():
    """
    Main function of the game runs 
    """
    print("Welcome to ChrisSweeper:MineHunter")
    grid_size = get_grid_size()
    display_grid(int(grid_size))

main()