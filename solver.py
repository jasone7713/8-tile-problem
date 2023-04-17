import dfs
import bfs
import dijkstra
import time

#solve the puzzle given a start state, end start, and method => 'BFS', 'DFS', 'DIJ'
def solve(start, goal, method, quiet=False):

    #check if the problem is solvable before proceeding
    if not is_solvable(start, goal):
        print('Error: the problem is not solvable')
        return
    
    #log start time for testing
    start_time = time.time()

    #call algorithms based on provided algo
    if 'DFS' in method.upper():
        cost, steps = dfs.solve_iterative(start, goal)
    elif 'BFS' in method.upper():
        cost, steps = bfs.solve(start, goal)
    elif 'DIJ' in method.upper():
        cost, steps = dijkstra.solve(start, goal)
    else:
        print(f'Error {method} is an unrecognized method')
        return

    #log and print end time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds.", end='\n\n')

    #print the moves and the cost to solve (if quiet set to true do not ouput)
    if not quiet:
        for i in steps:
            print_matrix(i)
            print()
    
    print(f'The overall cost for solving with {method} was: {cost}. See above for the moves taken')

#BELOW THIS POINT ARE HELPER FUNCTIONS USED BY SOLVE
    
#print out an n x n matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()

#given 2 n x n matrices check if the problem is solvable: return true if solvable
def is_solvable(start, goal):
    if not is_valid_matrix(start) or not is_valid_matrix(goal):
        print('Error: invalid matrix entered (make sure values are 0 - 8)')

    c1 = inversion_count(start)
    c2 = inversion_count(goal)

    #check if both even or both odd via XAND (~XOR) operation
    return True if not ((c1 % 2 == 0) ^ (c2 % 2 == 0)) else False

#make sure that each value 0 - 8 occurs exactly once
def is_valid_matrix(matrix):
    n = len(matrix)

    #map how many times each value occurs
    direct_map = [0] * (n * n)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            val = matrix[i][j]
            if val < 0 or val > ((n * n)- 1):   #0-9 check
                return False
            direct_map[val] += 1

    #0 - 9 must occur exactly once, else rreturn false
    for i in direct_map:
        if i != 1:
            return False
    return True

#given an n x n matrix return the number of inversions
def inversion_count(matrix):
    inv_count = 0
    m = len(matrix)
    n = m * m
    data = []

    #make a 1D list of all numbers in matrix -- this is just to make the inversion counter simpler to run
    for i in range(m):
        for j in range(m):
            data.append(matrix[i][j])

    #count the number of inversions that occur in the list
    for i in range(n):
        for j in range(i, n):
            if data[i] != 0 and data[j] != 0:
                if data[j] < data[i]:
                    inv_count += 1
    return inv_count