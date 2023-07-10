# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

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
    # row-std = standard
    for row_std in range(square):
        # Prints the bottom border for the header
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

        # prints second row including set_mine
        row = str(row_std + 1) + "   |"
        for column in range(square):
            row = row + "  " + str(display_values[row_std][column]) + "  |"
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
        grid_size = input("Please enter the game grd size (between 5-9):  ")

        if validate_grid_size(grid_size):
            print("Data is valid")
            break

    grid_size = int(grid_size)
    
    return grid_size


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
 

def grid_values(value):
    """
    Add numerical values to grid
    """
    grid_values = [[0 for x in range(value)] for y in range(value)]

    return grid_values


def generate_random_mines(value):
    """
    Generate random mine positions based on grid_size
    """
    counter = 0

    while counter < grid_size:

        num1 = random.randint(1, grid_size**2-1)
        num2 = random.randint(1, grid_size**2-1)
        
        x = num1 // grid_size
        y = num2 % grid_size

        if value[x][y] != -1:
            counter += 1
            value[x][y] = -1

    return value


def update_grid_numbers(value):
    for x in range(grid_size):
        for y in range(grid_size):

            if value[x][y] == -1:
                continue
            
            # Check top grid space
            if x >= 1 and value[x-1][y] == -1:
                value[x][y] = value[x][y] + 1
            # Check top-right grid space
            if x >= 1 and y < grid_size-1 and value[x-1][y+1] == -1:
                value[x][y] = value[x][y] + 1
            # Check right grid space
            if y < grid_size - 1 and value[x][y+1] == -1:
                value[x][y] = value[x][y] + 1
            # Check bottom-right grid space
            if x < grid_size - 1  and y < grid_size-1 and value[x+1][y+1] == -1:
                value[x][y] = value[x][y] + 1
            # Check bottom grid space
            if x < grid_size - 1 and value[x+1][y] == -1:
                value[x][y] = value[x][y] + 1
            # Check bottom-left grid space
            if x < grid_size - 1  and y >= 1 and value[x+1][y-1] == -1:
                value[x][y] = value[x][y] + 1
            # Check left grid space
            if y >= 1 and value[x][y-1] == -1:
                value[x][y] = value[x][y] + 1
            # Check top-left grid space
            if x >= 1 and y >= 1 and value[x-1][y-1] == -1:
                value[x][y] = value[x][y] + 1
        
    return grid_values

def display_values(value):
    """
    Change list numeration to blank for display to console.
    """

    display_values = [[" " for x in range(value)] for y in range(value)]

    return display_values

def main():
    """
    Main function of the game runs 
    """
    print("Welcome to ChrisSweeper:MineHunter")
    display_grid(int(grid_size))

  
    


grid_size = get_grid_size()
grid_values = grid_values(grid_size)
grid_values = generate_random_mines(grid_values)
grid_values = update_grid_numbers(grid_values)

display_values = display_values(grid_size)

main()

game_over = False

while game_over is not True:
    user_input = []
    user_mine_guess = input("Enter the coordinates here:  ").split()
