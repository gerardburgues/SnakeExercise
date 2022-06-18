import numpy as np
from itertools import combinations, product
import copy
import argparse


def init_snake(grid, snake,fresh):
    """
    init_array: Start position of the snake
    snake: Cells where the snake appears
    fresh: init snake that never changes
    Initialize the grid and snake position
    """
    init_array =  np.zeros(shape=grid)
    snake = copy.deepcopy(fresh) # Saving the original snake
    
    #Setting snake
    for i in range(0,len(snake)):
        init_array[snake[i][0],snake[i][1]] = 1
    return init_array,snake

def update_matrix(snake,matrix):   
    """
    matrix: Start position of the grid
    snake: Cells where the snake appears
    Updating matrix visualization
    """
    for i in range(0,len(snake)):
        matrix[snake[i][0],snake[i][1]] = 1
    print("Showing updated matrix")
    print(matrix)

def possible_combinations(depth):
    """
    depth: max number of combinations to consider 

    This function creates all the possible combinations
    for the snake to move.
    """
    sample_list =  ['Left', 'Right', 'Up','Down']
    combinations = [p for p in product(sample_list, repeat=depth)]
   
    return combinations

def move_snake(combinations, init_array, snake):
    """
    combinations: All possible combinations of movement
    init_array: Start position of the snake
    snake: Cells where the snake appears
    
    This function moves the snake and add the correct result
    to a list. 
    """

    cont = 0
    resultant_array = []
    for i in combinations:
        init_array, snake = init_snake(grid,snake,fresh)
        if direction_snake(init_array, snake, i) == True:
            cont +=1
            resultant_array.append(i)

    return cont, resultant_array
    

def direction_snake(matrix, snake, comb):
    """
    matrix: start position of the snake
    snake: cells where the snake appears
    comb: All possible combinations of movements
    returns:
        True if we can move the snake
        False if we can't move the snake
    """
    
    """
    For each iteration we are going to do the movement.
    Taking into account:
        * overlapping of position => ERROR
        * stepping out of the grid => ERROR
    """

    bold = True  #If its False means there is ERROR
    for i in comb:  #Looping over movements combinations
        previous_pos = copy.copy(snake[0])
        matrix[snake[-1][0],snake[-1][1]] = 0    
        if i == 'Left':   
            snake[0][1]= snake[0][1]-1
            if snake[0][1] >= 0  :
                for i in range(1,len(snake)):
                    aux = snake[i] 
                    snake[i] = previous_pos
                    previous_pos = aux  
            else:
                bold = False
                break
            if snake[0] in snake[1:] :
                bold = False
                break  

        if i == 'Right':     
            snake[0][1]= snake[0][1]+1
            varoa = init_array.shape[1]-1   
            if snake[0][1] <= varoa:    
                for i in range(1,len(snake)):
                    aux = snake[i] 
                    snake[i] = previous_pos
                    previous_pos = aux
            else:
                bold = False
                break  
            if snake[0] in snake[1:] :
                bold = False
                break

        if i == 'Up': 
            snake[0][0]= snake[0][0]-1
            if snake[0][0] >= 0  :
                for i in range(1,len(snake)):
                    aux = snake[i] 
                    snake[i] = previous_pos
                    previous_pos = aux
            else:
                bold = False
                break 
            if snake[0] in snake[1:] :
                bold = False
                break  

        if i == 'Down':
            snake[0][0]= snake[0][0]+1
            varoa = init_array.shape[0]-1
            if snake[0][0] <=  varoa:
                for i in range(1,len(snake)):
                    aux = snake[i] 
                    snake[i] = previous_pos
                    previous_pos = aux
                
            else:
                bold = False
                break
            if snake[0] in snake[1:] :
                bold = False
                break

    if bold == True:
        update_matrix(snake,matrix)
        return True


if __name__ == '__main__':
    """
    Take into consideration position of matrix : [rows,columns]
    For the test cases I had to change the position of i and j.
    Before [columns, rows] 
    Now [rows, columns]
    """
    print("---------INSTRUCTIONS---------")

    print("The first values you must choose are for the grid. \nInsert 2 values rows and columns")
    print("\n")
    print("The next step must be inserted after executing")
    print("Following you must insert the snake positions. You must choose option 1,2 or 3")
    print("\n")
    print("The second value you must choose is the depth")


    print("------------------------------")
    #Start program
    parser = argparse.ArgumentParser(description="Select values to run test")
    parser.add_argument("--row",type=int)
    parser.add_argument("--col",type=int)
    parser.add_argument("--snake",type=int,default=1)
    parser.add_argument("--depth",type=int,default=3)
    args = parser.parse_args()
    variables = vars(args)
    
    
    row = variables["row"]
    col = variables["col"]
    snake = variables["snake"]
    #fresh = variables["snake"]
    depth = variables["depth"]
    if snake == 1:
        fresh = [[2,2],[2,3],[1,3],[0,3],[0,2],[0,1],[0,0]]
    elif snake == 2:
        fresh = [[2,0],[1,0],[0,0],[0,1],[1,1],[2,1]]
    elif snake == 3:
        fresh =[[5,5],[5,4],[4,4],[4,5]]

    grid = (row,col)
    
    init_array, snake = init_snake(grid, fresh,fresh)
    combinations  = possible_combinations(depth)
    cont, result = move_snake(combinations, init_array, snake)
    print("We can find: ",  cont)
    print("Those combinations are: ", result)
