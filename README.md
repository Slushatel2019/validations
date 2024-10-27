In this repo you can find various scripts to test some problems. For example, sudoku.py checks whether a Sudoku is valid or not.

About sudoku.py.

As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

- each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
- each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
- each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

This program:
1. reads 9 rows of the Sudoku, each containing 9 digits.
2. outputs result ("True" or "False") of each check(row, column, tile) and general result -  "Sudoku is Valid" or "Sudoku is Invalid".

About read_int.py.

Script acceptes input integer values and checks if they are within a specified range.

The function:

- accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
- if the user enters a string that is not an integer value, the function emits the message Error: wrong input, and ask the user to input the value again;
- if the user enters a number which falls outside the specified range, the function emits the message Error: the value is not within permitted range (min..max) and ask the user to input the value again;
- if the input value is valid, return it as a result.

This is how the function reacts to the user's input:

Enter a number from -10 to 10: 100
Error: the value is not within permitted range (-10..10)
Enter a number from -10 to 10: asd
Error: wrong input
Enter number from -10 to 10: 1
The number is: 1

