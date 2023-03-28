import dfs
import bfs
import dijkstra

#solve the puzzle given a start state, end start, and method => 'BFS', 'DFS', 'DIJ'
def solve(start, goal, method):
    if not is_solvable(start, goal):
        print('Error: the problem is not solvable')

    if 'DFS' in method.upper():
        None
    elif 'BFS' in method.upper():
        cost, steps = bfs.solve(start, goal)
    elif 'DIJ' in method.upper():
        None
    else:
        print(f'Error {method} is an unrecognized method')
        return

    print(f'The overall cost was: {cost} moves')
    for i in steps:
        print_matrix(i)
        print()
    
#print out an n x n matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()

#given 2 n x n matrices check if the problem is solvable: return true if solvable
def is_solvable(start, goal):
    c1 = inversion_count(start)
    c2 = inversion_count(goal)

    #check if both even or both odd via XAND (~XOR) operation
    return True if not ((c1 % 2 == 0) ^ (c2 % 2 == 0)) else False

#given an n x n matrix return the number of inversions
def inversion_count(matrix):
    inv_count = 0
    m = len(matrix)
    n = m * m
    data = []

    for i in range(m):
        for j in range(m):
            data.append(matrix[i][j])

    for i in range(n):
        for j in range(i, n):
            if data[i] != 0 and data[j] != 0:
                if data[j] < data[i]:
                    inv_count += 1
    return inv_count