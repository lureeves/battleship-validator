def validate_battlefield(field):

    # loop through (double for loops)
    # check every element for a hit
    # once a hit is found begin a checking funciton
        # check hit list set to see if already checked 
        # 
        # use flags, to check right, one to check below
        # if both flags are true, then return false
        # also check if diagonal is true
        # 
        # if right flag is true then go to the right, if another hit is found
        # keep going to the right until not hit is found or 5 blocks have been hit 
        # exit if 5 blocks have been hit
        # repeat the same checks but below for the vertical ships
        #
        # once a break is reached, store all preivious hit blocks locations 
        # in an array where each element is a ship and inside each eleement
        # is another set of the locations of each part of the ship 
        #
        # also store each one of the hits in a set 


    hit_set = set()
    ship_list = []
    orientation = ''

    def determine_ship_length(row, column, orientation):
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
    cruiser_count = 0
    destroyer_count = 0
    submarine_count = 0
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
            submarine_count += 1
    
    # return true if all ship counts are correct
    if battleship_count == 1 and cruiser_count == 2 and destroyer_count == 3 and submarine_count == 4:
        return True
    else:
        return False




battleField =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 1, 1, 0, 0, 1, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0]]

print(validate_battlefield(battleField))