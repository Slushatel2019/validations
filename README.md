In this repo you can find various scripts to test some problems. For example, sudoku.py checks whether a Sudoku is valid or not.

About sudoku.py.

As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

- each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
- each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
- each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

This program:
1. reads 9 rows of the Sudoku, each containing 9 digits.
2. outputs result ("True" or "False") of each check(row, column, tile) and general result -  "Sudoku is Valid" or "Sudoku is Invalid".
3. test
