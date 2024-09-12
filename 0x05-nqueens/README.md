#N Queens Problem Solver

##Description
The N Queens Problem is a classic combinatorial problem where the objective is to place N queens on an N×N chessboard such that no two queens attack each other. This project implements a solution to the N Queens problem using the backtracking algorithm in Python.

The solution explores all possible configurations and prints out every valid arrangement where queens do not share the same row, column, or diagonal.

##Usage
To run the program, execute it from the command line with a single argument representing the size of the chessboard N.

```bash

./0-nqueens.py N

```
Example:
```bash

$ ./0-nqueens.py 4

[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```
This will print all valid solutions to the 4-queens problem, where each solution is represented by a list of lists. Each inner list contains two values: the row and column position of a queen.

##Requirements
- Python 3.x (tested on Python 3.4.3)
- Ubuntu 20.04 LTS

##Project Structure
```bash

0x05-nqueens/
├── 0-nqueens.py    # Main Python script for solving the N Queens problem
└── README.md       # Project documentation
```

##Installation
Clone this repository to your local machine:
```bash

git clone https://github.com/Gideon-Phiri/alx-interview.git
```
Navigate to the project directory:
```bash

cd 0x05-nqueens
```

##Algorithm
This project uses backtracking to solve the N Queens problem. The backtracking algorithm places queens on the chessboard one by one, row by row. At each step, it checks if the queen placement is valid:

No other queen can be in the same column.
No other queen can be on the same diagonal.
If a conflict occurs, the algorithm backtracks and tries a new configuration.


###Author
This project was implemented as part of the ALX Software Engineering Interview Preparation module.

Feel free to contribute, suggest optimizations, or report any issues! 
