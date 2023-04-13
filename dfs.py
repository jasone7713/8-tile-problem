import utils
import sys
#sys.setrecursionlimit(10000)   #uncomment this if you are using the recursive version


def solve(start, goal):
    if utils.is_equal(start, goal):
        return 0, []
    visited_steps = []
    s = utils.step(start)
    utils.insert_matrix(s, visited_steps)
    
    test = recurse(s, goal, visited_steps)
    print(type(test))
    return test
    

def recurse(current, goal, visited_steps):
    if utils.is_equal(current.state, goal):
        print('it happened')
        return utils.get_step_list(current)
    
    moves = current.find_moves(visited_steps)
    for move in moves:
        child = utils.step(move, current)
        utils.insert_matrix(child, visited_steps)
        solution = recurse(child, goal, visited_steps)
        if solution is not None:
            return solution


#solve using bfs approach
def solve_iterative(start, goal):
    cost = 0
    if utils.is_equal(start, goal):
        return cost, [utils.step(start)]
    
    visited_steps = []
    queue = []
    queue.append(utils.step(start))
    
    while queue:
        curr = queue.pop(0)
        if utils.is_equal(curr.state, goal):
            #returns count, step_list as a tuple
            return utils.get_step_list(curr)
        else:
            utils.insert_matrix(curr, visited_steps)
            moves = curr.find_moves(visited_steps)
            for i in range(len(moves)-1, -1, -1):
                move = moves[i]
                temp = utils.step(move, parent=curr)
                queue.insert(0, temp)

    return -1, []
