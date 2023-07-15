"""
Imports
"""
import random
import os


def display_grid(square, mines):
    """
    Displays game grid to terminal and inserts values

    Function takes two parameters
    square =which is determined by the user - value between 5 and 9
    mines = display value depending on stage of game
    Grid is outlined by numbers identifying the row and column
    Remaining game grid consists of three rows that are repeated
    Using for loop in a for loop on both row and columne
    as per the square parameter:
    1st row =    |     |
    2nd row =  1 |  ?  |
    3rd row =    |_____|
    ? = mine_value, this will either be blank, number or M
    """
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
    Stores the a value of the grid following user input

    User inputs a value bewteen 5 and 9
    Data input is validated using a seperate function
    Once validated valid, value is stored in a variable grid
    """
    while True:
        grid_input = input("Please enter the game grd size (between 5-9):\n")

        if validate_grid_size(grid_input):
            break

    grid = int(grid_input)
    return grid


def validate_grid_size(value):
    """
    Validates the number inputted for grid size

    Input is valid if an integer and between 5 and 9
    If value is not valid, a value error is displayed and user can retry
    Valid input returns True
    """
    try:
        value = int(value)
        if value < 5 or value > 9:
            raise ValueError("Please enter a number between 5 and 9")

    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False

    return True


def generate_grid_values(value):
    """
    Generates a nested list, with values of 0

    Function passes grid_size and generates a nested list
    The number of nested liss and the values inside each list
    will depend on the grid_size. I.e. if grid_size = 5
    then list will be 5 lists of 5 numbers each with value of 0
    [[0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]
    """
    grid_values = [[0 for x in range(value)] for y in range(value)]

    return grid_values


def generate_random_mines(grid):
    """
    Updates selected values of nested list with values of -1

    Function passes grid_values (which is a nested list)
    Two random numbers are generted and used as index numbers
    to update the value.index of a nested list.
    Number of iterations is determined by the grid_size
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

        if grid[x][y] != -1:
            counter += 1
            grid[x][y] = -1

    return grid


def update_grid_numbers(value):
    """
    Updates nested list with a value showing how many mines are surrounding

    This function will pass the grid_values and using the range from
    grid_size as index numbers.
    Each index of the nested list will interrogate all surrounding values.
    Any surrounding values with a value of -1 will add to the count.
    Once the loop has completed the total value will be passed to the
    grid_value index.
    I.e. if 4 then there are 4 mines in the surroind 8 cells.
    """
    for x in range(grid_size):
        for y in range(grid_size):
            # Passes index number to iterate through all grid_values
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
            if (x < grid_size - 1 and y < grid_size-1 and
                    value[x+1][y+1] == -1):
                value[x][y] = value[x][y] + 1
            # Check bottom grid space
            if x < grid_size - 1 and value[x+1][y] == -1:
                value[x][y] = value[x][y] + 1
            # Check bottom-left grid space
            if x < grid_size - 1 and y >= 1 and value[x+1][y-1] == -1:
                value[x][y] = value[x][y] + 1
            # Check left grid space
            if y >= 1 and value[x][y-1] == -1:
                value[x][y] = value[x][y] + 1
            # Check top-left grid space
            if x >= 1 and y >= 1 and value[x-1][y-1] == -1:
                value[x][y] = value[x][y] + 1
    return value


def generate_display_values(value):
    """
    Generates a nested list, with values of " "

    Function passes grid_size and generates a nested list.
    The number of nested lists and the values inside each list will
    depend on the grid_size
    I.e. if grid_size = 5 then list will be 5 lists of 5 strings each
    with an empty value.
    [[" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "]]
    This will be used to display empty cells to the user
    """

    visible_grid = [[" " for x in range(value)] for y in range(value)]

    return visible_grid


def reveal_answers(grid):
    """
    Generates a nested list, with values of M and numbers

    This function passes the nested list grid_values and iterates through it
    using the grid_size value to generate index numbers.
    The grid_values list is updated to change -1 values to "M"
    This new nested list will then be used to display
    grid values to the user when the game_over variable is false
    """
    answer_values = [[" " for x in range(grid_size)] for y in range(grid_size)]

    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] == -1:
                answer_values[x][y] = "M"
            else:
                answer_values[x][y] = grid[x][y]

    return answer_values


def clear():
    """
    Clears the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def title():
    """
    Prints the title of the game and intructions to the terminal
    """
    clear()
    print("ChrisSweeper: Mine Hunter\n")
    print("Instructions:")
    print("1. Find all the mines without using all lives")
    print("2. Enter two numbers seperated by a space to reveal square")
    print("   first number is the x axis and second is th y axis")
    print("3. M = mine, number = number of surrounding mines")
    print("-------------------------------------------")

    # Added extra blank print statement so that the above remains available
    # in terminal on deployed website.
    # os.system("clear") does not clear the full terminal in Heroku.
    print("    ")


def main():
    """
    Main function containing game logic

    Called to the terminal when loaded after grid_size input from user.
    The game loop runs when the game_over variable is False.
    The number of attempts left and the number of mines left to find
    are calculated using the grid_size.
    Both these values are then displayed to the terminal.
    The diaplay_grid function is called and displays a grid with blank cells.
    A user input is displayed with clear instructions for valid input
    The input variables are checked and once validated the numbers are
    used as index values to iterate through the grid_values and then the
    display_values are printed to the terminal.
    Each attempts that successfully identifies a mine deducts one from the
    mines_left only.
    Each attempt that is unsuccessful in identifying a mine deducts one from
    the life counter only.
    The terminal is then cleared and an updated grid is displayed.
    The game is over when all mines have been found or the life_counter = 0.
    At the point the display grid is updated to show all values.
    """

    game_over = False
    life_counter = grid_size * 2
    mines_left = grid_size

    title()

    display_grid(grid_size, display_values)
    print(f"Number of attempts left: {life_counter}")
    print(f"Mines left: {(mines_left)}")

    # While loop for game function
    while game_over is not True:
        # User input as coordinates
        user_mine_guess = input("Enter the coordinates here:\n").split()

        # checks validity of user input and returns error message
        # Checks is inut lenght is not 2
        if len(user_mine_guess) != 2:
            print("Try again")
            print(f"Enter two numbers between 1 and {grid_size}")
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
                    print("Try again")
                    print(f"Enter two numbers between 1 and {grid_size}")
                    continue
                else:
                    # If numbers valid, then passed as index values
                    x = user_input[0] - 1
                    y = user_input[1] - 1

                    # Checks if coordinates already guessed
                    if display_values[x][y] != " ":
                        print("Already guessed this one")
                        continue

                    # Valid input values used to iterate over grid_values
                    # if value -1 (i.e. mine) then mine counter reduced by 1
                    # display_value updated
                    # terminal cleared and updated grid displayed
                    if mine_grid[x][y] == -1:
                        mines_left = mines_left - 1
                        display_values[x][y] = "M"
                        clear()
                        display_grid(grid_size, display_values)
                        print("BOOM!!! You have found a mine, good hunting")
                        print(f"Number of attempts left: {life_counter}")
                        print(f"Mines left: {(mines_left)}")

                        # After above, if mines_left = 0
                        # All mines have been found and winning message printed
                        if mines_left == 0:
                            clear()
                            display_grid(grid_size, answer_grid)
                            print("BOOM, BOOM, you have found all the mines")
                            print(f"with {life_counter} lives remaining")
                            print("Well Done! Give the Mine Hunt another go")
                            print("Click Run Program button to try again")
                            game_over = True

                    # if value != -1
                    # # i.e. not mine, then life counter reduced by 1
                    # display_value updated
                    # terminal cleared and updated grid displayed
                    else:
                        life_counter = life_counter - 1
                        display_values[x][y] = mine_grid[x][y]
                        clear()
                        display_grid(grid_size, display_values)
                        print("Close, keep hunting for all those mines")
                        print(f"Number of attempts left: {life_counter}")
                        print(f"Mines left: {(mines_left)}")
                        # After above, if life counter = 0
                        # Then all lives user game over message printed
                        if life_counter == 0:
                            clear()
                            display_grid(grid_size, answer_grid)
                            print("You have used all your attempts")
                            print("Click Run Program button to try again")
                            game_over = True
            except ValueError:
                print("Try again")
                print(f"Enter two numbers between 1 and {grid_size}")
                continue


print("Welcome to ChrisSweeper: MineHunter\n")

# Stores the grid_size after user inputs value
grid_size = get_grid_size()

# Generate initial grid_values
initial_grid = generate_grid_values(grid_size)

# Generate values to be displayed to user
display_values = generate_display_values(grid_size)

# Update grid_values after mines generated
grid_and_mine_values = generate_random_mines(initial_grid)

# Updates remaining gird values
mine_grid = update_grid_numbers(grid_and_mine_values)

# Updates grid_values to be displayed when game over or won
answer_grid = reveal_answers(mine_grid)

# Main game function called when terminal loaded and grid_size input recieved
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("The game has ended \n")
