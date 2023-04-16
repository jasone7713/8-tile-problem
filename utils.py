import copy as copier

#class which holds a saved state of the puzzle
class step:
    #constructor, set default cost to 1 and parent to None
    def __init__(self, state, cost = 1, parent = None):
        self.state = state
        self.parent = parent
        self.cost = cost
    
    #return the i and j coords of the 0 in the current state of the puzzle matrix
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
    
    #(for dijkstra's) given a matrix and i & j coords, return a list of the valid moves preserving left, up, right, down order
    #unique for dijkstra's be returning a cost list for each move
    def find_moves_and_costs(self, visited_steps, curr):
        i, j = self.find_zero()
        matrix = self.state
        moves = []
        costs = []

        #left move valid
        if j > 0:
            temp = swap(matrix, i, j, i, j - 1)
            cost = matrix[i][j - 1]

            flag = is_visited(temp, visited_steps)
            if flag is None:
                moves.append(temp)
                costs.append(cost)
            else:
                if cost + curr.cost < flag.cost and curr is not None:
                    flag.cost = cost + curr.cost
                    flag.parent = curr
        #up move valid
        if i > 0:
            temp = swap(matrix, i, j, i - 1, j)
            cost = matrix[i - 1][j]
            flag = is_visited(temp, visited_steps)
            if flag is None:
                moves.append(temp)
                costs.append(cost)
            else:
                if cost + curr.cost < flag.cost and curr is not None:
                    flag.cost = cost + curr.cost
                    flag.parent = curr

        #right move valid
        if j < (len(matrix[0]) - 1):
            temp = swap(matrix, i, j, i, j + 1)
            cost = matrix[i][j + 1]
            flag = is_visited(temp, visited_steps)
            if flag is None:
                moves.append(temp)
                costs.append(cost)
            else:
                if cost + curr.cost < flag.cost and curr is not None:
                    flag.cost = cost + curr.cost
                    flag.parent = curr

        #down move valid
        if i < (len(matrix) - 1):
            temp = swap(matrix, i, j, i + 1, j)
            cost = matrix[i + 1][j]
            flag = is_visited(temp, visited_steps)
            if flag is None:
                moves.append(temp)
                costs.append(cost)
            else:
                if cost + curr.cost < flag.cost and curr is not None:
                    flag.cost = cost + curr.cost
                    flag.parent = curr
            
        #return possible moves list and cost of each move
        return moves, costs

#given a state, return the path taken to get there as well as the cost
def get_step_list(step):
    step_list = []
    count = 0

    #traverse back-links until parent is none (start state found)
    while step is not None:
        step_list.insert(0, step.state)
        step = step.parent
        count += 1
    return count - 1, step_list

#separate get_step_list for Dijkstra's // same as normal step_list except cost of each move is not 1
def get_step_list_DIJ(step):
    step_list = []
    count = 0
    while step is not None:
        step_list.insert(0, step.state)
        count += step.cost
        step = step.parent
    return count - 1, step_list

#given a matrix and start/end coords, create a copied version that has the start/end coords swapped
def swap(matrix, start_row, start_column, end_row, end_column):

    #use python's deepcopy library to make a true copy of the matrix (cannot be copied by reference)
    copy = copier.deepcopy(matrix)

    #swap i1, j1 with i2, j2
    copy[start_row][start_column], copy[end_row][end_column] = copy[end_row][end_column], copy[start_row][start_column]
    return copy


#given a start and a goal state return if the matrices are equal
def is_equal(start, goal):
    for i in range(len(start)):
        for j in range(len(start[0])):
            if start[i][j] != goal[i][j]:
                return False
    return True

""" deprecated -- now found in the Step class above
#find the index of the 0 (empty space) in the matrix
def find_zero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return i, j
    return -1, -1
"""

#print out an n x n matrix : used for debugging
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()
    print()

#return if a node has beenm visited or not
def is_visited(matrix, visited_steps):
    L = 0
    H = len(visited_steps) - 1

    #binary search on visited_steps list for provided matrix state
    while L <= H:
        mid = (L + H) // 2
        curr = visited_steps[mid].state

        if is_equal(matrix, curr):
            return True
        elif matrix < curr:
            H = mid - 1
        else:
            L = mid + 1

    return False

#insert a step into the sorted visited_steps list using binary search
def insert_matrix(step, visited_steps):
    matrix = step.state
    L = 0
    H = len(visited_steps) - 1

    #binary search for index to place new step
    while L <= H:
        mid = (L + H) // 2
        if visited_steps[mid].state < matrix:
            L = mid + 1
        elif visited_steps[mid].state >= matrix:
            H = mid - 1

    #insert new step in found L index
    visited_steps.insert(L, step)
    