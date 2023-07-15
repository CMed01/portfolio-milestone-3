"""
ChriSweeper: Mine Hunter game
------------------
Aim of the game is to identify all the mines
within the number of attempts
"""

import random
import os


def display_grid(square, mines):
    """
    Builds game border and when called displays to terminal
    Header row contains numbers using the square parameter
    Remaining game grid consists of three rows that are repeated
    Using for loop in a for loop
    on both row and columne as per the square parameter:
    1st row =    |     |
    2nd row =  1 |  ?  |
    3rd row =    |_____|
    ? = mine_value, this will either be blank, number or M
    """
    clear()
    print("ChrisSweeper: Mine Hunter\n")
    print("-------------------------------------------")
    print("Instructions:")
    print("")
    print("-------------------------------------------")

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

        # prints second row including user display,
        # either blank, number or mine
        row = str(row_std + 1) + "   |"
        for column in range(square):
            row = row + "  " + str(mines[row_std][column]) + "  |"
        print(row)

        # prints third row
        row = "    |"
        for column in range(square):
            row = row + "_____|"
        print(row)

    print()


def get_grid_size():
    """
    User can input a value bewteen 4 and 9
    Data input is validated using a seperate function
    Once number is valid, this value is passed to several functions
    to display grid and generate mines
    """
    while True:
        grid_size = input("Please enter the game grd size (between 5-9):  ")

        if validate_grid_size(grid_size):
            break

    grid_size = int(grid_size)
    return grid_size


def validate_grid_size(value):
    """
    Input value from user is checked to ensure it is
    an integer and is between the values of 5 and 9
    If value does not meet criteria then a value error is displayed
    promting user to input the correct value
    Correct input is passed badk to get_grid_size
    """
    try:
        value = int(value)
        if value < 5 or value > 9:
            raise ValueError("Please enter a number between 5 and 9")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def generate_grid_values(grid_size):
    """
    Function passes grid_size and generate a nested list
    The number of nested list will depend on the grid_size
    I.e. if grid_size = 5
    then list will be 5 lists of 5 numbers each with value of 0
    [[0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]
    """
    grid_values = [[0 for x in range(grid_size)] for y in range(grid_size)]

    return grid_values


def generate_random_mines(grid_values):
    """
    Function passes grid_values (which is a nested list)
    Grid_size value is used to generate 2 random numbers
    These two numbers are then used as index numbers to grid_values
    and will amend the value of nested list.
    I.e. if number generated are 2 1, then list 1 and value 0 will
    be ameneded as below to -1
    [[0,0,0,0,0],
    [-1,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]
    """
    counter = 0

    while counter < grid_size:

        num1 = random.randint(1, grid_size**2-1)
        num2 = random.randint(1, grid_size**2-1)
        x = num1 // grid_size
        y = num2 % grid_size

        if grid_values[x][y] != -1:
            counter += 1
            grid_values[x][y] = -1

    return grid_values


def update_grid_numbers(grid_values):
    """
    This function will pass the grid_values and using
    the range from grid_size as index numbers.
    Each index of the nested list will be interrogated
    All surrounding values suing vextor method will be checked
    Any surrounding grid with a value of -1 will add to the count.
    Once the loop has completed the total value will be passed to
    the grid_value index.
    The aim of this function will update the nested list so that
    when displayed to the user, it will inform the user of the
    number of mines surrouding the cell revealed.
    I.e. if 4 then there are 4 mines in the surroind 8 cells.
    """
    for x in range(grid_size):
        for y in range(grid_size):
            # Passes index number to iterate through all grid_values
            if grid_values[x][y] == -1:
                continue

            # Check top grid space
            if x >= 1 and grid_values[x-1][y] == -1:
                grid_values[x][y] = grid_values[x][y] + 1
            # Check top-right grid space
            if x >= 1 and y < grid_size-1 and grid_values[x-1][y+1] == -1:
                grid_values[x][y] = grid_values[x][y] + 1
            # Check right grid space
            if y < grid_size - 1 and grid_values[x][y+1] == -1:
                grid_values[x][y] = grid_values[x][y] + 1
            # Check bottom-right grid space
            if (x < grid_size - 1 and y < grid_size-1 and
                    grid_values[x+1][y+1] == -1):
                grid_values[x][y] = grid_values[x][y] + 1
            # Check bottom grid space
            if x < grid_size - 1 and grid_values[x+1][y] == -1:
                grid_values[x][y] = grid_values[x][y] + 1
            # Check bottom-left grid space
            if x < grid_size - 1 and y >= 1 and grid_values[x+1][y-1] == -1:
                grid_values[x][y] = grid_values[x][y] + 1
            # Check left grid space
            if y >= 1 and grid_values[x][y-1] == -1:
                grid_values[x][y] = grid_values[x][y] + 1
            # Check top-left grid space
            if x >= 1 and y >= 1 and grid_values[x-1][y-1] == -1:
                grid_values[x][y] = grid_values[x][y] + 1
    return grid_values


def generate_display_values(value):
    """
    Simialr to generate_ grid_values function
    passes grid_size and generate a nested list
    The number of nested list will depend on the grid_size
    I.e. if grid_size = 5
    then list will be 5 lists of 5 blank string values each with value of " "
    [[" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "]]
    This will be used to display empty cells to the user
    """

    display_values = [[" " for x in range(value)] for y in range(value)]

    return display_values


def reveal_answers(grid_values):
    """
    This function passes the nested list grid_values
    This function will iterate through this nested list
    using the grid_size value to generate index numbers
    The grid_values list is updated to change -1 values to "M"
    This new nested list will then be used to display
    grid values to the user when the game_over variable is false
    """
    answer_values = [[" " for x in range(grid_size)] for y in range(grid_size)]

    for x in range(grid_size):
        for y in range(grid_size):
            if grid_values[x][y] == -1:
                answer_values[x][y] = "M"
            else:
                answer_values[x][y] = grid_values[x][y]

    return answer_values


def clear():
    """
    Clears the terminal
    """
    os.system("clear")


def main():
    """
    This function contains the main game logic and is called when the terminal
    is loaded after the user inputs the intended grid_size.
    The game loop runs when the game_over variable is False.
    The number of attempts left and the number of mines left to find
    are calculated using the grid_size
    Both these values are then displayed to the terminal.
    The diaplay_grid function is called and displayed a grid with blank cells
    A user input is displayed with clear instructions for valid input
    The input variables are checked and once validated the numbers are
    used as index values to iterate through the grid_values
    and then the display_values are printed to the terminal.
    Each attempts that successfully identifies a mine deducts one
    from the mines_left only.
    Each attempt that is unsuccessful in identifying a mine deducts one from
    the life counter only.
    The terminal is then cleared and an updated grid is displayed.
    The game is over when all mines have been found or the life_counter = 0.
    At the point the display grid is updated to show all values.
    """

    game_over = False
    life_counter = grid_size * 2
    mines_left = grid_size

    display_grid(grid_size, display_values)
    print(f"Number of attempts left: {life_counter}")
    print(f"Mines left: {(mines_left)}")

    # While loop for game function
    while game_over is not True:
        # User input as coordinates
        user_mine_guess = input("Enter the coordinates here:  ").split()

        # checks validity of user input and returns error message
        # Checks is inut lenght is not 2
        if len(user_mine_guess) != 2:
            print(
                f"Please try again and enter two single \
                    numbers between 1 and {grid_size}")
        else:
            # Checks is values are intergers
            # if not then returns a Value Error
            # If interger then generate 1 list of 2 numbers
            try:
                user_input = list(map(int, user_mine_guess))

                # If numbers in new list are values <1 or
                # > grid_size then returns an error message
                if (user_input[0] < 1 or user_input[0] > grid_size or
                        user_input[1] < 1 or user_input[1] > grid_size):
                    print(f"Please try again and enter two \
                        single numbers between 1 and {grid_size}")
                    continue
                else:
                    # If numbers valid, then passed as index values
                    x = user_input[0] - 1
                    y = user_input[1] - 1

                    # Valid input values used to iterate over grid_values
                    # if value -1 (i.e. mine) then mine counter reduced by 1
                    # display_value updated
                    # terminal cleared and updated grid displayed
                    if grid_values[x][y] == -1:
                        clear()
                        mines_left = mines_left - 1
                        display_values[x][y] = "M"
                        display_grid(grid_size, display_values)
                        print("BOOM!!! You have found a mine, good hunting")
                        print(f"Number of attempts left: {life_counter}")
                        print(f"Mines left: {(mines_left)}")

                        # After above, if mines_left = 0
                        # All mines have been found and winning message printed
                        if mines_left == 0:
                            clear()
                            display_grid(grid_size, answer_values)
                            print(f"BOOM, BOOM, BOOM, you have found all the \
                                 mines with {life_counter} lives remaining")
                            print("Well Done! Give the Mine Hunt another go")
                            game_over = True

                    # if value != -1
                    # # i.e. not mine, then life counter reduced by 1
                    # display_value updated
                    # terminal cleared and updated grid displayed
                    else:
                        clear()
                        life_counter = life_counter - 1
                        display_values[x][y] = grid_values[x][y]
                        display_grid(grid_size, display_values)
                        print("Close, keep hunting for all those mines")
                        print(f"Number of attempts left: {life_counter}")
                        print(f"Mines left: {(mines_left)}")
                        # After above, if life counter = 0
                        # Then all lives user game over message printed
                        if life_counter == 0:
                            display_grid(grid_size, answer_values)
                            print("You have used all your attempts, \
                                try again to find all the mines")
                            game_over = True
            except ValueError:
                print(f"Please try again and enter two \
                    single numbers between 1 and {grid_size}")
                continue


print("")
print("Welcome to ChrisSweeper: MineHunter\n")

# Stores the grid_size after user inputs value
grid_size = get_grid_size()

# Generate initial grid_values
grid_values = generate_grid_values(grid_size)

# Update grid_values after mines generated
grid_values = generate_random_mines(grid_values)

# Updates remaining gird values
grid_values = update_grid_numbers(grid_values)

# Generate values to be displayed to user
display_values = generate_display_values(grid_size)

# Updates grid_values to be displayed when game over or won
answer_values = reveal_answers(grid_values)

# Main game function called when terminal loaded and grid_size input recieved
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("The game has ended \n")
