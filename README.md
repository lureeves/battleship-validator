Battleship Field Validator
This repository contains a solution to the Battleship Field Validator problem on Code Wars.

Problem Description
The problem requires writing a method that takes a field for the well-known board game "Battleship" as an argument and returns True if it has a valid disposition of ships, False otherwise. The field is guaranteed to be a 10x10 two-dimensional array, where elements in the array are numbers: 0 if the cell is free and 1 if occupied by a ship.

The rules for the Battleship game, specifically the Soviet/Russian version, are as follows:

There must be a single battleship of size 4 cells.
There must be 2 cruisers of size 3 cells each.
There must be 3 destroyers of size 2 cells each.
There must be 4 submarines of size 1 cell each.
Each ship must be a straight line, except for submarines which are single cells.
Ships cannot overlap or be in contact with any other ship, neither by edge nor by corner.
Solution
The provided solution is implemented as the validate_battlefield function in Python. The function takes a 10x10 field as input and checks whether the arrangement of ships in the field is valid. It returns True if the arrangement is valid, and False otherwise.

The solution loops through the field, checks for hits, determines ship lengths and orientations, stores ship coordinates, and counts the number of each ship type. It applies the specified rules to validate the arrangement.

Usage
To use the validate_battlefield function, pass a 10x10 field represented as a 2-dimensional list to the function. Each element of the list should be either 0 (empty) or 1 (ship). The function will return True if the arrangement of ships is valid and False otherwise.

Example usage: