import copy as copier

#class which holds a saved step of the puzzle
class step:
    def __init__(self, state, parent = None):
        self.state = state
        self.parent = parent
        self.future_states = []
    
    def find_zero(self):
        matrix = self.state
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    return i, j
        return -1, -1
    #given a matrix and i & j coords, return a list of the valid moves preserving left, up, right, down order
    def find_moves(self, visited_steps):
        i, j = self.find_zero()
        matrix = self.state
        moves = []

        #left move valid
        if j > 0:
            temp = swap(matrix, i, j, i, j - 1)
            if not is_visited(temp, visited_steps):
                moves.append(temp)
        #up move valid
        if i > 0:
            temp = swap(matrix, i, j, i - 1, j)
            if not is_visited(temp, visited_steps):
                moves.append(temp)
        #right move valid
        if j < (len(matrix[0]) - 1):
            temp = swap(matrix, i, j, i, j + 1)
            if not is_visited(temp, visited_steps):
                moves.append(temp)
        #down move valid
        if i < (len(matrix) - 1):
            temp = swap(matrix, i, j, i + 1, j)
            if not is_visited(temp, visited_steps):
                moves.append(temp)
            
        return moves

#given a state, return the path taken to get there
def get_step_list(step):
    step_list = []
    while step is not None:
        step_list.insert(0, step.state)
        step = step.parent
    return step_list

#given a matrix and start/end coords, create a copied version that has the start/end coords swapped
def swap(matrix, start_row, start_column, end_row, end_column):
    copy = copier.deepcopy(matrix)
    copy[start_row][start_column], copy[end_row][end_column] = copy[end_row][end_column], copy[start_row][start_column]
    return copy


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

#print out an n x n matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()
    print()

def is_visited(matrix, visited_steps):
    for i in visited_steps:
        curr = i.state
        if is_equal(matrix, curr):
            return True
    return False