# SnakeExercise

## Algorithm and data structures
Consider a rectangular board consisting of n×m cells. There is a snake lying on some of the cells, and all of the other cells are empty. The snake consists of one or more cells such that cells with consecutive numbers are either horizontally or vertically adjacent. The first cell is the snake's head, and the last cell is the snake's tail.
On each turn, the snake's head moves to one of the horizontally or vertically adjacent cells, the second cell of the snake moves to the cell where the head was situated, the third cell takes the former place of the second cell, etc. All these movements happen simultaneously, so the head could potentially take the place of the tail. There are two configurations of the snake's cells that are prohibited: self-intersection (meaning that after each step any pair of snake cells should have pairwise different coordinates), and crossing the board's border. The path is a sequence of characters L, R, D, and U(corresponding to left, right, down, and up, respectively) describing the movements of snake's head on each turn. How many distinct valid paths of length p can the snake make on the board?


### Example
For board = [ 4, 3], snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]],and depth = 3, the output should be “numberOfAvailableDifferentPaths(board, snake, depth) = 7”.
Here are all of the valid paths with a length of 3 that the snake can make:
* LLU 
* LUR 
* LUL 
* ULL 
* ULD 
* LUU 
* ULU

## Used Libraries
- Numpy
- Copy
- intertools
- argparse

## How to execute it

1. Clone this repo
> git clone https://github.com/gerardburgues/SnakeExercise.git
3. Execute program
> python main.py --row #add_number --col ##add_number --snake ##add_number --depth ##add_number
