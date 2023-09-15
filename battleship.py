def validate_battlefield(field):
    """
    Validates the arrangement of ships in the battlefield.

    Args:
        field (list): A 2-dimensional list representing the battlefield.
                      Each element is either 0 (empty) or 1 (ship).

    Returns:
        bool: True if the arrangement of ships is valid, False otherwise.

    The function checks the battlefield for ships and ensures that the arrangement
    adheres to the following rules:
    - Ships cannot touch each other, including diagonally.
    - The number of ships must be as follows: 1 battleship (4 cells),
      2 cruisers (3 cells each), 3 destroyers (2 cells each), and
      4 submarines (1 cell each).

    The function iterates over the elements of the battlefield and performs the
    following steps:
    - For each hit (cell with a ship), a checking function is called to determine
      the length and orientation of the ship.
    - Ships are stored in a list of ship coordinates and added to a set of hit
      coordinates.
    - The function checks for diagonal hits, ship overlap, and determines the
      orientation of the ship.
    - The length of each ship is determined using a helper function.
    - After processing the battlefield, the counts of each ship type are compared
      against the expected counts to determine if the arrangement is valid.

    Example:
        field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        assert validate_battlefield(field) == True
    """


    hit_set = set()
    ship_list = []
    orientation = ''

    def determine_ship_length(row, column, orientation):
        """
        Determines the length of the ship based on its orientation.

        Args:
            row (int): The row index of the starting cell of the ship.
            column (int): The column index of the starting cell of the ship.
            orientation (str): The orientation of the ship ('right' or 'below').

        Returns:
            int: The length of the ship.
        """
        length = 1
        zero_found = False
        # check right
        if orientation == 'right':
            while zero_found == False:
                # check next space for hit if not last column
                if (column + length) <= 9 and field[row][column + length] == 1:
                    length += 1
                else:
                    zero_found = True
        # check below
        if orientation == 'below': 
            while zero_found == False:
                # check next space for hit if not last row
                if (row + length) <= 9 and field[row + length][column] == 1:
                    length += 1
                else:
                    zero_found = True
        return length


    # loop through every cell in list
    for row in range(len(field[0])):
        for column in range(len(field)):

            # checks for hits and are not in hit_set 
            if field[row][column] == 1 and (row, column) not in hit_set: 
                
                # checks diagonal right, if not end of row / column
                if row != 9 and column != 9 and field[row + 1][column + 1] == 1:
                        return False
                
                # check diagonal left, if not end of row / beginning of column
                if row != 9 and column != 0 and field[row + 1][column - 1] == 1: 
                    return False
                
                # checks if ships touch, if not end of row / column
                if column != 9 and row != 9 and field[row][column + 1] == 1 and field[row + 1][column] == 1:
                    return False 
                
                # determine if ship is horizontal or vertical
                if column != 9 and field[row][column + 1]:
                    orientation = 'right'
                else: 
                    orientation = 'below'
                
                # intializes / resets length
                ship_length = 1 
                
                # determine ship length
                ship_length = determine_ship_length(row, column, orientation)

                # initializies / resets list
                ship_coordinate_list = [] 
                
                # add ship to hit_set and ship_list
                if orientation == 'right':
                    for ship_coordinate in range(ship_length):
                        hit_set.add((row, column + ship_coordinate))
                        ship_coordinate_list.append([row, column + ship_coordinate])
                    ship_list.append(ship_coordinate_list)
                else:
                    for ship_coordinate in range(ship_length):
                        hit_set.add((row + ship_coordinate, column))
                        ship_coordinate_list.append([row + ship_coordinate, column])
                    ship_list.append(ship_coordinate_list)



    # count ships: 1 battleship (4 cell), 2 cruiser (3 cell),
    #              3 destroyer (2 cell), and 4 submarines (1 cell) 
    battleship_count = 0
    cruiser_count    = 0
    destroyer_count  = 0
    submarine_count  = 0
    ship_coordinates = []

    # adding appropriate ships
    for ship_coordinates in ship_list:
        if len(ship_coordinates) == 4:
            battleship_count += 1
        elif len(ship_coordinates) == 3:
            cruiser_count += 1
        elif len(ship_coordinates) == 2:
            destroyer_count += 1
        else:
            # if ship length is > 4 or = 1, then sub is incremented by 1
            submarine_count += 1
    
    # return true if all ship counts are correct
    if battleship_count == 1 and cruiser_count == 2 and destroyer_count == 3 and submarine_count == 4:
        return True
    else:
        return False

# example usage
battleField =  [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 1, 1, 0, 0, 1, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 1, 0]]

print(validate_battlefield(battleField))