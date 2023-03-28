#solve using bfs approach
def solve(start, goal):
    cost = 0
    if is_equal(start, goal):
        return cost
    
    #bfs queue // list, use append and pop methods to simulate queue behavior
    queue = []

    #coords of the 0 in start matrix
    queue.append(find_zero(start))
    
    while len(queue) > 0:
        state = queue.pop()
        i, j = state
        if start[i][j] != goal[i][j]:
            None



#given a start and a goal state return if the matrices are equal
def is_equal(start, goal):
    for i in range(len(start)):
        for j in range(len(start[0])):
            if start[i][j] != goal[i][j]:
                return False
    return True

#find the index of the 0 (empty space) in the matrix
def find_zero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return i, j
    return -1, -1