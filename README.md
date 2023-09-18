# Battleship Field Validator 🚢

[![Codewars](https://img.shields.io/badge/Codewars-Problem-red?style=for-the-badge&logo=codewars)](https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python)

🎯 **Introduction:** Here is my solution to the Battleship Field Validator problem on Codewars.

---

## 📜 Problem Description
The problem challenges us to create a method that evaluates a field for the renowned board game "Battleship". It should return `True` if the field has a valid disposition of ships, and `False` otherwise. The field is a 10x10 two-dimensional array, with:
- `0`: The cell is free.
- `1`: The cell is occupied by a ship.

### 🚢 Battleship Rules (Soviet/Russian version):

- 🚤 There should be 4 submarines of 1 cell each.
- 🛥️ There should be 3 destroyers of 2 cells each.
- 🛳️ There should be 2 cruisers of 3 cells each.
- 🚢 One battleship of 4 cells.
- Every ship (except submarines) must be in a straight line.
- Ships can't overlap or touch either by side or corner.

---

## 🛠 Solution
The `validate_battlefield` function in Python verifies if the ships on the given field are arranged validly. It checks ship orientations, lengths, and coordinates, and counts each ship type to ensure the rules are met.

## 🚀 Usage
Invoke the `validate_battlefield` function by passing a 10x10 field represented as a 2-dimensional list. Each list item should be either `0` (empty) or `1` (ship). The function then determines if the ship arrangement is valid.

### Example usage:
    field =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    result = validate_battlefield(field)
    print(result)  # Output: True   
    
### 🤝 Contributing
Contributions to this repository are welcome. If you have any improvements or suggestions for the solution, please create a pull request.

### 📜 MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

