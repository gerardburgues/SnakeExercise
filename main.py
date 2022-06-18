import numpy as np
from itertools import combinations_with_replacement,combinations,permutations, product
import copy




def init_snake():
    init_array =  np.zeros(shape=(10,10))
    snake = [[5,5],[4,5],[4,4],[4,5]]
    #Setting snake
    for i in range(0,len(snake)):
        init_array[snake[i][0],snake[i][1]] = 1
    return init_array,snake

def update_matrix(snake,matrix):   
    for i in range(0,len(snake)):
        matrix[snake[i][0],snake[i][1]] = 1
    print(matrix)

def case_of_error(snake, bold,matrix):
    # If there is intersection with snake body then 
    # count as false and jump interation
    if snake[0] in snake[1:] or bold == False:
        print("error here")
        return False
    else:
        update_matrix(snake,matrix)
        print("---------------_GOOD_----------------")
        return True
def possible_combinations(depth):
    #Left Right Up Down
    #Create all possible position for Left Right Up Down
    sample_list =  ['Left', 'Right', 'Up','Down']
    list_combinations = list()
    combinations = [p for p in product(sample_list, repeat=depth)]
    #combinations = list(permutations(sample_list, 3))
    print(combinations)
    #Let's create dictionary for validation of samples
    dict_result = {}
    for comb in combinations:
        dict_result[comb] = False
    return combinations,dict_result
def move_snake(combinations, init_array, snake, dict_result):
    cont = 0
    resultant_array = []
    for i in combinations:
        print("This is combination: " , i)
        init_array, snake = init_snake()
        if direction_snake(init_array, snake, i, dict_result) == True:
            cont +=1
            resultant_array.append(i)

    print(cont)
    print(resultant_array)
def direction_snake(matrix, snake, comb, dict_result):
    #Hem de tenir en consideració que quan j es negativa Error
    #Moving head positions
    print("Cmon!" ,snake)
    #This variable is going to help us just run print 
    #those matrix we are interested (No Error)
    bold = True 
    for i in comb:
        print(i)
        print("this is matrix")
        print(matrix)
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
                print("ERROR")
                bold = False
                break
            if snake[0] in snake[1:] :
                print("ERROR")
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
                print("ERROR")
                bold = False
                break  
            if snake[0] in snake[1:] :
                print("ERROR")
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
                print("ERROR")
                bold = False
                break 
            if snake[0] in snake[1:] :
                print("ERROR")
                bold = False
                break  
        if i == 'Down':
            snake[0][0]= snake[0][0]+1
            print(snake[0][0])
            varoa = init_array.shape[0]-1
            if snake[0][0] <=  varoa:
                for i in range(1,len(snake)):
                    aux = snake[i] 
                    snake[i] = previous_pos
                    previous_pos = aux
                print(snake)
            else:
                print("ERROR")
                bold = False
                break
            if snake[0] in snake[1:] :
                print("ERROR")
                bold = False
                break
    if case_of_error(snake,bold,matrix) == True:
        return True


if __name__ == '__main__':
    #initialize snake
    init_array, snake = init_snake()
    combinations,dict_result  = possible_combinations(4)
    move_snake(combinations, init_array, snake, dict_result)