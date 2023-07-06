# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    

def display_grid(height, width):
    """
    Builds game border and displays to terminal
    """
    print("\t\t Sweep the mines")
    
    empty_cell = "    "
    for h in range(height):
        row_border = empty_cell + str(h + 1)
        print(row_border)

    for w in range(width):
        column_border = empty_cell + str(h + 1)
        print(column_border)

    print()

display_grid(5, 4)